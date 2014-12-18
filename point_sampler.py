import numpy as np
import matplotlib.pyplot as plt


def run():
    cluster1 = sample2DGaussian(10, 10, 4, 1, 100)
    cluster2 = sample2DGaussian(0, 0, 2, 2, 100)
    clusters = [cluster1, cluster2]
    for c in clusters:
        plt.scatter(c[0], c[1])
    plt.show()

def sample2DGaussian(center_x, center_y, variance_x, variance_y, num_points):
    x_vals = sampleNormalData(center_x, variance_x, num_points)
    y_vals = sampleNormalData(center_y, variance_y, num_points)
    points = []
    for i in range(0, len(x_vals)):
        points.append((x_vals[i], y_vals[i]))
    return points

def sampleNormalData(mu, sigma, count):
    return np.random.normal(mu, sigma, count)

if __name__ == '__main__':
    run();