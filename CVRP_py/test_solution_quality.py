# standard library imports
import os

# local imports
from classes import TableData as td
from classes.GreedySolver import GreedySolver
from helpers.read_vrp import read_vrp_file


def main():
    """
    Recursively walks through all .vrp-files in rootdir and solves them
    with the Greedy-Solver.
    Then the various statistics (means, variance, covariance) are computed
    and writen to a .json file and a .txt file
    """
    rootdir = "../data/custom/"

    numbers_of_locations = [100, 150, 200, 250, 300, 350, 400, 500, 600, 700]
    number_of_instances = 1000

    # rootdir = "../data/small/"

    # numbers_of_locations = [20, 50, 100]
    # number_of_instances = 10

    table_data = td.TableData(numbers_of_locations, number_of_instances)

    for subdir, dirs, files in os.walk(rootdir):
        split = subdir.split("-")
        n = 0
        if len(split) > 1:
            n = split[1]

        # print("CURRENTLY AT n = " + str(n))
        for file in files:
            if file.endswith('.vrp'):
                # print(os.path.join(subdir, file))
                greedy_solver = GreedySolver()
                problem = read_vrp_file(os.path.join(subdir, file))
                solution = greedy_solver.solve(problem)
                # greedy_solver.write_solution_file("greedy/", problem.file_name.replace(".vrp", ".txt"))

                table_data.add_solution_data(solution, n)
                # pass

    table_data.last_solution_added()
    table_data.write_data_to_json("../data/results/solution-quality-test.json")
    table_data.write_data_to_latex_table("../data/results/solution-quality-test.txt")


if __name__ == '__main__':
    main()
