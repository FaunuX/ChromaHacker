import numpy as np

def convert_to_greyscale(image_array):
    if image_array.shape[-1] != 3:
        raise ValueError("Input image should have 3 channels (RGB).")

    r_coeff = 0.2989
    g_coeff = 0.5870
    b_coeff = 0.1140

    grayscale_image = np.rint(np.dot(image_array[...,:3], [r_coeff, g_coeff, b_coeff])).astype(np.uint8)
    return grayscale_image
