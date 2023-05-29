class LocationNode:

    def __init__(self, node_id, x_coord=0, y_coord=0, demand=0):
        self.location_id = node_id
        self.demand = demand
        self.x = x_coord
        self.y = y_coord
        self.times_visited = 0
        self.route_ids = []

    def visit(self, route_id):
        self.times_visited += 1
        self.route_ids.append(route_id)

    def coordinates(self):
        return [self.x, self.y]

    def print(self):
        print("ID:", self.location_id, " Demand:", self.demand, " Times visited:", self.times_visited)
