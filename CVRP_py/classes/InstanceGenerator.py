# standard library imports
import random

# local imports
from classes import LocationsContainer as lc
from classes import LocationNode as ln
from classes import Problem as prbl


def create_locations(number_of_locations,
                     max_x=1000, max_y=1000,
                     max_demand=101, capacity_range=(180, 400),
                     instance_id=0):
    """
    Creates a LocationsContainer-Object with the number of locations given in number_of_locations.
    Optionally the max x- and y-coordinates can be specified,
    as well as the max demand,
    and a range for randomly choosing the capacity from.
    In case of creating multiple random instances for the same n it can be helpful to also give a running number
    for the instance_id as to not overwrite instances with the same capacity that were created before.
    """
    locations = lc.LocationsContainer()
    locations.init_location_list(int(number_of_locations))
    for n in range(0, int(number_of_locations)):
        node_id = n
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        if node_id == 0:
            demand = 0
        else:
            demand = random.randint(1, max_demand)

        node = ln.LocationNode(node_id=n, x_coord=x, y_coord=y, demand=demand)
        locations.add_location(node)

    locations.set_depot_id(0)
    locations.create_distance_matrix()
    capacity = random.randint(capacity_range[0], capacity_range[1])
    filename = "Custom-n" + str(number_of_locations) + "-" + "q" + str(capacity) + "_" + str(instance_id) + ".vrp"
    problem = prbl.Problem(locations=locations, capacity=capacity, file_name=filename)

    return problem


class InstanceGenerator:

    def __init__(self, numbers_of_locations, number_of_instances, vrp_folder,
                 max_x=1000, max_y=1000,
                 max_demand=101, capacity_range=(180, 400),
                 instance_id=0
                 ):
        for n in numbers_of_locations:
            for i in range(number_of_instances + 1):
                problem = create_locations(n,
                                           max_x, max_y,
                                           max_demand,
                                           capacity_range,
                                           instance_id=i)

                problem.write_vrp_file(n, vrp_folder)
