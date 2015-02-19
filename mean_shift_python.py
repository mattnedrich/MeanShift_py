
import math
import matplotlib.pyplot as plt
import point_sampler as point_sampler
import sys
import copy
import os

def MeanShiftFactory(shift_each_point_standalone = True):
    if shift_each_point_standalone:
        return MeanShiftStandAlone()
    else:
        return MeanShiftBatch()

class MeanShift(object):
    def __init__(self):
        pass

    def cluster(self, original_points, kernel_bandwidth):
        pass # abstract method

    def _shift_point(self, p, points, kernel_bandwidth):
        # from http://en.wikipedia.org/wiki/Mean-shift
        shift_x = float(0)
        shift_y = float(0)
        scale_factor = float(0)

        for p_temp in points:
            # numerator computation
            dist = _euclidean_dist(p, p_temp)
            weight = _kernel(dist, kernel_bandwidth)
            shift_x += p_temp[0] * weight
            shift_y += p_temp[1] * weight
            # denominator computation
            scale_factor += weight

        shift_x = shift_x / scale_factor
        shift_y = shift_y / scale_factor
        return [shift_x, shift_y]

class MeanShiftStandAlone(MeanShift):
    def cluster(self, original_points, kernel_bandwidth):
        points = copy.deepcopy(original_points)
        min_dist = 0.000001
        for i in range(0, len(points)):
            dist = sys.float_info.max
            p_new = points[i]

            while(dist > min_dist):
                print "%f" % dist
                p_new_start = p_new
                p_new = self._shift_point(p_new, original_points, kernel_bandwidth)
                dist = _euclidean_dist(p_new, p_new_start)
            points[i] = p_new

# save_path = "/Users/matt/repo_nonwork/mean_shift/python/images"
class MeanShiftBatch(MeanShift):
    def cluster(self, original_points, kernel_bandwidth):
        figure_number = 0
        points = copy.deepcopy(original_points)
        min_dist = 0.000001
        max_min_dist = 1
        while max_min_dist > min_dist:
            # print "%f" % min_dist
            max_min_dist = 0
            for i in range(0, len(points)):
                p_new = points[i]
                p_new_start = p_new
                p_new = self._shift_point(p_new, original_points, kernel_bandwidth)
                dist = _euclidean_dist(p_new, p_new_start)
                if(dist > max_min_dist):
                    max_min_dist = dist
                points[i] = p_new

        return MeanShiftResult(original_points, points)
        # # plotting code
        # for pt in points:
        #     plt.scatter(pt[0], pt[1])
        # plt.axis([5, 15, 5, 15])
        # filename = "img_%08d.png" % figure_number
        # full_path = os.path.join(save_path, filename)
        # plt.savefig(full_path)
        # figure_number += 1
        # plt.clf()

class MeanShiftResult:
    def __init__(self, original_points, shifted_points):
        self.original_points = original_points
        self.shifted_points = shifted_points



def _kernel(distance, bandwidth):
    # Gaussian kernel
    val = math.exp(-distance / bandwidth)**2
    return val

def _euclidean_dist(pointA, pointB):
    if(len(pointA) != len(pointB)):
        raise Exception("expected point dimensionality to match")
    total = float(0)
    for dimension in range(0, len(pointA)):
        total += (pointA[dimension] - pointB[dimension])**2
    return math.sqrt(total)

