from classes import LocationNode as ln
from classes import LocationsContainer as lct
from classes import Problem as prbl


def read_vrp_file(file_path):
    """
    :param file_path:
    :return:
    """
    required_locations = lct.LocationsContainer()
    vehicle_capacity = 0

    with open(file_path, 'r') as file:
        section = 0

        for line in file:
            tokens = line.split()
            keyword = tokens[0]
            if keyword == "DIMENSION":
                section = 1
                required_locations.init_location_list(int(tokens[2]))
            elif keyword == "CAPACITY":
                section = 1
                vehicle_capacity = int(tokens[2])
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

            if section == 2:
                # decrease location-ID by 1 so it matches the index if we put it in a List
                # and also the IDs from the sol-file (which does not include the depot)
                loc_id = int(keyword) - 1
                x_coord = int(tokens[1])
                y_coord = int(tokens[2])
                node = ln.LocationNode(loc_id, x_coord=x_coord, y_coord=y_coord)
                required_locations.add_location(node)

            elif section == 3:
                loc_id = int(keyword) - 1
                required_locations.add_demand_to_location(loc_id, int(tokens[1]))

            elif section == 4:
                required_locations.set_depot_id(int(keyword) - 1)
                section = 5

    required_locations.create_distance_matrix()
    problem = prbl.Problem(required_locations, vehicle_capacity, file_path)
    return problem
