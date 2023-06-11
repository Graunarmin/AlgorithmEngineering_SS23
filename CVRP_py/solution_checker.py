import sys
from CVRP_py.helpers import read_vrp
from CVRP_py.helpers import read_sol
from CVRP_py.classes.Timer import WallClockTimer
from CVRP_py.classes.Timer import CPUTimer


def main():
    """
    Argument 1: relative path to vrp-file ("../data/Vrp-Set-X/X-n101-k25.vrp")
    Argument 2: relative path to matching sol-file ("../data/Vrp-Set-X/X-n101-k25.sol")
    """
    wall_time = WallClockTimer()
    cpu_time = CPUTimer()

    problem = read_vrp.read_vrp_file(sys.argv[1])
    solution = read_sol.read_sol_file(sys.argv[2])

    solution.check_solution(problem)

    wall_time.stop()
    cpu_time.stop()


if __name__ == '__main__':
    main()
