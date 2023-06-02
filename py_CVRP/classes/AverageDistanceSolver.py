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
                [found, nearest_5] = problem.nearest_five(current, route.cargo_amount)

                if found:
                    # 1. sort nearest5 by average_distance (max to min)
                    # 2. go through list and visit the first one with
                    # average_distance < distance between current and node
                    pass
