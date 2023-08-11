# import numpy as np

# from chromahacker.color_input import input_color

# def spline_from(*args, accurate=False):
#     args = np.array([ input_color(arg) for arg in args ])
#     def return_value(t):
#         c = (( t + 1 ) / 256) * (len(args) - 1)
#         b0 = args[np.floor(c).astype('int')]
#         b1 = args[np.ceil(c).astype('int')]
#         d = c - np.floor(c)
#         if not accurate:
#             d.shape += (1,)
#         return d * (b1 - b0) + b0
#     return return_value
import numpy as np

from chromahacker.color_input import input_color

def spline_from(*args, accurate=False):
    args = np.array([input_color(arg) for arg in args])
    num_points = len(args)

    def return_value(t):
        c = ((t + 1) / 256) * (num_points - 1)
        i = int(np.floor(c))

        p0 = args[(i - 1) % num_points]
        p1 = args[i]
        p2 = args[(i + 1) % num_points]
        p3 = args[(i + 2) % num_points]

        t = c - i

        return 0.5 * (
                (-t**3 + 2*t**2 - t) * p0 +
                (3*t**3 - 5*t**2 + 2) * p1 +
                (-3*t**3 + 4*t**2 + t) * p2 +
                (t**3 - t**2) * p3
                )

    return return_value
