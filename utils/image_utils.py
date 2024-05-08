# utils/image_utils.py

import os


def load_images(folder_path):
    image_extensions = [".jpg", ".jpeg", ".png"]
    images = []

    for filename in os.listdir(folder_path):
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            image_path = os.path.join(folder_path, filename)
            images.append(image_path)

    return images
