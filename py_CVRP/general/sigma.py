import math
import sys


def sigma(last):
    total = 0
    for i in range(last, 1, -1):
        total += math.comb(i,2)
    return total


def main():
    """
    Argument 1: relative path to vrp-file ("../data/Vrp-Set-X/X-n101-k25.vrp")
    """
    print(sigma(int(sys.argv[1])))


if __name__ == '__main__':
    main()