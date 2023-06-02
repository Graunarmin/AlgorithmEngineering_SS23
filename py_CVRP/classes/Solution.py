from general import conditions


class Solution:

    def __init__(self, routes_map, sol_file_cost=0):
        self.sol_file_cost = sol_file_cost  # the costs that were given in the sol-file
        self.routes_map = routes_map        # map of routes {route_id1:[wp1, wp2, ...], route_id2: [...], ...}

    def check_solution(self, problem, own_solution=False):

        # create a list of Route-Objects
        if own_solution:
            routes = [route for route in self.routes_map.values()]
        else:
            routes = self.create_routes(problem)

        # self.total_cost_matches(routes)

        # check if the routes fulfill all conditions:
        # 1. is every route within the capacity-bound?
        # 2. is every required customer visited exactly once?
        if conditions.capacity_condition_valid(routes) \
                and conditions.one_visit_condition_valid(problem.locations):
            print("Solution is VALID for given Problem.")
            return True
        print("Solution is NOT VALID for given Problem.")
        return False

    def create_routes(self, problem):
        routes = []
        for route_id in self.routes_map:
            customers = self.routes_map[route_id]
            route = problem.locations.create_route(customers, route_id, problem.vehicle_capacity)
            routes.append(route)

        return routes

    def total_cost_matches(self, routes):
        total_dist = 0
        for route in routes:
            total_dist += route.total_cost

        if self.sol_file_cost != total_dist:
            print("The solution-costs of ", self.sol_file_cost, " for the Tour do not match the calculated costs of "
                  , total_dist, " (but this is probably due to our rounding or calculation).")
            return False
        print("The solution-costs of ", self.sol_file_cost, " for the Tour match the calculated costs.")
        return True
