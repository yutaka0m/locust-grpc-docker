# locust-grpc

```bash
docker-compose up --scale worker=4
```

## Additional Explanation
### Setup mock api

#### Generate proto code

```bash
python -m grpc_tools.protoc \
    -Iproto \
    --python_out=mock-api \
    --grpc_python_out=mock-api \
    proto/helloworld.proto
```

#### Run

```bash
cd mock-api
python main.py
```

#### Test

```bash
grpcurl -plaintext \
 -proto proto/helloworld.proto \
 -d '{"name":"yutaka"}' localhost:6565 \
 helloworld.Greeter/SayHello
```

### Setup locust

#### Generate proto code

```bash
python -m grpc_tools.protoc \
    -Iproto \
    --python_out=. \
    --grpc_python_out=. \
    proto/helloworld.proto
```
