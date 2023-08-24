from PIL import Image

def generate_identity_clut(size=256):
    clut_data = [(i, i, i) for i in range(size)]
    clut_image = Image.new("RGB", (size, 1))
    clut_image.putdata(clut_data)
    return clut_image

def save_identity_clut_as_png(clut_image, filename="id_clut.png"):
    clut_image.save(filename)

def run():
    # Generate the identity CLUT
    identity_clut = generate_identity_clut()

    # Save the identity CLUT as PNG
    save_identity_clut_as_png(identity_clut)
