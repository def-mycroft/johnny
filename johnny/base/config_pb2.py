# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='johnny',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63onfig.proto\x12\x06johnny\"\xb1\x01\n\x06\x43onfig\x12\x1d\n\x05input\x18\x01 \x01(\x0b\x32\x0e.johnny.Inputs\x12\x1d\n\x06\x63hains\x18\x02 \x03(\x0b\x32\r.johnny.Chain\x12\'\n\x11transaction_links\x18\x03 \x03(\x0b\x32\x0c.johnny.Link\x12!\n\x0border_links\x18\x04 \x03(\x0b\x32\x0c.johnny.Link\x12\x1d\n\x06prices\x18\x05 \x03(\x0b\x32\r.johnny.Price\"+\n\x06Inputs\x12!\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32\x0f.johnny.Account\"\x91\x01\n\x07\x41\x63\x63ount\x12\x10\n\x08nickname\x18\x01 \x01(\t\x12(\n\x07logtype\x18\x02 \x01(\x0e\x32\x17.johnny.Account.LogType\x12\x0e\n\x06module\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\"*\n\x07LogType\x12\x10\n\x0cTRANSACTIONS\x10\x01\x12\r\n\tPOSITIONS\x10\x02\"$\n\x04Link\x12\x0f\n\x07\x63omment\x18\x01 \x01(\t\x12\x0b\n\x03ids\x18\x02 \x03(\t\"j\n\x05\x43hain\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t\x12\x12\n\ntrade_type\x18\x02 \x01(\t\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x12\x17\n\x0ftransaction_ids\x18\x04 \x03(\t\x12\x11\n\torder_ids\x18\x05 \x03(\t\":\n\x05\x41sset\x12\x12\n\ninstrument\x18\x01 \x01(\t\x12\r\n\x05\x63lass\x18\x02 \x01(\t\x12\x0e\n\x06\x66\x61\x63tor\x18\x03 \x01(\t\"B\n\x05Price\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x1a\n\x04\x64\x61te\x18\x02 \x01(\x0b\x32\x0c.johnny.Date\x12\r\n\x05price\x18\x03 \x01(\t\"0\n\x04\x44\x61te\x12\x0c\n\x04year\x18\x02 \x01(\x05\x12\r\n\x05month\x18\x03 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\x05'
)



_ACCOUNT_LOGTYPE = _descriptor.EnumDescriptor(
  name='LogType',
  full_name='johnny.Account.LogType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRANSACTIONS', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POSITIONS', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=353,
  serialized_end=395,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNT_LOGTYPE)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='johnny.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='johnny.Config.input', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chains', full_name='johnny.Config.chains', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transaction_links', full_name='johnny.Config.transaction_links', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_links', full_name='johnny.Config.order_links', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prices', full_name='johnny.Config.prices', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=202,
)


_INPUTS = _descriptor.Descriptor(
  name='Inputs',
  full_name='johnny.Inputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accounts', full_name='johnny.Inputs.accounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=247,
)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='johnny.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nickname', full_name='johnny.Account.nickname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logtype', full_name='johnny.Account.logtype', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module', full_name='johnny.Account.module', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='johnny.Account.source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACCOUNT_LOGTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=395,
)


_LINK = _descriptor.Descriptor(
  name='Link',
  full_name='johnny.Link',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='comment', full_name='johnny.Link.comment', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ids', full_name='johnny.Link.ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=397,
  serialized_end=433,
)


_CHAIN = _descriptor.Descriptor(
  name='Chain',
  full_name='johnny.Chain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chain_id', full_name='johnny.Chain.chain_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trade_type', full_name='johnny.Chain.trade_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comment', full_name='johnny.Chain.comment', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transaction_ids', full_name='johnny.Chain.transaction_ids', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_ids', full_name='johnny.Chain.order_ids', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=541,
)


_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='johnny.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instrument', full_name='johnny.Asset.instrument', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='class', full_name='johnny.Asset.class', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='factor', full_name='johnny.Asset.factor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=543,
  serialized_end=601,
)


_PRICE = _descriptor.Descriptor(
  name='Price',
  full_name='johnny.Price',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='johnny.Price.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date', full_name='johnny.Price.date', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='johnny.Price.price', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=669,
)


_DATE = _descriptor.Descriptor(
  name='Date',
  full_name='johnny.Date',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='johnny.Date.year', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='month', full_name='johnny.Date.month', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='day', full_name='johnny.Date.day', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=671,
  serialized_end=719,
)

_CONFIG.fields_by_name['input'].message_type = _INPUTS
_CONFIG.fields_by_name['chains'].message_type = _CHAIN
_CONFIG.fields_by_name['transaction_links'].message_type = _LINK
_CONFIG.fields_by_name['order_links'].message_type = _LINK
_CONFIG.fields_by_name['prices'].message_type = _PRICE
_INPUTS.fields_by_name['accounts'].message_type = _ACCOUNT
_ACCOUNT.fields_by_name['logtype'].enum_type = _ACCOUNT_LOGTYPE
_ACCOUNT_LOGTYPE.containing_type = _ACCOUNT
_PRICE.fields_by_name['date'].message_type = _DATE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['Inputs'] = _INPUTS
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['Link'] = _LINK
DESCRIPTOR.message_types_by_name['Chain'] = _CHAIN
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['Price'] = _PRICE
DESCRIPTOR.message_types_by_name['Date'] = _DATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Config)
  })
_sym_db.RegisterMessage(Config)

Inputs = _reflection.GeneratedProtocolMessageType('Inputs', (_message.Message,), {
  'DESCRIPTOR' : _INPUTS,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Inputs)
  })
_sym_db.RegisterMessage(Inputs)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Account)
  })
_sym_db.RegisterMessage(Account)

Link = _reflection.GeneratedProtocolMessageType('Link', (_message.Message,), {
  'DESCRIPTOR' : _LINK,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Link)
  })
_sym_db.RegisterMessage(Link)

Chain = _reflection.GeneratedProtocolMessageType('Chain', (_message.Message,), {
  'DESCRIPTOR' : _CHAIN,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Chain)
  })
_sym_db.RegisterMessage(Chain)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), {
  'DESCRIPTOR' : _ASSET,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Asset)
  })
_sym_db.RegisterMessage(Asset)

Price = _reflection.GeneratedProtocolMessageType('Price', (_message.Message,), {
  'DESCRIPTOR' : _PRICE,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Price)
  })
_sym_db.RegisterMessage(Price)

Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), {
  'DESCRIPTOR' : _DATE,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:johnny.Date)
  })
_sym_db.RegisterMessage(Date)


# @@protoc_insertion_point(module_scope)
