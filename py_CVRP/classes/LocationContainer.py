from general import maths
import Route
import sys


class LocationContainer:
    def __init__(self):
        self.locations = []
        self.distance_matrix = []

    def add_location(self, location_node):
        self.locations.append(location_node)

    def remove_location(self, location_node):
        self.locations = [loc for loc in self.locations if loc.location_id != location_node.location_id]

    def get_depot(self):
        if len(self.locations):
            print("No Locations added yet, there is no depot!")
            return
        return self.locations[0]

    def get_node_by_id(self, node_id):
        for loc in self.locations:
            if loc.location_id == node_id:
                return loc

    def create_distance_matrix(self):
        """
        Credit: https://github.com/vss2sn/cvrp/blob/master/src/utils.cpp#L178
        Function that creates a matrix containing the distances between all individual locations.
        distance_matrix[i][j] = distance between customer i and customer j
        (IDs based on location-ids from the vrp-file or the problem class)
        """
        for i in range(len(self.locations)):
            for j in range(i, len(self.locations)):
                self.distance_matrix[i][j] = maths.location_distance(self.locations[i], self.locations[j])
                self.distance_matrix[j][i] = self.distance_matrix[i][j]

    def create_route(self, customer_ids, route_id):
        """
        Creates a route from a given set of customers
        :param customer_ids: List of customers, that are visited on this route in the given order.
        IDs have to match the location-ids from the vrp-file!
        :param route_id: the id of the route
        :return: a Route-Object that visits all customers on the list
        """

        route = Route.Route(route_id)

        # all routes start at depot
        depot = self.get_depot()
        route.add_location(depot)

        for customer in customer_ids:
            # add node to route
            customer_node = self.get_node_by_id(customer)
            route.add_location(customer_node)

        # all routes end at depot
        route.add_location(depot)
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

    def check_any_node_unvisited(self):
        """
        Checks if any location was not visited at all
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
                    and self.locations[j].demand <= max_demand \
                    and self.distance_matrix[current_node.location_id][j] < cost:
                cost = self.distance_matrix[current_node.location_id][j]
                closest_id = j
                found = True

        return [found, self.locations[closest_id]]
