import sys

from helpers import maths
from classes import Route as rt


class LocationsContainer:
    def __init__(self):
        self.depot_id = 0
        self.locations = []         # List of LocationNode
        self.distance_matrix = []   # 2D Matrix

    def init_location_list(self, length):
        self.locations = [0] * length

    def add_location(self, location_node):
        self.locations[location_node.loc_id] = location_node

    def get_location(self, node_id):
        try:
            return self.locations[node_id]
        except IndexError:
            print("Couldn't find a Locations with ID", node_id)
            return

    def set_depot_id(self, depot_id):
        self.depot_id = depot_id

    def get_depot(self):
        return self.get_location(self.depot_id)

    def visit_node(self, node_id, route_id=0):
        self.get_location(node_id).visit(route_id)

    def add_demand_to_location(self, loc_id, demand):
        self.get_location(loc_id).demand = demand

    def total_average_distance(self):
        """
        :return: the average distance of all nodes that have not yet been visited
        """
        unvisited_nodes = [node.loc_id for node in self.locations if node.times_visited == 0]
        total_distance = 0

        for i in range(len(unvisited_nodes) - 1):
            start_id = unvisited_nodes[i]
            for j in range(i + 1, len(unvisited_nodes)):
                destination_id = unvisited_nodes[j]
                total_distance += self.get_distance(start_id, destination_id)

        return total_distance / (len(unvisited_nodes) * (len(unvisited_nodes)-1) / 2)

    def average_distance(self, node_id):
        """
        :param node_id: the node of which to compute the average distance to all remaining unvisited nodes
        :return: the average distance of the node to all remaining unvisited nodes
        """
        unvisited_nodes = [node.loc_id for node in self.locations if node.times_visited == 0 and node.loc_id != node_id]

        total_distance = 0
        for i in range(len(unvisited_nodes)):
            destination_id = unvisited_nodes[i]
            total_distance += self.get_distance(node_id, destination_id)

        return total_distance / len(unvisited_nodes)

    def create_distance_matrix(self):
        """
        Credit: https://github.com/vss2sn/cvrp/blob/master/src/utils.cpp#L178
        Function that creates a matrix containing the distances between all individual locations.
        distance_matrix[i][j] = distance between locations[i] (loc_id i) and locations[j] (loc_id j)
        """

        # 1. Prepare 2D Matrix of needed size
        for row in range(len(self.locations)):
            self.distance_matrix.append([0] * len(self.locations))

        # 2. Fill Matrix with Distances
        for i in range(len(self.locations)):
            for j in range(i, len(self.locations)):
                distance = maths.location_distance(self.locations[i], self.locations[j])
                self.distance_matrix[i][j] = distance
                self.distance_matrix[j][i] = distance

        self.total_average_distance()

    def get_distance(self, loc1_id, loc2_id):
        return self.distance_matrix[loc1_id][loc2_id]

    def create_route(self, customer_ids, route_id, capacity):
        """
        Creates a route from a given set of customers
        :param customer_ids: List of customers, that are visited on this route in the given order.
        IDs have to match the location-ids from the vrp-file!
        :param route_id: the id of the route
        :param capacity:
        :return: a Route-Object that visits all customers on the list
        """

        route = rt.Route(route_id, capacity)

        # all routes start at depot
        start_id = self.depot_id
        route.add_waypoint(0, 0, start_id, depot=True)
        self.get_depot().visit(route_id)

        for customer_id in customer_ids:
            # add demand and distance to route
            customer_demand = self.get_location(customer_id).demand
            distance = self.get_distance(start_id, customer_id)
            route.add_waypoint(customer_demand, distance, customer_id)

            # mark location as visited
            self.get_location(customer_id).visit(route_id)

            # set start for next tour to current location
            start_id = customer_id

        # all routes end at depot
        home_stretch = self.get_distance(start_id, self.depot_id)
        route.add_waypoint(0, home_stretch, self.depot_id, depot=True)
        self.get_depot().visit(route_id)
        return route

    def check_visited_once(self):
        """
        Checks if every location was visited exactly once
        :return:
        """
        # if any((loc.times_visited != 1 and loc.location_id != 1) for loc in self.locations):
        for loc in self.locations:
            if loc.loc_id != self.depot_id and loc.times_visited != 1:
                print("Location ", loc.loc_id, " was visited ", loc.times_visited, " times!")
                return False
        print("Every Customer was visited exactly once.")
        return True

    def any_node_unvisited(self):
        """
        Checks if there is any location that was not visited yet (except from depot)
        :return:
        """
        return any(loc.times_visited == 0 for loc in self.locations)

    def find_nearest_unvisited(self, current_id, max_demand):
        """
        Credit: https://github.com/vss2sn/cvrp/blob/master/src/utils.cpp#L96
        :param current_id: the id of the node to which we want to find the closest neighbour
        :param max_demand: the maximum demand that node is allowed to have
        :return:
        """
        cost = sys.float_info.max
        closest_id = 0
        found = False

        for j in range(len(self.distance_matrix[0])):
            # we are looking for a node that is note the depot and
            # 1. was not visited yet,
            # 2. has a demand at most equal to the max_demand and
            # 3. has a distance smaller than the previously found smallest distance to the current node
            if self.locations[j].loc_id != self.depot_id \
                    and self.locations[j].loc_id != current_id \
                    and self.locations[j].times_visited == 0 \
                    and self.locations[j].demand <= max_demand \
                    and self.get_distance(current_id, j) < cost:
                cost = self.get_distance(current_id, j)
                closest_id = j
                found = True

        return [found, self.locations[closest_id]]

    def find_nearest_five(self, current_id, max_demand):
        """
        :param current_id: the id of the node to which we want to find the 5 closest neighbours
        :param max_demand: the maximum demand these nodes are allowed to have
        :return: [bool found, dict closest_five] with found indicating whether any nodes were found 
        and the dictionary filled with up to the 5 closest nodes with node_id as key distance_to_current as value
        """
        closest_five = {}
        found = False

        for j in range(len(self.distance_matrix[0])):
            if self.locations[j].loc_id != self.depot_id \
                    and self.locations[j].loc_id != current_id \
                    and self.locations[j].times_visited == 0 \
                    and self.locations[j].demand <= max_demand:

                cost = self.get_distance(current_id, j)

                # as long as there are less than 5 nodes in the list, just add the next one
                if len(closest_five) < 5:
                    closest_five[j] = cost

                # as soon as there are five values, we start comparing
                else:
                    # if the current cost is smaller than any cost already in the list:
                    if any(cost < c for c in closest_five.values()):
                        # remove the max cost from the list
                        max_key = max(zip(closest_five.values(), closest_five.keys()))[1]
                        del closest_five[max_key]
                        # and add the new, smaller cost
                        closest_five[j] = cost

                if len(closest_five) >= 1:
                    found = True

        return [found, closest_five]

    def print(self):
        for loc in self.locations:
            loc.print()
