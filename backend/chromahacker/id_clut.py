from PIL import Image

def generate_identity_clut(size=256):
    """
Generate an identity halftone color lookup table (CLUT).

Args:
size (int): The size of the CLUT. Default is 256.

Returns:
Image: The identity CLUT as a Pillow Image object.
"""
    clut_data = [(i, i, i) for i in range(size)]
    clut_image = Image.new("RGB", (size, 1))
    clut_image.putdata(clut_data)
    return clut_image

def save_identity_clut_as_png(clut_image, filename="id_clut.png"):
    """
    Save the identity CLUT as a PNG image.

    Args:
    clut_image (Image): The CLUT image to save.
    filename (str): The filename for the saved image. Default is "id_clut.png".
    """
    clut_image.save(filename)

def run():
    # Generate the identity CLUT
    identity_clut = generate_identity_clut()

    # Save the identity CLUT as PNG
    save_identity_clut_as_png(identity_clut)
