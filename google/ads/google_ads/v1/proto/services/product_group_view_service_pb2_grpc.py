# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v1.proto.resources import product_group_view_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_product__group__view__pb2
from google.ads.google_ads.v1.proto.services import product_group_view_service_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_product__group__view__service__pb2


class ProductGroupViewServiceStub(object):
  """Service to manage product group views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetProductGroupView = channel.unary_unary(
        '/google.ads.googleads.v1.services.ProductGroupViewService/GetProductGroupView',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_product__group__view__service__pb2.GetProductGroupViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_product__group__view__pb2.ProductGroupView.FromString,
        )


class ProductGroupViewServiceServicer(object):
  """Service to manage product group views.
  """

  def GetProductGroupView(self, request, context):
    """Returns the requested product group view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProductGroupViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetProductGroupView': grpc.unary_unary_rpc_method_handler(
          servicer.GetProductGroupView,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_product__group__view__service__pb2.GetProductGroupViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_product__group__view__pb2.ProductGroupView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.ProductGroupViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
