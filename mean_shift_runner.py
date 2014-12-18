import mean_shift_python as ms
import point_sampler    
import kde

def run():
    # get all points
    c1 = point_sampler.sample2DGaussian(
        center_x = 10, 
        center_y = 10, 
        variance_x = 1.4, 
        variance_y = 1, 
        num_points = 40)

    c2 = point_sampler.sample2DGaussian(
        center_x = 15, 
        center_y = 12, 
        variance_x = 1, 
        variance_y = 2, 
        num_points = 20)

    c3 = point_sampler.sample2DGaussian(
        center_x = 8, 
        center_y = 8, 
        variance_x = 2, 
        variance_y = 0.5, 
        num_points = 10)

    reference_points = c1 + c2 + c3
    mean_shifter = ms.MeanShiftFactory(False)
    mean_shift_result = mean_shifter.cluster(reference_points, kernel_bandwidth = 1.5)
    
    for i in range(len(mean_shift_result.shifted_points)):
        original_point = mean_shift_result.original_points[i]
        converged_point = mean_shift_result.shifted_points[i]
        print "(%5.2f, %5.2f)\t->\t(%5.2f, %5.2f)" % (original_point[0], original_point[1], converged_point[0], converged_point[1])

    # Z = kde.matrix(reference_points, 4, .1, [0, 20, 0, 20])    
    # for pt in reference_points:
    #     plt.scatter(pt[0], pt[1])
    # plt.scatter(points[0][0], points[0][1], s=200, c="red")
    # plt.show()


if __name__ == '__main__':
    run()