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
                [found, closest_five] = problem.nearest_five(current.loc_id, route.cargo_amount)

                if found:
                    # 1. sort closest5 by distance from current (min to max)
                    candidate_order = [node_id for node_id in closest_five.keys()]
                    candidate_order = sorted(candidate_order, key=lambda x: closest_five[x])

                    # 2. set nearest to the closest node
                    nearest = problem.locations.get_location(candidate_order[0])

                    if len(candidate_order) > 1:
                        # 3. Compute the average distance of all remaining locations
                        total_average_distance = problem.locations.total_average_distance()

                        # 4. Go through candidates
                        for node_id in candidate_order:
                            distance_to_current = closest_five[node_id]

                            # 5. Check for Outliers:
                            if problem.locations.average_distance(node_id) > total_average_distance:

                                # 6. If current is closer to that node than the average distance is
                                if distance_to_current < total_average_distance:
                                    # we assume that it could pay off to visit that node now
                                    nearest = problem.locations.get_location(node_id)
                                    break

                    # Add node to route
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
            self.routes[route].print()
            self.total_cost += self.routes[route].total_cost

        print("Cost: ", self.total_cost)
        return Solution(self.routes, self.total_cost)