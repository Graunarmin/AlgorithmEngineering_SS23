from classes import Route as rt
from classes.Solver import Solver


class GreedySolver(Solver):
    def __init__(self, problem):
        super().__init__(problem)

    def solve(self):
        route_id = 0
        while self.problem.locations.any_node_unvisited():
            route_id += 1
            print("Route", route_id)
            route = rt.Route(route_id, self.problem.vehicle_capacity)

            # Start new route at depot:
            current = self.problem.depot()
            route.add_waypoint(current.demand, 0, current.location_id, depot=True)
            self.problem.depot().visit(0)

            while True:
                # Then find the nearest unvisited customer who's demand can be fulfilled by the remaining cargo
                [found, nearest] = self.problem.nearest_unvisited(current, route.cargo_amount)

                # if there is still such a node:
                if found:
                    print("visiting", nearest.location_id)
                    # add it to the route
                    route.add_waypoint(demand=nearest.demand,
                                       distance=self.problem.distance_between(
                                           current.location_id, nearest.location_id),
                                       waypoint_id=nearest.location_id,
                                       depot=False)

                    # and mark it as visited
                    self.problem.visit_node(nearest.location_id)
                    current = nearest
                # if there is no node left that can be visited on this route:
                else:
                    # return back to depot
                    nearest = self.problem.depot()
                    route.add_waypoint(demand=nearest.demand,
                                       distance=self.problem.distance_between(
                                           current.location_id, nearest.location_id),
                                       waypoint_id=nearest.location_id,
                                       depot=True)
                    self.routes[route_id] = route
                    break

            for route in self.routes:
                print("Route #", self.routes[route].route_id, ":", self.routes[route].waypoints)
                self.total_cost += route.total_cost

            print("Cost: ", self.total_cost)
