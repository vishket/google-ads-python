# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/errors/keyword_plan_keyword_error.proto

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
  name='google/ads/googleads_v1/proto/errors/keyword_plan_keyword_error.proto',
  package='google.ads.googleads.v1.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v1.errorsB\034KeywordPlanKeywordErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Errors\312\002\036Google\\Ads\\GoogleAds\\V1\\Errors\352\002\"Google::Ads::GoogleAds::V1::Errors'),
  serialized_pb=_b('\nEgoogle/ads/googleads_v1/proto/errors/keyword_plan_keyword_error.proto\x12\x1egoogle.ads.googleads.v1.errors\x1a\x1cgoogle/api/annotations.proto\"\x82\x02\n\x1bKeywordPlanKeywordErrorEnum\"\xe2\x01\n\x17KeywordPlanKeywordError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1e\n\x1aINVALID_KEYWORD_MATCH_TYPE\x10\x02\x12\x15\n\x11\x44UPLICATE_KEYWORD\x10\x03\x12\x19\n\x15KEYWORD_TEXT_TOO_LONG\x10\x04\x12\x1d\n\x19KEYWORD_HAS_INVALID_CHARS\x10\x05\x12\x1e\n\x1aKEYWORD_HAS_TOO_MANY_WORDS\x10\x06\x12\x18\n\x14INVALID_KEYWORD_TEXT\x10\x07\x42\xf7\x01\n\"com.google.ads.googleads.v1.errorsB\x1cKeywordPlanKeywordErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Errors\xea\x02\"Google::Ads::GoogleAds::V1::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_KEYWORDPLANKEYWORDERRORENUM_KEYWORDPLANKEYWORDERROR = _descriptor.EnumDescriptor(
  name='KeywordPlanKeywordError',
  full_name='google.ads.googleads.v1.errors.KeywordPlanKeywordErrorEnum.KeywordPlanKeywordError',
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
      name='INVALID_KEYWORD_MATCH_TYPE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_KEYWORD', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYWORD_TEXT_TOO_LONG', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYWORD_HAS_INVALID_CHARS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYWORD_HAS_TOO_MANY_WORDS', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_KEYWORD_TEXT', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=168,
  serialized_end=394,
)
_sym_db.RegisterEnumDescriptor(_KEYWORDPLANKEYWORDERRORENUM_KEYWORDPLANKEYWORDERROR)


_KEYWORDPLANKEYWORDERRORENUM = _descriptor.Descriptor(
  name='KeywordPlanKeywordErrorEnum',
  full_name='google.ads.googleads.v1.errors.KeywordPlanKeywordErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _KEYWORDPLANKEYWORDERRORENUM_KEYWORDPLANKEYWORDERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=394,
)

_KEYWORDPLANKEYWORDERRORENUM_KEYWORDPLANKEYWORDERROR.containing_type = _KEYWORDPLANKEYWORDERRORENUM
DESCRIPTOR.message_types_by_name['KeywordPlanKeywordErrorEnum'] = _KEYWORDPLANKEYWORDERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeywordPlanKeywordErrorEnum = _reflection.GeneratedProtocolMessageType('KeywordPlanKeywordErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _KEYWORDPLANKEYWORDERRORENUM,
  __module__ = 'google.ads.googleads_v1.proto.errors.keyword_plan_keyword_error_pb2'
  ,
  __doc__ = """Container for enum describing possible errors from applying a keyword or
  a negative keyword from a keyword plan.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.errors.KeywordPlanKeywordErrorEnum)
  ))
_sym_db.RegisterMessage(KeywordPlanKeywordErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
