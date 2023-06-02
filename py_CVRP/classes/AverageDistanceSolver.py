from classes import Route as rt
from classes.Solver import Solver
from classes.Solution import Solution


class AverageDistanceSolver(Solver):
    def __init__(self):
        super().__init__()

    def solve(self, problem):
        route_id = 0

        while problem.any_location_unvisited():
            route_id += 1
            route = rt.Route(route_id, problem.vehicle_capacity)

            current = problem.depot()
            route.add_waypoint(demand=current.demand,
                               distance=0,
                               waypoint_id=current.loc_id,
                               depot=True)
            problem.visit_depot()

            while True:
                [found, nearest_5] = problem.nearest_five(current.loc_id, route.cargo_amount)

                if found:
                    nearest = problem.locations.get_location(min(zip(nearest_5.values(), nearest_5.keys()))[1])
                    # 1. sort nearest5 by distance from current (max to min)
                    candidate_order = [node_id for node_id in nearest_5.keys()]
                    candidate_order = sorted(candidate_order, key=lambda x: nearest_5[x])
                    candidate_order.reverse()

                    # 2. go through list and visit the first one that has no distance to another node
                    # which is smaller than the distance to current
                    for node_id in candidate_order:
                        # TODO: sth. is probably wrong with smaller_distance_remaining - CHECK!!
                        if not problem.locations.smaller_distance_remaining(node_id, nearest_5[node_id]):
                            nearest = problem.locations.get_location(node_id)

                    # 3. Add node to route
                    route.add_waypoint(demand=nearest.demand,
                                       distance=problem.distance_between(
                                           current.loc_id, nearest.loc_id),
                                       waypoint_id=nearest.loc_id,
                                       depot=False)

                    # and mark it as visited
                    problem.visit_node(nearest.loc_id)

                    # then set start for next tour to current location
                    current = nearest
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