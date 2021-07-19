"""Find the files to form the database.

We rely on patterns and dates and sorting to sieve the latest files of every
type in a bungled directory of downloads. For now.
"""

__copyright__ = "Copyright (C) 2021  Martin Blais"
__license__ = "GNU GPLv2"

from decimal import Decimal
from os import path
from typing import Callable, Dict, List, Optional, Tuple
import collections
import glob
import importlib
import os

from more_itertools import last
from dateutil import parser

from johnny.base.etl import petl, Table
from johnny.base import chains
from johnny.base import match
from johnny.base import transactions as txnlib
from johnny.base import config as configlib
from johnny.sources.thinkorswim_csv import positions as positions_tos
from johnny.sources.thinkorswim_csv import transactions as transactions_tos
from johnny.sources.tastyworks_csv import positions as positions_tw
from johnny.sources.tastyworks_csv import transactions as transactions_tw


ZERO = Decimal(0)


def GetLatestFile(source: str) -> str:
    """Given a globbing pattern, find the most recent file matching the pattern,
    based on the timestamp."""
    filenames = sorted((path.getctime(filename), filename)
                       for filename in glob.glob(source, recursive=True))
    _, filename = last(filenames)
    return filename


def ReadInitialPositions(filename: str) -> Table:
    """Read a table of initial positions."""
    table = (petl.fromcsv(filename)
            .cut('datetime', 'symbol', 'instruction', 'quantity', 'cost')

            .addfield('transaction_id', lambda r: 'open-{}'.format(r.symbol))
            .addfield('account', '')
            .convert('datetime', lambda v: parser.parse(v))
            .addfield('rowtype', 'Open')
            .addfield('effect', 'OPENING')
            .convert('quantity', Decimal)
            .convert('cost', Decimal)
            .addfield('price', lambda r: r.cost / r.quantity)
            .addfield('commissions', ZERO)
            .addfield('fees', ZERO)
            .addfield('description', lambda r: "Opening balance for {}".format(r.symbol))
            .addfield('order_id', '')

            .cut(txnlib.FIELDS))

    # TODO(blais): Support multiplier in here. In the meantime, detect and fail
    # if present.
    if table.select(lambda r: r.symbol.startswith('/')).nrows() > 0:
        raise ValueError("Futures are not supported")
    return table


def ReadConfiguredInputs(
        config: configlib.Config) -> Dict[int, Table]:
    """Read the explicitly configured inputs in the config file.
    Returns tables for the transactions and positions."""

    # Parse and accumulate by log type.
    tablemap = collections.defaultdict(list)
    for account in config.input.accounts:
        output_tables = tablemap[account.logtype]

        # Incorporate initial positions.
        if account.initial:
            table = ReadInitialPositions(account.initial)
            if table is not None:
                output_tables.append(table.update('account', account.nickname))

        # Import module transactions.
        module = importlib.import_module(account.module)
        table = module.Import(account.source)
        if table is not None:
            output_tables.append(table.update('account', account.nickname))

    # Concatenate tables for each logtype.
    bytype = {}
    for logtype, tables in tablemap.items():
        bytype[logtype] = (petl.cat(*tables)
                           .sort(('account', 'datetime')))

    return bytype
