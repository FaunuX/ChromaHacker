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

colors = [(26, 27, 38), (61, 81, 124), (192, 202, 245)]
def make_spline_animation_1(colors):
    colors_array = np.array(colors) / 255
    colors_x = colors_array[:, 0]
    colors_y = colors_array[:, 1]
    colors_z = colors_array[:, 2]

    spline = palettize("id_clut.png", *[convert_colors(i) for i in colors])

    fig = plt.figure()

    ax = plt.axes(projection='3d')

    xs = []
    ys = []
    zs = []
    cs = []

    def update_frame(i):
        ax.cla()  # Clear the previous frame
        progress = i / 255
        c = spline[0, np.rint(progress * 255).astype(np.uint8)] / 255
        x = c[0]
        y = c[1]
        z = c[2]
        xs.append(x)
        ys.append(y)
        zs.append(z)
        cs.append(c)

        ax.scatter(colors_x, colors_y, colors_z, s=250, c=colors_array, alpha=0.5)
        ax.scatter(xs, ys, zs, c=cs, s=25)


    anim = FuncAnimation(fig, update_frame, frames=256, repeat=False, interval=50)
    anim.save('make_spline_animation_1.mp4', writer = 'ffmpeg', fps = 60, dpi=300) 
