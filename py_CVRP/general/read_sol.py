from classes import Solution as slt


def read_sol_file(file_path):
    """
    :param file_path:
    :return:
    """
    routes = {}
    sol_cost = 0

    with open(file_path, 'r') as file:
        for line in file:
            tokens = line.split()
            keyword = tokens[0]

            if keyword == "Route":
                # Route #1: 31 46 35
                route_id = tokens[1]
                route_id = route_id.replace("#", "").replace(":", "")

                customers = []
                for customer_id in range(2, len(tokens)):
                    customers.append(int(tokens[customer_id]))
                routes[route_id] = customers

            elif keyword == "Cost":
                sol_cost = tokens[1]

            else:
                print(keyword, " is not a valid keyword! Solution file INVALID.")
                return
            tokens.clear()

        print("sol-file is VALID.")
        solution = slt.Solution(routes, sol_cost)
        return solution
