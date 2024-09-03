from server.gaas.image_gen import ImageGen


def generate_image():
    """_summary_
    Generate an image using the ImageGen class.
    """
    image_gen = ImageGen()

    url = image_gen.generate_image(
        prompt="A beautiful sunset over the ocean",
    )

    print(url)


if __name__ == "__main__":
    generate_image()
