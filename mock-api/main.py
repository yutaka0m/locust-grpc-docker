import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import logging
from concurrent import futures

logger = logging.getLogger("Stab API")
logging.basicConfig(level=logging.DEBUG)


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        message = f"Hello, {request.name}"
        return helloworld_pb2.HelloReply(message=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:6565')
    server.start()
    logger.info("Server started!")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
