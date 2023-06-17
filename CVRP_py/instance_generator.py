from classes import InstanceGenerator as IG


def main():
    generator = IG.InstanceGenerator("../data/custom/")

    numbers_of_locations = [100, 150, 200, 250, 300, 350, 400, 500, 600, 700]
    number_of_instances = 1000

    # generator = IG.InstanceGenerator("../data/small/")
    # numbers_of_locations = [20, 50, 100]
    # number_of_instances = 10

    for n in numbers_of_locations:
        for i in range(number_of_instances+1):
            generator.create_locations(n, instance_id=i)


if __name__ == '__main__':
    main()
