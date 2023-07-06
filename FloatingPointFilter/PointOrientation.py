# standard library imports
import maths
from fractions import Fraction

# local imports
from classes.Measure import Measure
from classes.Index import Index


class ThreePointOrientation:
    def __init__(self):
        self.single_precision = pow(2, -24)
        self.double_precision = pow(2, -53)
        self.index = Index().ind


# -------------- STATIC FUNCTIONS ----------------
def floating_point_arithmetics(p, q, r):
    approx_det = maths.approximate_determinant(p.cartesian(),
                                               q.cartesian(),
                                               r.cartesian())

    if approx_det < 0:
        return -1
    elif approx_det > 0:
        return 1
    else:
        return 0


def integer_arithmetics(p, q, r):
    det = maths.precise_determinant(p, q, r)

    if det < Fraction(0):
        return -1
    elif det > Fraction(0):
        return 1
    else:
        return 0


def floating_point_filter(p, q, r, epsilon, index):
    approx_det = maths.approximate_determinant(p.cartesian(),
                                               q.cartesian(),
                                               r.cartesian())

    # 3. compute measure and index
    mes_E = Measure(p, q, r).mes
    ind_E = index

    # 4. compute B
    upper_bound = epsilon * ind_E * mes_E

    # 5. determine sign(E)
    if approx_det >= upper_bound:
        return 1
    elif approx_det <= -upper_bound:
        return -1
    elif upper_bound < 1 and maths.is_integer(approx_det):
        return 0
    else:
        return integer_arithmetics(p, q, r)
