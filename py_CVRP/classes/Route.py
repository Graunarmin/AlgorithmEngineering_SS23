from general import maths


class Route:

    def __init__(self, route_id, distance=0, demand=0, capacity=0, waypoints=[]):
        self.route_id = route_id
        self.total_cost = distance
        self.total_demand = demand
        self.route_capacity = capacity
        self.cargo_amount = capacity
        self.customers = waypoints

    def add_location(self, location_node):
        # check if there is any capacity left on this route:
        if self.cargo_depleted():
            print("ERROR, can't add any more customers, not enough capacity left!")
            return

        # check if the customer demand is too high to the capacity that's left:
        if not self.demand_can_be_met(location_node.demand):
            print("ERROR, cannot add this customers, their demand is too high for the cargo that's left!")
            return

        if len(self.customers) != 0:
            # increase the total distance of the route
            self.total_cost += maths.location_distance(self.customers[len(self.customers) - 1],
                                                       location_node)

        # add node to route
        self.customers.append(location_node)

        # increase total demand of the route
        self.total_demand += location_node.demand

        # decrease the loaded cargo
        self.cargo_amount -= location_node.demand

    def cargo_depleted(self):
        return self.cargo_amount <= 0

    def demand_can_be_met(self, demand):
        return demand <= self.cargo_amount

    def total_demand_meets_capacity(self):
        return self.total_demand <= self.route_capacity
