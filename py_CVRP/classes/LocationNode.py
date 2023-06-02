class LocationNode:

    def __init__(self, node_id, x_coord=0, y_coord=0, demand=0):
        self.loc_id = node_id  # ID of the location (= vrp_ID - 1 = sol_ID)
        self.demand = demand
        self.x = x_coord
        self.y = y_coord
        self.times_visited = 0
        self.route_ids = []     # List of routes that have visited this node
                                # (should be one for every node except depot)
        self.average_distance = 0

    def visit(self, route_id=0):
        self.times_visited += 1
        self.route_ids.append(route_id)

    def coordinates(self):
        return [self.x, self.y]

    def print(self):
        print("ID:", self.loc_id, " Demand:", self.demand, " Times visited:", self.times_visited)
