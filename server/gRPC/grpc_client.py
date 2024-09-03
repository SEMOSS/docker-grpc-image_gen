# This file is for testing purposes.
# This file sets up a gRPC client to connect to the gRPC server.
import grpc
import image_gen_pb2
import image_gen_pb2_grpc
from google.protobuf import wrappers_pb2


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = image_gen_pb2_grpc.ImageGenServiceStub(channel)

    request = image_gen_pb2.ImageGenRequest(
        prompt="Canada",
        consistency_decoder=wrappers_pb2.BoolValue(value=True),
        negative_prompt=wrappers_pb2.StringValue(value=""),
        guidance_scale=wrappers_pb2.FloatValue(value=7.5),
        num_inference_steps=wrappers_pb2.Int32Value(value=50),
        height=wrappers_pb2.Int32Value(value=1000),
        width=wrappers_pb2.Int32Value(value=1000),
        seed=wrappers_pb2.Int32Value(value=0),
    )

    response = stub.GenerateImage(request)
    print(response)


if __name__ == "__main__":
    run()
