class Problem:

    def __init__(self, locations, capacity):
        self.locations = locations          # LocationContainer
        self.vehicle_capacity = capacity    # int
        self.average_distance = 0

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
