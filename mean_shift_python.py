
import math
import numpy as np
import sys

def _gaussian_kernel(distance, bandwidth):
    val = np.exp(-(distance**2 / bandwidth))
    return val

MIN_DISTANCE = 0.0000001
class MeanShift(object):
    def __init__(self, kernel = _gaussian_kernel):
        self.kernel = kernel

    def cluster(self, points, kernel_bandwidth):
        shift_points = np.array(points)
        max_min_dist = 1
        while max_min_dist > MIN_DISTANCE:
            print max_min_dist
            max_min_dist = 0
            for i in range(0, len(shift_points)):
                p_new = shift_points[i]
                p_new_start = p_new
                p_new = self._shift_point(p_new, points, kernel_bandwidth)
                dist = _euclidean_dist(p_new, p_new_start)
                if(dist > max_min_dist):
                    max_min_dist = dist
                shift_points[i] = p_new
        return MeanShiftResult(points, shift_points.tolist())

    def _shift_point(self, point, points, kernel_bandwidth):
        # from http://en.wikipedia.org/wiki/Mean-shift
        points = np.array(points)
        # numerator
        point_distances = np.sqrt(((point - points)**2).sum(axis=1))
        point_weights = self.kernel(point_distances, kernel_bandwidth)
        tiled_weights = np.tile(point_weights, [len(point), 1])
        # denominator
        denominator = sum(point_weights)
        shifted_point = np.multiply(tiled_weights.transpose(), points).sum(axis=0) / denominator
        return shifted_point

        # #  The above vectorized code is equivalent to the unrolled version below
        # shift_x = float(0)
        # shift_y = float(0)
        # scale_factor = float(0)
        # for p_temp in points:
        #     # numerator
        #     dist = _euclidean_dist(point, p_temp)
        #     weight = self.kernel(dist, kernel_bandwidth)
        #     shift_x += p_temp[0] * weight
        #     shift_y += p_temp[1] * weight
        #     # denominator
        #     scale_factor += weight
        # shift_x = shift_x / scale_factor
        # shift_y = shift_y / scale_factor
        # return [shift_x, shift_y]

def _euclidean_dist(pointA, pointB):
    if(len(pointA) != len(pointB)):
        raise Exception("expected point dimensionality to match")
    total = float(0)
    for dimension in range(0, len(pointA)):
        total += (pointA[dimension] - pointB[dimension])**2
    return math.sqrt(total)

class MeanShiftResult:
    def __init__(self, original_points, shifted_points):
        self.original_points = original_points
        self.shifted_points = shifted_points
