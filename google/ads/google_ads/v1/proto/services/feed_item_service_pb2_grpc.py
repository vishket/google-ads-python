# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v1.proto.resources import feed_item_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_feed__item__pb2
from google.ads.google_ads.v1.proto.services import feed_item_service_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_feed__item__service__pb2


class FeedItemServiceStub(object):
  """Service to manage feed items.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFeedItem = channel.unary_unary(
        '/google.ads.googleads.v1.services.FeedItemService/GetFeedItem',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_feed__item__service__pb2.GetFeedItemRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_feed__item__pb2.FeedItem.FromString,
        )
    self.MutateFeedItems = channel.unary_unary(
        '/google.ads.googleads.v1.services.FeedItemService/MutateFeedItems',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_feed__item__service__pb2.MutateFeedItemsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_feed__item__service__pb2.MutateFeedItemsResponse.FromString,
        )


class FeedItemServiceServicer(object):
  """Service to manage feed items.
  """

  def GetFeedItem(self, request, context):
    """Returns the requested feed item in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateFeedItems(self, request, context):
    """Creates, updates, or removes feed items. Operation statuses are
    returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FeedItemServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFeedItem': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeedItem,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_feed__item__service__pb2.GetFeedItemRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_feed__item__pb2.FeedItem.SerializeToString,
      ),
      'MutateFeedItems': grpc.unary_unary_rpc_method_handler(
          servicer.MutateFeedItems,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_feed__item__service__pb2.MutateFeedItemsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_feed__item__service__pb2.MutateFeedItemsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.FeedItemService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
