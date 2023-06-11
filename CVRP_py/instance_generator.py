import sys
from CVRP_py.classes import InstanceGenerator as IG


def main():
    """
    Argument 1: number of locations
    """
    generator = IG.InstanceGenerator()
    # generator.create_locations(sys.argv[1])

    number_of_instances = 1000
    for i in range(number_of_instances):
        generator.create_locations(200, i)


if __name__ == '__main__':
    main()
