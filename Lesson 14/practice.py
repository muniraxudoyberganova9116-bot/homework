import numpy as np

tiny_image = np.array([
    [[255, 0, 0], [0, 255, 0]],     # row 0: red pixel, green pixel
    [[0, 0, 255], [255, 255, 255]]  # row 1: blue pixel, white pixel
])

print(tiny_image.shape)