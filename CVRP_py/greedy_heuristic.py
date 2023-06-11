import sys
from CVRP_py.helpers import read_vrp
from CVRP_py.classes.Solvers.GreedySolver import GreedySolver
from CVRP_py.classes.Timer import WallClockTimer
from CVRP_py.classes.Timer import CPUTimer


def main():
    """
    Argument 1: relative path to vrp-file ("../data/Vrp-Set-X/X-n101-k25.vrp")
    """
    wall_time = WallClockTimer()
    cpu_time = CPUTimer()

    problem = read_vrp.read_vrp_file(sys.argv[1])

    greedy_solution = GreedySolver().solve(problem)
    greedy_solution.check_solution(problem, own_solution=True)

    wall_time = wall_time.stop()
    cpu_time = cpu_time.stop()

    greedy_solution.write_time(wall_time, cpu_time)


if __name__ == '__main__':
    main()
