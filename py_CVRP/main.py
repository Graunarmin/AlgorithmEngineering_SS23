from general import read_vrp
from general import read_sol

if __name__ == '__main__':
    problem = read_vrp.read_vrp_file("../data/Vrp-Set-X/X-n101-k25.vrp")
    solution = read_sol.read_sol_file("../data/Vrp-Set-X/X-n101-k25.sol")

    solution.check_solution(problem)
