import os
import io

import cv2
import numpy as np

from chromahacker.spline import spline_from # hey this line is a palindrome
from chromahacker.process_image import url_to_image

def palettize(url, output, *args, accurate=False):
    img = url_to_image(url)
    
    try:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    except:
        pass

    fn = spline_from(*args, accurate=accurate)

    if accurate:
        display = np.array([[fn(j) for j in i] for i in img])
    else:
        display = np.rint(fn(img)).astype(np.uint8)

    img_encode = cv2.imencode('.' + output, display)[1]

    data_encode = np.array(img_encode)
    byte_encode = data_encode.tobytes()
    return byte_encode
