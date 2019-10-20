# Wrap a neural network model with Flask
# what you will do?
# - get an image as an input
# - run a neural network on it
# - return the results
# - wrap the app with docker with all relevant environment variables
#   the production start script should be named "serve"
# - except a /predict API call, add also /health API
# - eventually we want to call `docker run -p 8080:8080 image_name serve` and it will run the server

# things to take into consideration:
# logging
# virtualenv
# project folder structure
# use python3.6

from pathlib import Path

import click
import numpy as np
from keras.applications import ResNet50, imagenet_utils
from keras.preprocessing.image import img_to_array
from PIL import Image


def prepare_image(image, target=(224, 224)):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image


@click.command()
@click.argument('image_path', type=Path)
def main(image_path):
    image = Image.open(image_path)
    image = prepare_image(image)

    model = ResNet50(weights="imagenet")
    preds = model.predict(image)

    results = imagenet_utils.decode_predictions(preds)
    print(results)


if __name__ == "__main__":
    main()
