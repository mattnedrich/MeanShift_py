import mean_shift_python as ms
import matplotlib.pyplot as plt
from numpy import genfromtxt

def load_points(filename):
    data = genfromtxt(filename, delimiter=',')
    return data

def run():
    reference_points = load_points("data.csv")
    mean_shifter = ms.MeanShift()
    mean_shift_result = mean_shifter.cluster(reference_points, kernel_bandwidth = 3)
    
    for i in range(len(mean_shift_result.shifted_points)):
        original_point = mean_shift_result.original_points[i]
        converged_point = mean_shift_result.shifted_points[i]
        print "(%5.2f, %5.2f)\t->\t(%5.2f, %5.2f)" % (original_point[0], original_point[1], converged_point[0], converged_point[1])
    
    # plot_reference_points(reference_points)
    # for pt in mean_shift_result.shifted_points:
    #     plt.scatter(pt[0], pt[1], c="black")
    

# def plot_reference_points(reference_points):
#     for pt in reference_points:
#         plt.scatter(pt[0], pt[1], c="red", zorder=2)
    

if __name__ == '__main__':
    run()