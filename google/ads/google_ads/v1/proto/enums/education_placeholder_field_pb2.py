# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/education_placeholder_field.proto

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
  name='google/ads/googleads_v1/proto/enums/education_placeholder_field.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\036EducationPlaceholderFieldProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\nEgoogle/ads/googleads_v1/proto/enums/education_placeholder_field.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\xbf\x03\n\x1d\x45\x64ucationPlaceholderFieldEnum\"\x9d\x03\n\x19\x45\x64ucationPlaceholderField\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0e\n\nPROGRAM_ID\x10\x02\x12\x0f\n\x0bLOCATION_ID\x10\x03\x12\x10\n\x0cPROGRAM_NAME\x10\x04\x12\x11\n\rAREA_OF_STUDY\x10\x05\x12\x17\n\x13PROGRAM_DESCRIPTION\x10\x06\x12\x0f\n\x0bSCHOOL_NAME\x10\x07\x12\x0b\n\x07\x41\x44\x44RESS\x10\x08\x12\x17\n\x13THUMBNAIL_IMAGE_URL\x10\t\x12#\n\x1f\x41LTERNATIVE_THUMBNAIL_IMAGE_URL\x10\n\x12\x0e\n\nFINAL_URLS\x10\x0b\x12\x15\n\x11\x46INAL_MOBILE_URLS\x10\x0c\x12\x10\n\x0cTRACKING_URL\x10\r\x12\x17\n\x13\x43ONTEXTUAL_KEYWORDS\x10\x0e\x12\x14\n\x10\x41NDROID_APP_LINK\x10\x0f\x12\x17\n\x13SIMILAR_PROGRAM_IDS\x10\x10\x12\x10\n\x0cIOS_APP_LINK\x10\x11\x12\x14\n\x10IOS_APP_STORE_ID\x10\x12\x42\xf3\x01\n!com.google.ads.googleads.v1.enumsB\x1e\x45\x64ucationPlaceholderFieldProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_EDUCATIONPLACEHOLDERFIELDENUM_EDUCATIONPLACEHOLDERFIELD = _descriptor.EnumDescriptor(
  name='EducationPlaceholderField',
  full_name='google.ads.googleads.v1.enums.EducationPlaceholderFieldEnum.EducationPlaceholderField',
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
      name='PROGRAM_ID', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_ID', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROGRAM_NAME', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AREA_OF_STUDY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROGRAM_DESCRIPTION', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCHOOL_NAME', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THUMBNAIL_IMAGE_URL', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALTERNATIVE_THUMBNAIL_IMAGE_URL', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINAL_URLS', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINAL_MOBILE_URLS', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRACKING_URL', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTEXTUAL_KEYWORDS', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANDROID_APP_LINK', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIMILAR_PROGRAM_IDS', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IOS_APP_LINK', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IOS_APP_STORE_ID', index=18, number=18,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=169,
  serialized_end=582,
)
_sym_db.RegisterEnumDescriptor(_EDUCATIONPLACEHOLDERFIELDENUM_EDUCATIONPLACEHOLDERFIELD)


_EDUCATIONPLACEHOLDERFIELDENUM = _descriptor.Descriptor(
  name='EducationPlaceholderFieldEnum',
  full_name='google.ads.googleads.v1.enums.EducationPlaceholderFieldEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EDUCATIONPLACEHOLDERFIELDENUM_EDUCATIONPLACEHOLDERFIELD,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=582,
)

_EDUCATIONPLACEHOLDERFIELDENUM_EDUCATIONPLACEHOLDERFIELD.containing_type = _EDUCATIONPLACEHOLDERFIELDENUM
DESCRIPTOR.message_types_by_name['EducationPlaceholderFieldEnum'] = _EDUCATIONPLACEHOLDERFIELDENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EducationPlaceholderFieldEnum = _reflection.GeneratedProtocolMessageType('EducationPlaceholderFieldEnum', (_message.Message,), dict(
  DESCRIPTOR = _EDUCATIONPLACEHOLDERFIELDENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.education_placeholder_field_pb2'
  ,
  __doc__ = """Values for Education placeholder fields. For more information about
  dynamic remarketing feeds, see
  https://support.google.com/google-ads/answer/6053288.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.EducationPlaceholderFieldEnum)
  ))
_sym_db.RegisterMessage(EducationPlaceholderFieldEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
