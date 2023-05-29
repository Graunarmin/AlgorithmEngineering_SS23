def one_visit_condition_valid(required_locations):
    """
    Condition 1: Every Customer is visited exactly once
    :param required_locations: all locations specified in the vrp-file
    :return: True if every location was visited exactly once, False otherwise
    """
    return required_locations.check_visited_once()


def capacity_condition_valid(routes):
    """
    Condition 2: The Demand on a single route is never greater than the vehicle capacity
    :param routes: The list of all routes specified in the sol-file
    :return: True if the capacity is met on all routes, False otherwise
    """
    for route in routes:
        if not route.total_demand_meets_capacity():
            print("The demand on at least one routes is bigger than the maximum vehicle capacity.")
            return False
    print("The demand on all routes is less or equal to the maximum vehicle capacity.")
    return True


"""
Condition 3: All routes start and end at depot
Implied by sol-file format.
can only be checked by testing if the total distance is correct when including the depot
"""

"""
Condition 4: There are no sub-tours
"""

