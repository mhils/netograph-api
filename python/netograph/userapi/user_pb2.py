# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: userapi/user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='userapi/user.proto',
  package='io.netograph.user',
  syntax='proto3',
  serialized_options=_b('Z\007userapi'),
  serialized_pb=_b('\n\x12userapi/user.proto\x12\x11io.netograph.user\x1a\x1fgoogle/protobuf/timestamp.proto\"&\n\x08Metadata\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x11\n\x0f\x44\x61tasetsRequest\"|\n\x07\x44\x61taset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0f\n\x07urlbase\x18\x03 \x01(\t\x12+\n\x07\x64\x65leted\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08readonly\x18\x05 \x01(\x08\"q\n\x12TempCaptureRequest\x12\x14\n\x0cnotification\x18\x01 \x01(\t\x12\x0c\n\x04urls\x18\x02 \x03(\t\x12)\n\x04meta\x18\x03 \x03(\x0b\x32\x1b.io.netograph.user.Metadata\x12\x0c\n\x04zone\x18\x04 \x01(\t\"/\n\x11TempCaptureResult\x12\x0e\n\x06\x61ssets\x18\x01 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t2\xb0\x01\n\x04User\x12Z\n\x0bTempCapture\x12%.io.netograph.user.TempCaptureRequest\x1a$.io.netograph.user.TempCaptureResult\x12L\n\x08\x44\x61tasets\x12\".io.netograph.user.DatasetsRequest\x1a\x1a.io.netograph.user.Dataset0\x01\x42\tZ\x07userapib\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='io.netograph.user.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='io.netograph.user.Metadata.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='io.netograph.user.Metadata.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=112,
)


_DATASETSREQUEST = _descriptor.Descriptor(
  name='DatasetsRequest',
  full_name='io.netograph.user.DatasetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=131,
)


_DATASET = _descriptor.Descriptor(
  name='Dataset',
  full_name='io.netograph.user.Dataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='io.netograph.user.Dataset.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='io.netograph.user.Dataset.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urlbase', full_name='io.netograph.user.Dataset.urlbase', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='io.netograph.user.Dataset.deleted', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readonly', full_name='io.netograph.user.Dataset.readonly', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=257,
)


_TEMPCAPTUREREQUEST = _descriptor.Descriptor(
  name='TempCaptureRequest',
  full_name='io.netograph.user.TempCaptureRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification', full_name='io.netograph.user.TempCaptureRequest.notification', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urls', full_name='io.netograph.user.TempCaptureRequest.urls', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='io.netograph.user.TempCaptureRequest.meta', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone', full_name='io.netograph.user.TempCaptureRequest.zone', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=372,
)


_TEMPCAPTURERESULT = _descriptor.Descriptor(
  name='TempCaptureResult',
  full_name='io.netograph.user.TempCaptureResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='assets', full_name='io.netograph.user.TempCaptureResult.assets', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='io.netograph.user.TempCaptureResult.id', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=374,
  serialized_end=421,
)

_DATASET.fields_by_name['deleted'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TEMPCAPTUREREQUEST.fields_by_name['meta'].message_type = _METADATA
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['DatasetsRequest'] = _DATASETSREQUEST
DESCRIPTOR.message_types_by_name['Dataset'] = _DATASET
DESCRIPTOR.message_types_by_name['TempCaptureRequest'] = _TEMPCAPTUREREQUEST
DESCRIPTOR.message_types_by_name['TempCaptureResult'] = _TEMPCAPTURERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), dict(
  DESCRIPTOR = _METADATA,
  __module__ = 'userapi.user_pb2'
  # @@protoc_insertion_point(class_scope:io.netograph.user.Metadata)
  ))
_sym_db.RegisterMessage(Metadata)

DatasetsRequest = _reflection.GeneratedProtocolMessageType('DatasetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _DATASETSREQUEST,
  __module__ = 'userapi.user_pb2'
  # @@protoc_insertion_point(class_scope:io.netograph.user.DatasetsRequest)
  ))
_sym_db.RegisterMessage(DatasetsRequest)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), dict(
  DESCRIPTOR = _DATASET,
  __module__ = 'userapi.user_pb2'
  # @@protoc_insertion_point(class_scope:io.netograph.user.Dataset)
  ))
_sym_db.RegisterMessage(Dataset)

TempCaptureRequest = _reflection.GeneratedProtocolMessageType('TempCaptureRequest', (_message.Message,), dict(
  DESCRIPTOR = _TEMPCAPTUREREQUEST,
  __module__ = 'userapi.user_pb2'
  # @@protoc_insertion_point(class_scope:io.netograph.user.TempCaptureRequest)
  ))
_sym_db.RegisterMessage(TempCaptureRequest)

TempCaptureResult = _reflection.GeneratedProtocolMessageType('TempCaptureResult', (_message.Message,), dict(
  DESCRIPTOR = _TEMPCAPTURERESULT,
  __module__ = 'userapi.user_pb2'
  # @@protoc_insertion_point(class_scope:io.netograph.user.TempCaptureResult)
  ))
_sym_db.RegisterMessage(TempCaptureResult)


DESCRIPTOR._options = None

_USER = _descriptor.ServiceDescriptor(
  name='User',
  full_name='io.netograph.user.User',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=424,
  serialized_end=600,
  methods=[
  _descriptor.MethodDescriptor(
    name='TempCapture',
    full_name='io.netograph.user.User.TempCapture',
    index=0,
    containing_service=None,
    input_type=_TEMPCAPTUREREQUEST,
    output_type=_TEMPCAPTURERESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Datasets',
    full_name='io.netograph.user.User.Datasets',
    index=1,
    containing_service=None,
    input_type=_DATASETSREQUEST,
    output_type=_DATASET,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USER)

DESCRIPTOR.services_by_name['User'] = _USER

# @@protoc_insertion_point(module_scope)
