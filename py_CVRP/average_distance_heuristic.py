import sys
from general import read_vrp
from classes.AverageDistanceSolver import AverageDistanceSolver
from general.measure_time import WallClockTimer
from general.measure_time import CPUTimer


def main():
    """
    Argument 1: relative path to vrp-file ("../data/Vrp-Set-X/X-n101-k25.vrp")
    """
    wall_time = WallClockTimer()
    cpu_time = CPUTimer()

    problem = read_vrp.read_vrp_file(sys.argv[1])
    distance_consideration_solution = AverageDistanceSolver().solve(problem)
    distance_consideration_solution.check_solution(problem, own_solution=True)

    wall_time.stop()
    cpu_time.stop()


if __name__ == '__main__':
    main()
