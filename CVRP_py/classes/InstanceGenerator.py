import os
import random
from ..classes import LocationsContainer as lc
from ..classes import LocationNode as ln
from ..classes import Problem as prbl


class InstanceGenerator:

    def __init__(self):
        self.file_path = "../data/custom/"

    def create_locations(self, number_of_locations, instance_id=0):
        locations = lc.LocationsContainer()
        locations.init_location_list(int(number_of_locations))
        for n in range(0, int(number_of_locations)):
            node_id = n
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            if node_id == 1:
                demand = 0
            else:
                demand = random.randint(1, 101)

            node = ln.LocationNode(node_id=n, x_coord=x, y_coord=y, demand=demand)
            locations.add_location(node)

        locations.set_depot_id(1)
        locations.create_distance_matrix()
        capacity = random.randint(180, 400)
        filename = "Custom-n" + str(number_of_locations) + "-" + "q" + str(capacity) + "_" + str(instance_id) + ".vrp"
        problem = prbl.Problem(locations=locations, capacity=capacity, file_name=filename)

        self.write_instances_to_file(problem, number_of_locations)

    def write_instances_to_file(self, problem, dimension):
        path = self.file_path
        if os.path.exists(path) and os.access(path, os.R_OK):
            with open(path + problem.file_name, 'w') as outfile:
                line = "NAME : " + problem.file_name.replace(".vrp", "") + "\n"
                outfile.write(line)

                line = "COMMENT : Created by Johanna Sacher and Christian Paffrath \n"
                outfile.write(line)

                line = "TYPE : CVRP \n"
                outfile.write(line)

                line = "DIMENSION : " + str(dimension) + "\n"
                outfile.write(line)

                line = "EDGE_WEIGHT_TYPE : EUC_2D \n"
                outfile.write(line)

                line = "CAPACITY : " + str(problem.vehicle_capacity) + "\n"
                outfile.write(line)

                line = "NODE_COORD_SECTION \n"
                outfile.write(line)
                for node in problem.locations.locations:
                    line = str(node.loc_id + 1) + " " + str(node.x) + " " + str(node.y) + "\n"
                    outfile.write(line)

                line = "DEMAND_SECTION \n"
                outfile.write(line)

                for node in problem.locations.locations:
                    line = str(node.loc_id + 1) + " " + str(node.demand) + "\n"
                    outfile.write(line)

                line = "DEPOT_SECTION\n1\n-1\n"
                outfile.write(line)

                line = "EOF\n"
                outfile.write(line)

        else:
            print(path, " does not exist")
