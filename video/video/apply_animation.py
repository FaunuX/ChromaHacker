from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns

from chromahacker.palettize import palettize
from chromahacker.process_image import load_image

plt.style.use('dark_background')

LOAD_IMAGE = load_image('https://picsum.photos/640/480?grayscale')
image = np.stack([LOAD_IMAGE] * 3, axis=2)

def convert_colors(color_tuple):
    return '#' + hex_value(hex(color_tuple[0])[2:]) + hex_value(hex(color_tuple[1])[2:]) + hex_value(hex(color_tuple[2])[2:])

def hex_value(val):
    if len(val) == 1:
        return '0' + val
    else:
        return val

def apply_animation(colors):
    colors_array = np.array(colors) / 255
    colors_x = colors_array[:, 0]
    colors_y = colors_array[:, 1]
    colors_z = colors_array[:, 2]

    spline = palettize("id_clut.png", *[convert_colors(i) for i in colors])

    fig = plt.figure()

    ax = plt.axes()

    def update_frame(i):
        ax.cla()  # Clear the previous frame
        c = np.rint(spline[0, i]).astype(np.uint8)
        shape = image.shape
        for j in range(shape[0]):
            for k in range(shape[1]):
                if np.all(image[j, k] == np.array([i, i, i])):
                    image[j, k] = c
        ax.imshow(image)

    anim = FuncAnimation(fig, update_frame, frames=256, repeat=False, interval=50)
    anim.save('apply_animation.mp4', writer = 'ffmpeg', fps = 60, dpi=300) 
