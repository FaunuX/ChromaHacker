import requests
import numpy as np
from PIL import Image
from io import BytesIO

# Send GET request
def url_to_image(url):
    response = requests.get(url)

    image = Image.open(BytesIO(response.content))

    image_array = np.array(image)

    return image_array
