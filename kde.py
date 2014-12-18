import numpy as np
import mean_shift_python as ms_tools

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def matrix(points, kernel_bandwidth, step_size, dimension_ranges):
    x_min = dimension_ranges[0]
    x_max = dimension_ranges[1]
    y_min = dimension_ranges[2]
    y_max = dimension_ranges[3]

    x = np.arange(x_min, x_max, step_size)
    y = np.arange(y_min, y_max, step_size)
    X, Y = np.meshgrid(x, y)
    zs = np.array([height([x,y], points, kernel_bandwidth) for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # plt.imshow(Z)
    ax.plot_surface(X, Y, Z)
    plt.show()
    # return Z

def height(point, points, kernel_bandwidth):
    height = 0;
    for pt in points:
        distance = ms_tools._euclidean_dist(point, pt)
        weight = ms_tools._kernel(distance, kernel_bandwidth)
        height += weight
    return height;
