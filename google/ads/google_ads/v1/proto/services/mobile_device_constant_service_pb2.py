# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/services/mobile_device_constant_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.resources import mobile_device_constant_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_mobile__device__constant__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/services/mobile_device_constant_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v1.servicesB MobileDeviceConstantServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services'),
  serialized_pb=_b('\nKgoogle/ads/googleads_v1/proto/services/mobile_device_constant_service.proto\x12 google.ads.googleads.v1.services\x1a\x44google/ads/googleads_v1/proto/resources/mobile_device_constant.proto\x1a\x1cgoogle/api/annotations.proto\"7\n\x1eGetMobileDeviceConstantRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xe9\x01\n\x1bMobileDeviceConstantService\x12\xc9\x01\n\x17GetMobileDeviceConstant\x12@.google.ads.googleads.v1.services.GetMobileDeviceConstantRequest\x1a\x37.google.ads.googleads.v1.resources.MobileDeviceConstant\"3\x82\xd3\xe4\x93\x02-\x12+/v1/{resource_name=mobileDeviceConstants/*}B\x87\x02\n$com.google.ads.googleads.v1.servicesB MobileDeviceConstantServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_mobile__device__constant__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETMOBILEDEVICECONSTANTREQUEST = _descriptor.Descriptor(
  name='GetMobileDeviceConstantRequest',
  full_name='google.ads.googleads.v1.services.GetMobileDeviceConstantRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetMobileDeviceConstantRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=213,
  serialized_end=268,
)

DESCRIPTOR.message_types_by_name['GetMobileDeviceConstantRequest'] = _GETMOBILEDEVICECONSTANTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetMobileDeviceConstantRequest = _reflection.GeneratedProtocolMessageType('GetMobileDeviceConstantRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETMOBILEDEVICECONSTANTREQUEST,
  __module__ = 'google.ads.googleads_v1.proto.services.mobile_device_constant_service_pb2'
  ,
  __doc__ = """Request message for
  [MobileDeviceConstantService.GetMobileDeviceConstant][google.ads.googleads.v1.services.MobileDeviceConstantService.GetMobileDeviceConstant].
  
  
  Attributes:
      resource_name:
          Resource name of the mobile device to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetMobileDeviceConstantRequest)
  ))
_sym_db.RegisterMessage(GetMobileDeviceConstantRequest)


DESCRIPTOR._options = None

_MOBILEDEVICECONSTANTSERVICE = _descriptor.ServiceDescriptor(
  name='MobileDeviceConstantService',
  full_name='google.ads.googleads.v1.services.MobileDeviceConstantService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=271,
  serialized_end=504,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMobileDeviceConstant',
    full_name='google.ads.googleads.v1.services.MobileDeviceConstantService.GetMobileDeviceConstant',
    index=0,
    containing_service=None,
    input_type=_GETMOBILEDEVICECONSTANTREQUEST,
    output_type=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_mobile__device__constant__pb2._MOBILEDEVICECONSTANT,
    serialized_options=_b('\202\323\344\223\002-\022+/v1/{resource_name=mobileDeviceConstants/*}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MOBILEDEVICECONSTANTSERVICE)

DESCRIPTOR.services_by_name['MobileDeviceConstantService'] = _MOBILEDEVICECONSTANTSERVICE

# @@protoc_insertion_point(module_scope)
