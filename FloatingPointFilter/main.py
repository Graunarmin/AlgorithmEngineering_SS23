import json

# local imports
import PointOrientation as po
from PointOrientation import ThreePointOrientation
from classes.Coordinates import HomogenousPoint as hc
from classes.InstanceGenerator import InstanceGenerator
import helper as hp
from classes.Timer import Timer


def main():
    # generator = InstanceGenerator(1000000)
    # hp.write_json(generator.data, "../data/floating-point-filter/instances.json")

    constants = ThreePointOrientation()
    results = {}
    with open("../data/floating-point-filter/instances.json") as file:
        data = json.load(file)

        float_timer = Timer()
        exact_timer = Timer()
        filter_timer = Timer()

        for instance in data:
            p_coord = data[instance]["p"]
            p = hc(p_coord[0], p_coord[1], p_coord[2])

            q_coord = data[instance]["q"]
            q = hc(q_coord[0], q_coord[1], q_coord[2])

            r_coord = data[instance]["r"]
            r = hc(r_coord[0], r_coord[1], r_coord[2])

            filter_timer.start()
            filter_sign = po.floating_point_filter(p, q, r,
                                                   constants.double_precision,
                                                   constants.index)
            filter_timer.pause()

            float_timer.start()
            float_sign = po.floating_point_arithmetics(p, q, r)
            float_timer.pause()

            exact_timer.start()
            exact_sign = po.integer_arithmetics(p, q, r)
            exact_timer.pause()

            results[instance] = {"orient_float": float_sign,
                                 "orient_exact": exact_sign,
                                 "orient_filter": filter_sign}

        print("Timer for Floating Point Arithmetics -  CPU-Time: " + str(float_timer.cpu_time) + ", Wall-Time: " + str(float_timer.wall_time))
        print("Timer for Exact Arithmetics - CPU-Time: " + str(exact_timer.cpu_time) + ", Wall-Time: " + str(exact_timer.wall_time))
        print("Timer for Floating Point Filter -  CPU-Time: " + str(filter_timer.cpu_time) + ", Wall-Time: " + str(filter_timer.wall_time))

    hp.write_json(results, "../data/floating-point-filter/results.json")


if __name__ == '__main__':
    main()
