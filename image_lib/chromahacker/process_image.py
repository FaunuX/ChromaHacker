import numpy as np
from PIL import Image
from io import BytesIO

def load_image(source):
    if source.startswith("http"):
        response = requests.get(source)
        image = Image.open(BytesIO(response.content))
    else:
        image = Image.open(source)

    image_array = np.array(image)
    return image_array
