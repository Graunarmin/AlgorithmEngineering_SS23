# standard library imports
import os

# local imports
from classes import HorseRaceData as hrd
from classes.GreedySolver import GreedySolver
from classes.AverageDistanceSolver import AverageDistanceSolver
from helpers.read_vrp import read_vrp_file


def main():
    """
    Recursively walks through all .vrp-files in rootdir and solves them
    with the Greedy-Solver.
    Then the various statistics (mean, variance, covariance) are computed
    and writen to a .json file and also formatted as a LaTeX Table
    """
    # 4.a: solve old n-300 Instances with Average Distance Solver
    # 4.b: solve new n-300 Instances with Greedy Solver
    # 4.c: solve old n-300 Instances with Greedy Solver and compare

    instances = ["../data/custom/n-300", "../data/horse-race-special/n-300"]
    data = hrd.HorseRaceData()
    instance_counter = 0

    for filepath in instances:
        instance_counter += 1

        for subdir, dirs, files in os.walk(filepath):
            for file in files:
                if file.endswith('.vrp'):
                    ad_solver = AverageDistanceSolver()
                    greedy_solver = GreedySolver()

                    ad_problem = read_vrp_file(os.path.join(subdir, file))
                    greedy_problem = read_vrp_file(os.path.join(subdir, file))

                    ad_solution = ad_solver.solve(ad_problem)
                    data.add_solution_data(ad_solution, heuristic="a", instance=instance_counter)

                    greedy_solution = greedy_solver.solve(greedy_problem)
                    data.add_solution_data(greedy_solution, heuristic="g", instance=instance_counter)

    data.compute_mean()
    data.write_data_to_json("../data/results/randomized-horse-race.json")


if __name__ == '__main__':
    main()
