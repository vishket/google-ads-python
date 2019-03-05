# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v1.proto.resources import mutate_job_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_mutate__job__pb2
from google.ads.google_ads.v1.proto.services import mutate_job_service_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2


class MutateJobServiceStub(object):
  """Service to manage mutate jobs.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateMutateJob = channel.unary_unary(
        '/google.ads.googleads.v1.services.MutateJobService/CreateMutateJob',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.CreateMutateJobRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.CreateMutateJobResponse.FromString,
        )
    self.GetMutateJob = channel.unary_unary(
        '/google.ads.googleads.v1.services.MutateJobService/GetMutateJob',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.GetMutateJobRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_mutate__job__pb2.MutateJob.FromString,
        )
    self.ListMutateJobResults = channel.unary_unary(
        '/google.ads.googleads.v1.services.MutateJobService/ListMutateJobResults',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.ListMutateJobResultsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.ListMutateJobResultsResponse.FromString,
        )
    self.RunMutateJob = channel.unary_unary(
        '/google.ads.googleads.v1.services.MutateJobService/RunMutateJob',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.RunMutateJobRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.AddMutateJobOperations = channel.unary_unary(
        '/google.ads.googleads.v1.services.MutateJobService/AddMutateJobOperations',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.AddMutateJobOperationsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.AddMutateJobOperationsResponse.FromString,
        )


class MutateJobServiceServicer(object):
  """Service to manage mutate jobs.
  """

  def CreateMutateJob(self, request, context):
    """Creates a mutate job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMutateJob(self, request, context):
    """Returns the mutate job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListMutateJobResults(self, request, context):
    """Returns the results of the mutate job. The job must be done.
    Supports standard list paging.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RunMutateJob(self, request, context):
    """Runs the mutate job.

    The Operation.metadata field type is MutateJobMetadata. When finished, the
    long running operation will not contain errors or a response. Instead, use
    ListMutateJobResults to get the results of the job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddMutateJobOperations(self, request, context):
    """Add operations to the mutate job.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MutateJobServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateMutateJob': grpc.unary_unary_rpc_method_handler(
          servicer.CreateMutateJob,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.CreateMutateJobRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.CreateMutateJobResponse.SerializeToString,
      ),
      'GetMutateJob': grpc.unary_unary_rpc_method_handler(
          servicer.GetMutateJob,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.GetMutateJobRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_mutate__job__pb2.MutateJob.SerializeToString,
      ),
      'ListMutateJobResults': grpc.unary_unary_rpc_method_handler(
          servicer.ListMutateJobResults,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.ListMutateJobResultsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.ListMutateJobResultsResponse.SerializeToString,
      ),
      'RunMutateJob': grpc.unary_unary_rpc_method_handler(
          servicer.RunMutateJob,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.RunMutateJobRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'AddMutateJobOperations': grpc.unary_unary_rpc_method_handler(
          servicer.AddMutateJobOperations,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.AddMutateJobOperationsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_mutate__job__service__pb2.AddMutateJobOperationsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.MutateJobService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
