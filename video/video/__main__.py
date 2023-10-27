import time

from apply_animation import apply_animation
from make_spline_animation_1 import make_spline_animation_1
from make_spline_animation_2 import make_spline_animation_2

t = time.time()
colors = [(26, 27, 38), (61, 81, 124), (192, 202, 245)]
apply_animation(colors)
print(time.time() - t)
# make_spline_animation_1(colors)
# make_spline_animation_2(colors)
