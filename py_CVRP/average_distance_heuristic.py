import sys
from general import read_vrp
from classes.Solvers.AverageDistanceSolver import AverageDistanceSolver
from classes.Timer import WallClockTimer
from classes.Timer import CPUTimer


def main():
    """
    Argument 1: relative path to vrp-file ("../data/Vrp-Set-X/X-n101-k25.vrp")
    """
    wall_time = WallClockTimer()
    cpu_time = CPUTimer()

    problem = read_vrp.read_vrp_file(sys.argv[1])
    average_distance_solution = AverageDistanceSolver().solve(problem)
    average_distance_solution.check_solution(problem, own_solution=True)

    wall_time = wall_time.stop()
    cpu_time = cpu_time.stop()

    average_distance_solution.write_time(wall_time, cpu_time)


if __name__ == '__main__':
    main()
