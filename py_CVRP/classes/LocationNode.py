class LocationNode:

    def __init__(self, node_id, x_coord=0, y_coord=0, demand=0):
        self.location_id = node_id
        self.demand = demand
        self.x = x_coord
        self.y = y_coord
        self.times_visited = 0

    def visit(self):
        self.times_visited += 1

    def coordinates(self):
        return [self.x, self.y]
