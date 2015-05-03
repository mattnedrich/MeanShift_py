import sys
import math
import numpy as np
import mean_shift_utils as ms_utils

GROUP_DISTANCE_TOLERANCE = .1
class PointGrouper(object):
    
    def group_points(self, points):
        group_assignment = []
        groups = []
        group_index = 0
        index = 0
        for point in points:
            nearest_group_index = self._determine_nearest_group(point, groups)
            if nearest_group_index == None:
                # create new group
                groups.append([point])
                group_assignment.append(group_index)
                group_index += 1
            else:
                group_assignment.append(nearest_group_index)
                groups[nearest_group_index].append(point)
            index += 1
        return np.array(group_assignment)

    def _determine_nearest_group(self, point, groups):
        nearest_group_index = None
        index = 0
        for group in groups:
            distance_to_group = self._distance_to_group(point, group)
            if distance_to_group < GROUP_DISTANCE_TOLERANCE:
                nearest_group_index = index
            index += 1
        return nearest_group_index

    def _distance_to_group(self, point, group):
        min_distance = sys.float_info.max
        for pt in group:
            dist = ms_utils.euclidean_dist(point, pt)
            if dist < min_distance:
                min_distance = dist
        return min_distance

