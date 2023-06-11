import math


def location_distance(loc_1, loc_2):
    """
    Computes and returns the euclidian 2D-Distance between loc_1 and loc_2
    """
    l_1 = loc_1.coordinates()
    l_2 = loc_2.coordinates()

    # round distance to the smallest integer greater than or equal to x
    distance = int(math.ceil(math.dist(l_1, l_2)))

    return distance


def sigma_binomial_coefficient(last):
    """
    Computes and returns the sum of (i choose 2) from i = 1 to last
    :param last:
    """
    total = 0
    for i in range(last, 1, -1):
        total += math.comb(i, 2)
    return total
