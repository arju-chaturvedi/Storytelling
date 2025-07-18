import random

def generate_image_for_text(text):
    placeholder_images = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Example.jpg/800px-Example.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Washington_Capitol.jpg/800px-Washington_Capitol.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Test_image.jpg/800px-Test_image.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Sunflower_from_Silesia2.jpg/800px-Sunflower_from_Silesia2.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/640px-PNG_transparency_demonstration_1.png"
    ]
    return random.choice(placeholder_images)

