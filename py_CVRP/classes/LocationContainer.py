from general import maths
from classes import Route
import sys


class LocationContainer:
    def __init__(self):
        self.depot_id = 1
        self.locations = []         # List of LocationNode
        self.distance_matrix = []   # 2D Matrix

    def add_location(self, location_node):
        self.locations.append(location_node)

    def set_depot_id(self, depot_id):
        self.depot_id = depot_id

    def get_depot(self):
        try:
            return self.locations[self.depot_id-1]
        except IndexError:
            print("No Locations added yet, there is no depot!")
            return

    def get_node(self, node_id):
        for loc in self.locations:
            if loc.location_id == node_id:
                return loc
        print("Couldn't find a Locations with ID", node_id)
        return

    def visit_node(self, node_id):
        self.get_node(node_id).visit()

    def create_distance_matrix(self):
        """
        Credit: https://github.com/vss2sn/cvrp/blob/master/src/utils.cpp#L178
        Function that creates a matrix containing the distances between all individual locations.
        distance_matrix[i][j] = distance between locations[i] (ID = i+1) and locations[j] (ID = j+1)
        (IDs based on location-ids from the vrp-file)
        """
        tmp = [0] * len(self.locations)
        for row in range(len(self.locations)):
            self.distance_matrix.append(tmp)

        for i in range(len(self.locations)):
            for j in range(i, len(self.locations)):
                self.distance_matrix[i][j] = maths.location_distance(self.locations[i], self.locations[j])
                self.distance_matrix[j][i] = self.distance_matrix[i][j]

    def get_distance(self, loc1_id, loc2_id):
        return self.distance_matrix[loc1_id - 1][loc2_id - 1]

    def create_route(self, customer_ids, route_id, capacity):
        """
        Creates a route from a given set of customers
        :param customer_ids: List of customers, that are visited on this route in the given order.
        IDs have to match the location-ids from the vrp-file!
        :param route_id: the id of the route
        :param capacity:
        :return: a Route-Object that visits all customers on the list
        """

        route = Route.Route(route_id, capacity)

        # all routes start at depot
        start_id = self.depot_id
        route.add_waypoint(self.get_depot().demand, 0, start_id, depot=True)
        self.get_depot().visit(0)

        for customer_id in customer_ids:
            # add demand and distance to route
            customer_demand = self.get_node(customer_id).demand
            distance = self.get_distance(start_id, customer_id)
            route.add_waypoint(customer_demand, distance, customer_id)

            # mark node as visited
            self.get_node(customer_id).visit(route_id)

            # set start for next tour to current location
            start_id = customer_id

        # all routes end at depot
        home_stretch = self.distance_matrix[start_id - 1][self.depot_id - 1]
        route.add_waypoint(self.get_depot().demand, home_stretch, self.depot_id, depot=True)
        return route

    def add_demand_to_location(self, loc_id, demand):
        for loc in self.locations:
            if loc.location_id == loc_id:
                loc.demand = demand
                break

    def check_visited_once(self):
        """
        Checks if every location was visited exactly once
        :return:
        """
        # if any((loc.times_visited != 1 and loc.location_id != 1) for loc in self.locations):
        for loc in self.locations:
            if loc.location_id != 1 and loc.times_visited != 1:
                print("Location ", loc.location_id, " was visited ", loc.times_visited, " times!")
                return False
        print("Every Customer was visited exactly once.")
        return True

    def any_node_unvisited(self):
        """
        Checks if there is any location that was not visited yet (except from depot)
        :return:
        """
        return any(loc.times_visited == 0 for loc in self.locations)

    def find_nearest_unvisited(self, current_node, max_demand):
        """
        Credit: https://github.com/vss2sn/cvrp/blob/master/src/utils.cpp#L96
        :param current_node: the node to which we want to find the closest neighbour
        :param max_demand: the maximum demand that node is allowed to have
        :return:
        """
        cost = sys.float_info.max
        closest_id = 0
        found = False

        for j in range(len(self.distance_matrix[0])):
            # we are looking for a node that
            # 1. was not visited yet,
            # 2. has a demand at most equal to the max_demand and
            # 3. has a distance smaller than the previously found smallest distance to the current node
            if self.locations[j].times_visited == 0 \
                    and self.locations[j].location_id != 1 \
                    and self.locations[j].demand <= max_demand \
                    and self.distance_matrix[current_node.location_id][j] < cost:
                cost = self.distance_matrix[current_node.location_id][j]
                # ToDo: Check the correct ID!!!
                closest_id = j + 1
                found = True

        return [found, self.locations[closest_id]]

    def print(self):
        for loc in self.locations:
            loc.print()
