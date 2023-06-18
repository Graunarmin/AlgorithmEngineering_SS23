import os


class Solver:

    def __init__(self):
        self.routes = {}        # dictionary of the solution-routes
        self.total_cost = 0     # total cost for this solution
        self.solution_path = "../data/sol/"
        self.file_format = ".txt"
        self.heuristics_path = ""

    def solve(self, problem):
        pass

    def check_solution(self, problem):
        pass

    def write_solution_file(self, solver_path, file_name):
        path = self.solution_path + solver_path
        if os.path.exists(path) and os.access(path, os.R_OK):
            with open(path + file_name, 'w') as outfile:
                for route in self.routes:
                    line = "Route #" + str(self.routes[route].route_id) + ": " + str(self.routes[route].waypoints)
                    outfile.write(line + "\n")

                outfile.write("Cost: " + str(self.total_cost) + "\n")
        else:
            print(path, " does not exist")
