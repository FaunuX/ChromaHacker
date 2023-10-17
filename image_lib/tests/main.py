from chromahacker.palettize import palettize
import matplotlib.pyplot as plt
import numpy as np

def run():
    # with open('image.png', 'wb') as f:
    plt.imshow(np.rint(palettize('imag.jpg', 'black', '#16161e', '#1a1b26', '#7aa2f7', '#c0caf5')).astype(np.uint8))
    plt.show()
    # print(palettize("imag.jpg", colorscheme="nord"))

# run()
