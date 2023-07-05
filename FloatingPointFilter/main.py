import PointOrientation as po
from PointOrientation import ThreePointOrientation
from classes.Coordinates import HomogenousCoordinate as hc


def main():
    constants = ThreePointOrientation()

    p = hc("7", "2", "1")
    q = hc("6", "6", "1")
    r = hc("4", "4", "1")

    float_sign = po.floating_point_arithmetics(p, q, r)
    exact_sign = po.integer_arithmetics(p, q, r)
    filter_sign = po.floating_point_filter(p, q, r,
                                           constants.double_precision,
                                           constants.index)

    print("Float-Precision: ", float_sign)
    print("Exact: ", exact_sign)
    print("Filter: ", filter_sign)


if __name__ == '__main__':
    main()
