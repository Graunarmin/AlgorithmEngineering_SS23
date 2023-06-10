import random
import os
from classes import LocationsContainer as lc
from classes import LocationNode as ln
from classes import Problem as prbl


class InstanceGenerator:

    def __init__(self, n):
        self.create_locations(n)
        self.file_path = "../data/custom/"

    def create_locations(self, number_of_locations):
        locations = lc.LocationsContainer()
        for n in range(1, number_of_locations):
            node_id = n
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            if node_id == 1:
                demand = 0
            else:
                demand = random.randint(1, 1001)

            locations.add_location(ln.LocationNode(node_id=n, x_coord=x, y_coord=y, demand=demand))

        locations.set_depot_id(1)
        locations.create_distance_matrix()
        capacity = random.randint(180, 500)
        filename = "Custom-n" + str(number_of_locations) + "-" + "k" + str(capacity) + ".vrp"
        problem = prbl.Problem(locations=locations, capacity=capacity, file_name=filename)

        self.write_instances_to_file(problem)

    def write_instances_to_file(self, problem):
        path = self.file_path
        if os.path.exists(path) and os.access(path, os.R_OK):
            with open(path + problem.file_name, 'w') as outfile:
                line = "NAME : " + problem.file_name.replace(".vrp", "")
                outfile.write(line + "\n")
                line = "COMMENT : "
