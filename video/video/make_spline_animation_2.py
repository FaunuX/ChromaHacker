from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns

from chromahacker.palettize import palettize

plt.style.use('dark_background')

def convert_colors(color_tuple):
    return '#' + hex_value(hex(color_tuple[0])[2:]) + hex_value(hex(color_tuple[1])[2:]) + hex_value(hex(color_tuple[2])[2:])

def hex_value(val):
    if len(val) == 1:
        return '0' + val
    else:
        return val

def make_spline_animation_2(colors):
    colors_array = np.array(colors) / 255
    colors_x = colors_array[:, 0]
    colors_y = colors_array[:, 1]
    colors_z = colors_array[:, 2]

    spline = palettize("id_clut.png", *[convert_colors(i) for i in colors])

    fig = plt.figure()

    ax = plt.axes()

    cs = []

    def update_frame(i):
        ax.cla()  # Clear the previous frame
        progress = i / 255
        c = np.rint(spline[0, np.rint(progress * 255).astype(np.uint8)]).astype(np.uint8)
        cs.append(c)
        blackspace = np.zeros((256 - i, 3)).astype(np.uint8)
        ax.imshow(np.stack([np.concatenate((np.array(cs), blackspace))]*64, axis=0).reshape(64, -1, 3))

    anim = FuncAnimation(fig, update_frame, frames=256, repeat=False, interval=50)
    anim.save('make_spline_animation_2.mp4', writer = 'ffmpeg', fps = 60, dpi=300) 
