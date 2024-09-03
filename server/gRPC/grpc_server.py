import grpc
from concurrent import futures
import image_gen_pb2
import image_gen_pb2_grpc
from gaas.image_gen import ImageGen


class ImageGenServiceServicer(image_gen_pb2_grpc.ImageGenServiceServicer):

    def GenerateImage(self, request, context):
        print("GenerateImage called")
        image_gen = ImageGen()

        try:
            prompt = request.prompt

            consistency_decoder = (
                request.consistency_decoder.value
                if request.HasField("consistency_decoder")
                else False
            )

            negative_prompt = (
                request.negative_prompt.value
                if request.HasField("negative_prompt")
                else ""
            )

            guidance_scale = (
                request.guidance_scale.value
                if request.HasField("guidance_scale")
                else 7.5
            )

            num_inference_steps = (
                request.num_inference_steps.value
                if request.HasField("num_inference_steps")
                else 50
            )

            height = request.height.value if request.HasField("height") else 512

            width = request.width.value if request.HasField("width") else 512

            seed = request.seed.value if request.HasField("seed") else None

        except Exception as e:
            print(f"Error processing request: {e}")
            context.set_details(f"Error processing request: {e}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return image_gen_pb2.ImageGenResponse()

        response_data = image_gen.generate_image(
            prompt,
            consistency_decoder,
            negative_prompt,
            guidance_scale,
            num_inference_steps,
            height,
            width,
            seed,
        )
        print("GenerateImage completed")
        return image_gen_pb2.ImageGenResponse(**response_data)

    def HealthCheck(self, request, context):
        return image_gen_pb2.HealthCheckResponse(status="Healthy")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_gen_pb2_grpc.add_ImageGenServiceServicer_to_server(
        ImageGenServiceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
