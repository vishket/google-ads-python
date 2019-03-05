# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/resources/domain_category.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/resources/domain_category.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v1.resourcesB\023DomainCategoryProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources'),
  serialized_pb=_b('\n=google/ads/googleads_v1/proto/resources/domain_category.proto\x12!google.ads.googleads.v1.resources\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xca\x03\n\x0e\x44omainCategory\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12.\n\x08\x63\x61mpaign\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x63\x61tegory\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rlanguage_code\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06\x64omain\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11\x63overage_fraction\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x32\n\rcategory_rank\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x30\n\x0chas_children\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x1arecommended_cpc_bid_micros\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x80\x02\n%com.google.ads.googleads.v1.resourcesB\x13\x44omainCategoryProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_DOMAINCATEGORY = _descriptor.Descriptor(
  name='DomainCategory',
  full_name='google.ads.googleads.v1.resources.DomainCategory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.DomainCategory.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v1.resources.DomainCategory.campaign', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='google.ads.googleads.v1.resources.DomainCategory.category', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.ads.googleads.v1.resources.DomainCategory.language_code', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='google.ads.googleads.v1.resources.DomainCategory.domain', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coverage_fraction', full_name='google.ads.googleads.v1.resources.DomainCategory.coverage_fraction', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category_rank', full_name='google.ads.googleads.v1.resources.DomainCategory.category_rank', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_children', full_name='google.ads.googleads.v1.resources.DomainCategory.has_children', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recommended_cpc_bid_micros', full_name='google.ads.googleads.v1.resources.DomainCategory.recommended_cpc_bid_micros', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=163,
  serialized_end=621,
)

_DOMAINCATEGORY.fields_by_name['campaign'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_DOMAINCATEGORY.fields_by_name['category'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_DOMAINCATEGORY.fields_by_name['language_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_DOMAINCATEGORY.fields_by_name['domain'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_DOMAINCATEGORY.fields_by_name['coverage_fraction'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_DOMAINCATEGORY.fields_by_name['category_rank'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_DOMAINCATEGORY.fields_by_name['has_children'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_DOMAINCATEGORY.fields_by_name['recommended_cpc_bid_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['DomainCategory'] = _DOMAINCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DomainCategory = _reflection.GeneratedProtocolMessageType('DomainCategory', (_message.Message,), dict(
  DESCRIPTOR = _DOMAINCATEGORY,
  __module__ = 'google.ads.googleads_v1.proto.resources.domain_category_pb2'
  ,
  __doc__ = """A category generated automatically by crawling a domain. If a campaign
  uses the DynamicSearchAdsSetting, then domain categories will be
  generated for the domain. The categories can be targeted using
  WebpageConditionInfo. See:
  https://support.google.com/google-ads/answer/2471185
  
  
  Attributes:
      resource_name:
          The resource name of the domain category. Domain category
          resource names have the form:  ``customers/{customer_id}/domai
          nCategories/{campaign_id}~{category_base64}~{language_code}``
      campaign:
          The campaign this category is recommended for.
      category:
          Recommended category for the website domain. e.g. if you have
          a website about electronics, the categories could be
          "cameras", "televisions", etc.
      language_code:
          The language code specifying the language of the website. e.g.
          "en" for English. The language can be specified in the
          DynamicSearchAdsSetting required for dynamic search ads. This
          is the language of the pages from your website that you want
          Google Ads to find, create ads for, and match searches with.
      domain:
          The domain for the website. The domain can be specified in the
          DynamicSearchAdsSetting required for dynamic search ads.
      coverage_fraction:
          Fraction of pages on your site that this category matches.
      category_rank:
          The position of this category in the set of categories. Lower
          numbers indicate a better match for the domain. null indicates
          not recommended.
      has_children:
          Indicates whether this category has sub-categories.
      recommended_cpc_bid_micros:
          The recommended cost per click for the category.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.DomainCategory)
  ))
_sym_db.RegisterMessage(DomainCategory)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
