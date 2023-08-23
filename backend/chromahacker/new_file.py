from PIL import Image
import io
import numpy as np
import time
import cv2

from chromahacker.palettize import palettize
from chromahacker.process_image import load_image
from chromahacker.apply import apply_clut_to_image

def do():
    clut_array = palettize("id_clut.png", "png", colorscheme='tokyonight_night', accurate=True)
    image_array = load_image("imag.jpg")

    image_with_clut_array = apply_clut_to_image(image_array, clut_array)

    img_encode = cv2.imencode('.png', image_with_clut_array)[1]

    data_encode = np.array(img_encode)
    byte_encode = data_encode.tobytes()
    with open('okthen.png', 'wb') as f:
        f.write(byte_encode)
