# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/mime_type.proto

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
  name='google/ads/googleads_v1/proto/enums/mime_type.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\rMimeTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\n3google/ads/googleads_v1/proto/enums/mime_type.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\xdc\x01\n\x0cMimeTypeEnum\"\xcb\x01\n\x08MimeType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0e\n\nIMAGE_JPEG\x10\x02\x12\r\n\tIMAGE_GIF\x10\x03\x12\r\n\tIMAGE_PNG\x10\x04\x12\t\n\x05\x46LASH\x10\x05\x12\r\n\tTEXT_HTML\x10\x06\x12\x07\n\x03PDF\x10\x07\x12\n\n\x06MSWORD\x10\x08\x12\x0b\n\x07MSEXCEL\x10\t\x12\x07\n\x03RTF\x10\n\x12\r\n\tAUDIO_WAV\x10\x0b\x12\r\n\tAUDIO_MP3\x10\x0c\x12\x10\n\x0cHTML5_AD_ZIP\x10\rB\xe2\x01\n!com.google.ads.googleads.v1.enumsB\rMimeTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_MIMETYPEENUM_MIMETYPE = _descriptor.EnumDescriptor(
  name='MimeType',
  full_name='google.ads.googleads.v1.enums.MimeTypeEnum.MimeType',
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
      name='IMAGE_JPEG', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_GIF', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_PNG', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLASH', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_HTML', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PDF', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSWORD', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSEXCEL', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTF', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIO_WAV', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIO_MP3', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTML5_AD_ZIP', index=13, number=13,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=134,
  serialized_end=337,
)
_sym_db.RegisterEnumDescriptor(_MIMETYPEENUM_MIMETYPE)


_MIMETYPEENUM = _descriptor.Descriptor(
  name='MimeTypeEnum',
  full_name='google.ads.googleads.v1.enums.MimeTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MIMETYPEENUM_MIMETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=337,
)

_MIMETYPEENUM_MIMETYPE.containing_type = _MIMETYPEENUM
DESCRIPTOR.message_types_by_name['MimeTypeEnum'] = _MIMETYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MimeTypeEnum = _reflection.GeneratedProtocolMessageType('MimeTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _MIMETYPEENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.mime_type_pb2'
  ,
  __doc__ = """Container for enum describing the mime types.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.MimeTypeEnum)
  ))
_sym_db.RegisterMessage(MimeTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
