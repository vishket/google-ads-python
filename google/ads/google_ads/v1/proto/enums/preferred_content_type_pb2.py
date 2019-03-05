# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/preferred_content_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/enums/preferred_content_type.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\031PreferredContentTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\n@google/ads/googleads_v1/proto/enums/preferred_content_type.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"j\n\x18PreferredContentTypeEnum\"N\n\x14PreferredContentType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x18\n\x13YOUTUBE_TOP_CONTENT\x10\x90\x03\x42\xee\x01\n!com.google.ads.googleads.v1.enumsB\x19PreferredContentTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_PREFERREDCONTENTTYPEENUM_PREFERREDCONTENTTYPE = _descriptor.EnumDescriptor(
  name='PreferredContentType',
  full_name='google.ads.googleads.v1.enums.PreferredContentTypeEnum.PreferredContentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE_TOP_CONTENT', index=2, number=400,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=157,
  serialized_end=235,
)
_sym_db.RegisterEnumDescriptor(_PREFERREDCONTENTTYPEENUM_PREFERREDCONTENTTYPE)


_PREFERREDCONTENTTYPEENUM = _descriptor.Descriptor(
  name='PreferredContentTypeEnum',
  full_name='google.ads.googleads.v1.enums.PreferredContentTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFERREDCONTENTTYPEENUM_PREFERREDCONTENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=235,
)

_PREFERREDCONTENTTYPEENUM_PREFERREDCONTENTTYPE.containing_type = _PREFERREDCONTENTTYPEENUM
DESCRIPTOR.message_types_by_name['PreferredContentTypeEnum'] = _PREFERREDCONTENTTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PreferredContentTypeEnum = _reflection.GeneratedProtocolMessageType('PreferredContentTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _PREFERREDCONTENTTYPEENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.preferred_content_type_pb2'
  ,
  __doc__ = """Container for enumeration of preferred content criterion type.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.PreferredContentTypeEnum)
  ))
_sym_db.RegisterMessage(PreferredContentTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
