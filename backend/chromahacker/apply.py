from chromahacker.greyscale import convert_to_greyscale

def apply_clut_to_image(image_array, clut_array):
    image_array = convert_to_greyscale(image_array)

    image_with_clut_array = clut_array[0, image_array[:, :]]

    return image_with_clut_array
