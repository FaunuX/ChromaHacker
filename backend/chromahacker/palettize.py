from chromahacker.spline import make_spline
from chromahacker.process_image import load_image
from chromahacker.apply import apply_clut_to_image

def palettize(url, *args, **kwargs):
    clut_array = make_spline("id_clut.png", *args, **kwargs, accurate=True)
    image_array = load_image(url)

    image_with_clut_array = apply_clut_to_image(image_array, clut_array)
    return image_with_clut_array
