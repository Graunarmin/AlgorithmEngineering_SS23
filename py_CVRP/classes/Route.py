class Route:

    def __init__(self, route_id, capacity, distance=0, demand=0):
        self.route_id = route_id
        self.total_cost = distance          # accumulated distance between all waypoints on this route
        self.route_capacity = capacity      # vehicle capacity for this route
        self.total_demand = demand          # accumulated demand from all customers on this route
        self.cargo_amount = capacity        # remaining cargo after visiting each customer
        self.waypoints = []                 # List of IDs that are visited:

    def add_waypoint(self, demand, distance, waypoint_id, depot=False):
        if not depot:
            # check if there is any capacity left on this route:
            if self.cargo_depleted():
                print("ERROR, can't add any more customers, not enough capacity left!")
                return

            # check if the customer demand is too high for the remaining cargo:
            if not self.demand_can_be_met(demand):
                print("ERROR, cannot add customer with ID", waypoint_id)
                print("Their demand of", demand, "is too high for the cargo of", self.cargo_amount, "that's left!")
                return

        self.total_demand += demand
        self.cargo_amount -= demand
        self.total_cost += distance
        self.waypoints.append(waypoint_id)
        # print("Successfully added waypoint ID", waypoint_id, "with Demand", demand, ". Cargo:", self.cargo_amount)

    def cargo_depleted(self):
        return self.cargo_amount <= 0

    def demand_can_be_met(self, demand):
        return demand <= self.cargo_amount

    def total_demand_meets_capacity(self):
        return self.total_demand <= self.route_capacity
