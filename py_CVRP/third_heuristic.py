import sys
from general import read_vrp


def main():
    """
    Argument 1: relative path to vrp-file ("../data/Vrp-Set-X/X-n101-k25.vrp")
    """
    problem = read_vrp.read_vrp_file(sys.argv[1])
    problem.nearest_five(problem.locations.get_location(1), 206)


if __name__ == '__main__':
    main()
