import time

from locust import task
import helloworld_pb2

import helloworld_pb2_grpc
from grpc_client import GrpcUser


class HelloGrpcUser(GrpcUser):
    host = "mock-api:6565"
    stub_class = helloworld_pb2_grpc.GreeterStub

    @task
    def say_hello(self):
        if not self._channel_closed:
            self.client.SayHello(helloworld_pb2.HelloRequest(name="Test"))
        time.sleep(1)
