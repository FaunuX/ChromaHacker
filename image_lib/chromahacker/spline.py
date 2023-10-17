import numpy as np

from chromahacker.color_input import input_color
from chromahacker.colorschemes import process_colorscheme
from chromahacker.process_image import load_image

def make_spline(*args, **kwargs):
    return Spline(*args, **kwargs).display

class Spline:
    def __init__(self, url, *args, colorscheme=None, accurate=False):
        self.accurate = accurate
        self.args = np.array([input_color(arg) for arg in args])
        if colorscheme != None:
            input_args = process_colorscheme(colorscheme)
        else:
            input_args = args
        self.args = np.array([input_color(arg) for arg in input_args])
        self.num_points = len(self.args)
        self.img = load_image(url)

        if accurate:
            display = np.array([[self.spline(j) for j in i] for i in self.img])
        else:
            display = np.rint(self.spline(self.img)).astype(np.uint8)
        self.display = display

    def spline(self, n):
        if self.accurate:
            t = np.median(n)
        else:
            t = np.median(n, axis=2)
        c = ((t + 1) / 256) * (self.num_points - 1)
        i = np.rint(np.floor(c)).astype(int)

        p0 = self.args[(i - 1) % self.num_points]
        p1 = self.args[i                        ]
        p2 = self.args[(i + 1) % self.num_points]
        p3 = self.args[(i + 2) % self.num_points]

        t = c - i
        if not self.accurate:
            t = np.stack((t, t, t), axis=2)

        return 0.5 * (
            (-t**3 + 2*t**2 - t) * p0 +
            (3*t**3 - 5*t**2 + 2) * p1 +
            (-3*t**3 + 4*t**2 + t) * p2 +
            (t**3 - t**2) * p3
        )
