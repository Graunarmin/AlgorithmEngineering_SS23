from classes import InstanceGenerator as IG


def main():
    """
    Generates N random instances for each n given in number_of_locations.
    Folders n-<n> have to exist in "../data/custom/"
    """
    # vrp_folder = "../data/small/"
    # numbers_of_locations = [20, 50, 100]
    # number_of_instances = 10

    # vrp_folder = "../data/custom/"
    # numbers_of_locations = [100, 150, 200, 250, 300, 350, 400, 500, 600, 700]

    vrp_folder = "../data/horse-race-special/"
    numbers_of_locations = [300]
    number_of_instances = 1000

    IG.InstanceGenerator(numbers_of_locations=numbers_of_locations,
                         number_of_instances=number_of_instances,
                         vrp_folder=vrp_folder)


if __name__ == '__main__':
    main()
