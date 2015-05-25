import mean_shift as ms
from numpy import genfromtxt

def load_points(filename):
    data = genfromtxt(filename, delimiter=',')
    return data

def run():
    reference_points = load_points("data.csv")
    mean_shifter = ms.MeanShift()
    mean_shift_result = mean_shifter.cluster(reference_points, kernel_bandwidth = 3)
    
    print "Original Point     Shifted Point  Cluster ID"
    print "============================================"
    for i in range(len(mean_shift_result.shifted_points)):
        original_point = mean_shift_result.original_points[i]
        converged_point = mean_shift_result.shifted_points[i]
        cluster_assignment = mean_shift_result.cluster_ids[i]
        print "(%5.2f,%5.2f)  ->  (%5.2f,%5.2f)  cluster %i" % (original_point[0], original_point[1], converged_point[0], converged_point[1], cluster_assignment)

if __name__ == '__main__':
    run()