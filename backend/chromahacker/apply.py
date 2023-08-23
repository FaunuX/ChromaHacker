from PIL import Image
import io
import numpy as np
import time
import cv2
from chromahacker.palettize import palettize
from chromahacker.process_image import load_image
from chromahacker.greyscale import convert_to_greyscale

def apply_clut_to_image(image_array, clut_array):
    image_array = convert_to_greyscale(image_array)

    # Apply the CLUT using NumPy indexing and broadcasting
    image_with_clut_array = clut_array[0, image_array[:, :]]

    image_with_clut = Image.fromarray(image_with_clut_array.astype(np.uint8))

    return image_with_clut_array

if __name__ == '__main__':
    """
    disregard
    """
    clut_array = palettize("id_clut.png", "png", colorscheme='tokyonight_night', accurate=True)
    image_array = load_image("imag.jpg")

    image_with_clut_array = apply_clut_to_image(image_array, clut_array)

    img_encode = cv2.imencode('.png', image_with_clut_array)[1]

    data_encode = np.array(img_encode)
    byte_encode = data_encode.tobytes()
    with open('okthen.png', 'wb') as f:
        f.write(byte_encode)
