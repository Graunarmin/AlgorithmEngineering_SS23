import fractions
import numbers


def fl(a):
    return float(a)


def abs_fl(a):
    return abs(fl(a))


def approximate_determinant(p, q, r):
    approx_determinant = fl(p.x) * (fl(q.y) * fl(r.w) - fl(r.y) * fl(q.w)) - \
                         fl(p.y) * (fl(q.x) * fl(r.w) - fl(r.x) * fl(q.w)) + \
                         fl(p.w) * (fl(q.x) * fl(r.y) - fl(r.x) * fl(q.y))

    return approx_determinant


def precise_determinant(p, q, r):
    det = p.x * (q.y * r.w - r.y * q.w) - \
          p.y * (q.x * r.w - r.x * q.w) + \
          p.w * (q.x * r.y - r.x * q.y)

    return det


def is_integer(a):
    if isinstance(a, numbers.Integral):
        return True
    if isinstance(a, fractions.Fraction):
        if a.denominator == 1 or a.numerator == a.denominator:
            return True
    if isinstance(a, float):
        return a.is_integer()
    return False
