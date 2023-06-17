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


def mean(x_values):
    res = sum(x_values) / len(x_values)
    return round(res, 3)


def variance(x_values, x_mean):
    var = sum([(x - x_mean) ** 2 for x in x_values]) / (len(x_values) - 1)
    return round(var, 3)


def covariance(x_values, x_mean, y_values, y_mean):
    """
    Computes the Covariance of X and Y
    """
    cov = sum([(x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values)])

    return round((cov / (len(x_values) - 1)), 3)


def random_variate(x_values, y_values, y_variance, covariance):
    """
    Computes the random variate z = x - a(y - mean(Y))
    mit a = Cov(X,Y)/Var(Y)
    """
    rd_variates = [x - (covariance / y_variance) * (y - y_variance)
                   for x, y in zip(x_values, y_values)]

    return rd_variates
