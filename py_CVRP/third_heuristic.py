import sys
from general import read_vrp
from classes.AverageDistanceSolver import AverageDistanceSolver


def main():
    """
    Argument 1: relative path to vrp-file ("../data/Vrp-Set-X/X-n101-k25.vrp")
    """
    problem = read_vrp.read_vrp_file(sys.argv[1])
    # problem.nearest_five(124, 206)
    distance_consideration_solution = AverageDistanceSolver()
    distance_consideration_solution.solve(problem)


if __name__ == '__main__':
    main()
