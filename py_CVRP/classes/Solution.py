class Solution:

    def __init__(self, routes_map, sol_file_cost=0):
        self.sol_file_cost = sol_file_cost
        self.required_locations = None

        for route_id in routes_map:
            self.create_route(route_id, routes_map[route_id])

    def check_solution(self, problem):
        self.required_locations = problem.locations
        if self.capacity_condition_valid() and self.one_visit_condition_valid():
            print("Solution is VALID for given Problem.")
            return True
        print("Solution is NOT VALID for given Problem.")
        return False

    def capacity_condition_valid(self):
        for route in self.routes:
            if not route.total_demand_meets_capacity():
                print("The demand on at least one routes is bigger than the maximum vehicle capacity.")
                return False
        print("The demand on all routes is less or equal to the maximum vehicle capacity.")
        return True

    def one_visit_condition_valid(self):
        return self.required_locations.check_visited_once()

    def total_cost_matches(self):
        total_dist = 0
        for route in self.routes:
            total_dist += route.total_cost

        if self.sol_file_cost != total_dist:
            print("The solution-costs of " , self.sol_file_cost, " for the Tour do not match the calculated costs of "
                  , total_dist, " (but this is probably due to our rounding or calculation).")
            return False
        print("The solution-costs of ", self.sol_file_cost, " for the Tour match the calculated costs.")
        return True

    def create_route(self, route_id, customer_ids):
        pass
