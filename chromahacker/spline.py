import numpy as np

from chromahacker.color_input import input_color

def spline_from(*args):
    args = np.array([ input_color(arg) for arg in args ])
    def return_value(t):
        c = (( t + 1 ) / 256) * (len(args) - 1)
        b0 = args[np.floor(c).astype('int')]
        b1 = args[np.ceil(c).astype('int')]
        d = c - np.floor(c)
        d.shape += (1,)
        return d * (b1 - b0) + b0
    return return_value
