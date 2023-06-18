# standard library imports
import os


class Problem:

    def __init__(self, locations, capacity, file_name):
        self.locations = locations          # LocationContainer
        self.vehicle_capacity = capacity    # int
        tokens = file_name.split("/")
        self.file_name = tokens[len(tokens)-1]

    def depot(self):
        return self.locations.get_depot()

    def any_location_unvisited(self):
        return self.locations.any_node_unvisited()

    def nearest_unvisited(self, current_node, max_demand):
        return self.locations.find_nearest_unvisited(current_node, max_demand)

    def visit_node(self, node_id):
        self.locations.visit_node(node_id)

    def visit_depot(self):
        self.locations.visit_node(self.locations.depot_id)

    def distance_between(self, loc1_id, loc2_id):
        return self.locations.get_distance(loc1_id, loc2_id)

    def nearest_five(self, current_node, max_demand):
        return self.locations.find_nearest_five(current_node, max_demand)

    def write_vrp_file(self, dimension, file_path):
        """
        Writes the problem to a file in the required .vrp-format
        """
        path = file_path + "n-" + str(dimension) + "/"
        if os.path.exists(path) and os.access(path, os.R_OK):
            with open(path + self.file_name, 'w') as outfile:
                line = "NAME : " + self.file_name.replace(".vrp", "") + "\n"
                outfile.write(line)

                line = "COMMENT : Created by Johanna Sacher and Christian Paffrath \n"
                outfile.write(line)

                line = "TYPE : CVRP \n"
                outfile.write(line)

                line = "DIMENSION : " + str(dimension) + "\n"
                outfile.write(line)

                line = "EDGE_WEIGHT_TYPE : EUC_2D \n"
                outfile.write(line)

                line = "CAPACITY : " + str(self.vehicle_capacity) + "\n"
                outfile.write(line)

                line = "NODE_COORD_SECTION \n"
                outfile.write(line)
                for node in self.locations.locations:
                    line = str(node.loc_id + 1) + " " + str(node.x) + " " + str(node.y) + "\n"
                    outfile.write(line)

                line = "DEMAND_SECTION \n"
                outfile.write(line)
                for node in self.locations.locations:
                    line = str(node.loc_id + 1) + " " + str(node.demand) + "\n"
                    outfile.write(line)

                line = "DEPOT_SECTION\n1\n-1\n"
                outfile.write(line)

                line = "EOF\n"
                outfile.write(line)

        else:
            print(path, " does not exist")
