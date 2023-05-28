from classes import LocationNode as ln
from classes import LocationContainer as lct
from classes import Problem as prbl


def read_file(file_path):
    """
    :param file_path:
    :return:
    """
    required_locations = lct.LocationContainer()
    vehicle_capacity = 0

    with open(file_path, 'r') as file:
        section = 0

        for line in file:
            tokens = line.split()
            keyword = tokens[0]
            if keyword == "CAPACITY":
                section = 1
                vehicle_capacity = tokens[2]
            elif keyword == "NODE_COORD_SECTION":
                section = 2
                continue
            elif keyword == "DEMAND_SECTION":
                section = 3
                continue
            elif keyword == "DEPOT_SECTION":
                section = 4
                continue
            elif keyword == "EOF":
                break

            loc_id = int(keyword)
            if section == 2:
                x_coord = int(tokens[1])
                y_coord = int(tokens[2])
                node = ln.LocationNode(loc_id, x_coord=x_coord, y_coord=y_coord)
                required_locations.add_location(node)

            elif section == 3:
                demand = int(tokens[1])
                required_locations.add_demand_to_location(loc_id, demand)

    problem = prbl.Problem(required_locations, vehicle_capacity)
    return problem
