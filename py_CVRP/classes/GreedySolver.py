from classes import Route as rt
from classes.Solver import Solver
from classes.Solution import Solution


class GreedySolver(Solver):
    def __init__(self):
        super().__init__()

    def solve(self, problem):
        route_id = 0

        # As long as there are unvisited nodes
        while problem.any_location_unvisited():
            # Create a new route
            route_id += 1
            route = rt.Route(route_id, problem.vehicle_capacity)

            # Start at depot:
            current = problem.depot()
            route.add_waypoint(demand=current.demand,
                               distance=0,
                               waypoint_id=current.loc_id,
                               depot=True)
            problem.visit_depot()

            while True:
                # Then find the nearest unvisited customer who's demand can be fulfilled by the remaining cargo
                [found, nearest] = problem.nearest_unvisited(current, route.cargo_amount)

                # if there still is such a node:
                if found:
                    # add it to the route
                    route.add_waypoint(demand=nearest.demand,
                                       distance=problem.distance_between(
                                           current.loc_id, nearest.loc_id),
                                       waypoint_id=nearest.loc_id,
                                       depot=False)

                    # and mark it as visited
                    problem.visit_node(nearest.loc_id)

                    # then set start for next tour to current location
                    current = nearest

                # if there is no node left that can be visited on this route:
                else:
                    # return back to depot
                    nearest = problem.depot()
                    route.add_waypoint(demand=nearest.demand,
                                       distance=problem.distance_between(
                                           current.loc_id, nearest.loc_id),
                                       waypoint_id=nearest.loc_id,
                                       depot=True)
                    # add route to map
                    self.routes[route_id] = route
                    break

        for route in self.routes:
            print("Route #", self.routes[route].route_id, ":", self.routes[route].waypoints)
            self.total_cost += self.routes[route].total_cost

        print("Cost: ", self.total_cost)
        return Solution(self.routes, self.total_cost)
