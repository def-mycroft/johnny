"""A new version of the matching code, which integrates state-based processing.

This code processes a transactions log in order and matches reductions of
positions against each other, in order to:

- Set the position effect where it is missing in the input,
- Split rows for futures crossing the null position boundary,
- Compute expiration quantities and signs,
- Creates a corresponding match id column to save this in the table.
- Add missing expiration rows (thinkorswim suffers from some of these),

TODO(blais):
- Add mark rows for positions still open and active,

Note that adding opening rows for positions created before the transactions time
window is done separately (see discovery.ReadInitialPositions).

The purpose is to (a) relax the requirements on the particular importers and (b)
run through a single loop of this expensive accumulation (for performance
reasons). The result we seek is a log with the ability to be processed without
any state accumulation--all fields correctly rectified with proper
opening/closing effect and opening and marking entries. This makes any further
processing much easier and faster.

All of this processing requires state accumulation and correction for missing
information before the beginning of the transaction log, and is reasonably
difficult to factor into independent pieces, because the corrections affect the
rest of the computations.

Basically, if you have only a partial window of time of a transactions log, you
have to be ready to reconcile:

1. positions opened and closed within the window
2. positions opened BEFORE the window and closed within the window
3. positions opened within the window and never closed (or closed after the window, if the window isn't up to now)
4. positions opened before the window, and never closed during the window (or closed after the window)

Comments:

- (1) is never a problem.
- (2) will require synthesizing a fake opening trade, and can be detected by
  their unmatched closing
- (3) is going to result in residual positions leftover in the inventory
  accumulator after processing the log
- (4) is basically undetectable, except if you have a positions file to
  reconcile against (you will find positions you didn't expect and for those you
  need to synthesize opens for those)

Finally, we'd like to do away with a "current positions" log; if one is
provided, the positions computed from this code can be asserted and missing
positions can be inserted.

"""

__copyright__ = "Copyright (C) 2021  Martin Blais"
__license__ = "GNU GPLv2"

import datetime
import collections
import itertools
import logging
from decimal import Decimal
from typing import Any, Dict, Mapping, NamedTuple, Optional, Tuple

from johnny.base.etl import petl, AssertColumns, Table, Record
from johnny.base import instrument
from johnny.base import inventories


ZERO = Decimal(0)


class InstKey(NamedTuple):
    """Instrument key."""
    account: str
    symbol: str


def Process(transactions: Table,
            mark_time: Optional[datetime.datetime]=None) -> Table:
    """Run state-based processing over the transactions log.

    Args:
      transactions: The table of transactions, as normalized by each importer code.
      mark_time: The datetime to use for marking position.
    Returns:
      A fixed up table, as per the description of this module.
    """
    AssertColumns(transactions,
                  ('account', str),
                  ('transaction_id', str),
                  ('datetime', datetime.datetime),
                  ('rowtype', str),
                  ('order_id', str),
                  ('symbol', str),
                  ('effect', str),
                  ('instruction', str),
                  ('quantity', Decimal),
                  ('price', Decimal),
                  ('cost', Decimal),
                  ('commissions', Decimal),
                  ('fees', Decimal),
                  ('description', str))

    # Create a mapping of transaction ids to matches.
    transactions, invs = _AccumulateStateAndTransform(transactions)

    return transactions


def _GetExpirationDate() -> datetime.date:
    """Get the expiration date. Override for tests."""
    return datetime.date.today()


def _AccumulateStateAndTransform(transactions: Table) -> Tuple[Table, dict[str, Decimal]]:
    """Run inventory matching on the raw log and transform it.

    Args:
      transactions: The raw transactions table from the broker converter, with
        instrument expanded.
    Returns:
      A pair of
        transactions: Processed, transformed and normalized transactions (see docstring).
        invs: A dict of of InstKey tuples to (position, basis, match-id) tuples.
    """
    debug = False
    invs = collections.defaultdict(lambda: inventories.OpenCloseFifoInventory(debug=debug))

    # Accumulator for new records to output.
    new_rows = []
    def accum(nrec, modtype):
        new_rows.append(nrec)

    def accum_debug(nrec, modtype):
        if nrec is not rec:
            print(modtype)
            print(rec)
            print(nrec)
            print()
        new_rows.append(nrec)

    # Note: Unfortunately we require two sortings; one to ensure that inventory
    # matching is done properly, and a final one to reorder the newly
    # synthesized outputs {123a4903c212}.
    transactions = (transactions
                    .addfield('match_id', '')
                    .sort('datetime'))
    for rec in transactions.namedtuples():
        inv = invs[InstKey(rec.account, rec.symbol)]

        if rec.rowtype in {'Trade', 'Open'}:
            if rec.effect == 'OPENING':
                inv.opening(rec, accum)
            elif rec.effect == 'CLOSING':
                inv.closing(rec, accum)
            else:
                assert not rec.effect
                inv.match(rec, accum)

        elif rec.rowtype == 'Expire':
            inv.expire(rec, accum)

        else:
            raise ValueError(f"Invalid row type: {rec.rowtype}")

    # Insert missing expirations.
    prototype = type(rec)(*[None] * len(transactions.header()))
    AddMissingExpirations(invs, _GetExpirationDate(), accum, prototype)

    # Produce final set of positions (cull inventories with no positions).
    positions = {key: inv.quantity()
                 for key, inv in invs.items()
                 if inv.quantity() != ZERO or inv.cost() != ZERO}

    # Note: We sort again to ensure newly synthesized outputs are ordered
    # properly {123a4903c212}.
    new_transactions = (petl.wrap(itertools.chain([transactions.header()], new_rows))
                        .sort('datetime'))
    return new_transactions, positions


def AddMissingExpirations(invs: dict[str, Decimal],
                          current_date: datetime.datetime,
                          accum: inventories.TxnAccumFn,
                          prototype_row: tuple) -> Table:
    """Create missing expirations. Some sources miss them."""

    for key, inv in sorted(invs.items()):
        inst = instrument.FromString(key.symbol)
        if (inst.expiration is not None and
            inst.expiration < current_date and
            inv.quantity() != ZERO):
            expiration_time = datetime.datetime.combine(
                inst.expiration + datetime.timedelta(days=1),
                datetime.time(0, 0, 0))
            rec = prototype_row._replace(
                account=key.account,
                symbol=key.symbol,
                datetime=expiration_time,
                description=f'Synthetic expiration for {key.symbol}',
                cost=ZERO,
                price=ZERO,
                quantity=ZERO,
                commissions=ZERO,
                fees=ZERO)
            inv.expire(rec, accum)
