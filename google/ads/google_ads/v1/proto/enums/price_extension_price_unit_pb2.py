# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/price_extension_price_unit.proto

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
  name='google/ads/googleads_v1/proto/enums/price_extension_price_unit.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\034PriceExtensionPriceUnitProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\nDgoogle/ads/googleads_v1/proto/enums/price_extension_price_unit.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\xac\x01\n\x1bPriceExtensionPriceUnitEnum\"\x8c\x01\n\x17PriceExtensionPriceUnit\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0c\n\x08PER_HOUR\x10\x02\x12\x0b\n\x07PER_DAY\x10\x03\x12\x0c\n\x08PER_WEEK\x10\x04\x12\r\n\tPER_MONTH\x10\x05\x12\x0c\n\x08PER_YEAR\x10\x06\x12\r\n\tPER_NIGHT\x10\x07\x42\xf1\x01\n!com.google.ads.googleads.v1.enumsB\x1cPriceExtensionPriceUnitProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_PRICEEXTENSIONPRICEUNITENUM_PRICEEXTENSIONPRICEUNIT = _descriptor.EnumDescriptor(
  name='PriceExtensionPriceUnit',
  full_name='google.ads.googleads.v1.enums.PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit',
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
      name='PER_HOUR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PER_DAY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PER_WEEK', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PER_MONTH', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PER_YEAR', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PER_NIGHT', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=166,
  serialized_end=306,
)
_sym_db.RegisterEnumDescriptor(_PRICEEXTENSIONPRICEUNITENUM_PRICEEXTENSIONPRICEUNIT)


_PRICEEXTENSIONPRICEUNITENUM = _descriptor.Descriptor(
  name='PriceExtensionPriceUnitEnum',
  full_name='google.ads.googleads.v1.enums.PriceExtensionPriceUnitEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PRICEEXTENSIONPRICEUNITENUM_PRICEEXTENSIONPRICEUNIT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=306,
)

_PRICEEXTENSIONPRICEUNITENUM_PRICEEXTENSIONPRICEUNIT.containing_type = _PRICEEXTENSIONPRICEUNITENUM
DESCRIPTOR.message_types_by_name['PriceExtensionPriceUnitEnum'] = _PRICEEXTENSIONPRICEUNITENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PriceExtensionPriceUnitEnum = _reflection.GeneratedProtocolMessageType('PriceExtensionPriceUnitEnum', (_message.Message,), dict(
  DESCRIPTOR = _PRICEEXTENSIONPRICEUNITENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.price_extension_price_unit_pb2'
  ,
  __doc__ = """Container for enum describing price extension price unit.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.PriceExtensionPriceUnitEnum)
  ))
_sym_db.RegisterMessage(PriceExtensionPriceUnitEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
