import math


def location_distance(loc_1, loc_2):
    l_1 = loc_1.coordinates()
    l_2 = loc_2.coordinates()

    # round distance to the smallest integer greater than or equal to x
    distance = int(math.ceil(math.dist(l_1, l_2)))

    return distance
#