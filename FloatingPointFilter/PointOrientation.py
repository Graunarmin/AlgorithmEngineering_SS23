from classes.Measure import Measure
from classes.Index import Index


def preparation(p, q, r):
    epsilon_float = pow(2, -24)
    epsilon_double = pow(2, -53)

    # 1. Homogene Koordinaten in Gleitkommazahlen konvertieren
    float_p = p.floating_point_coordinate()
    float_q = q.floating_point_coordinate()
    float_r = r.floating_point_coordinate()


def approximate_determinant(p, q, r, precision):
    approx_determinant = p.x * (q.y * r.w - r.y * q.w) - \
                          p.y * (q.x * r.w - r.x * q.w) + \
                          p.w * (q.x * r.y - r.x * q.y)

    return approx_determinant


def is_integer(a):
    pass


def floating_point_arithmetics(p, q, r, precision):
    det = approximate_determinant(p, q, r, precision)

    if det < 0:
        return -1
    elif det > 0:
        return 1
    else:
        return 0


def integer_arithmetics(p, q, r):
    pass


def floating_point_filter(p, q, r, epsilon):
    det_approx = approximate_determinant(p, q, r, epsilon)

    # 3. compute measure and index
    mes_E = Measure(p, q, r).mes
    ind_E = Index().ind

    # 4. compute B
    upper_bound = epsilon * ind_E * mes_E

    # 5. determine sign(E)
    if det_approx >= upper_bound:
        return 1
    elif det_approx <= -upper_bound:
        return -1
    elif upper_bound < 1 and is_integer(det_approx):
        return 0
    else:
        return integer_arithmetics(p, q, r)






