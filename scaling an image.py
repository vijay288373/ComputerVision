from PIL import Image

def scale_image(image_path, scale_factors):
    """
    Scales the image at image_path to multiple sizes defined by scale_factors.
    
    :param image_path: Path to the input image.
    :param scale_factors: List of floats indicating scale multipliers (e.g., 0.5, 2.0).
    :return: Dictionary mapping scale factor to resized Image objects.
    """
    original_image = Image.open(image_path)
    resized_images = {}

    for factor in scale_factors:
        new_width = int(original_image.width * factor)
        new_height = int(original_image.height * factor)
        resized = original_image.resize((new_width, new_height), Image.LANCZOS)
        resized_images[factor] = resized

    return resized_images

if __name__ == "__main__":
    image_path = r"C:/Users/vijay/Downloads/butterfly1.jpeg "
    scale_factors = [0.5, 1.5, 2.0]  # 50% smaller, 150% bigger, 200% bigger

    resized_images = scale_image(image_path, scale_factors)
    for factor, img in resized_images.items():
        print(f"Scaled image by factor {factor}: size {img.size}")
        img.show()
