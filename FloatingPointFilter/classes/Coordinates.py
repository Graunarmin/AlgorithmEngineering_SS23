from fractions import Fraction


class HomogenousCoordinate:

    def __init__(self, x, y, w):
        self.x = Fraction(x)
        self.y = Fraction(y)
        self.w = Fraction(w)

    def float_coord(self):
        x = float(self.x)
        y = float(self.y)
        w = float(self.w)
        return[x, y, w]

    def fraction_coord(self):
        x = Fraction(self.x)
        y = Fraction(self.y)
        w = Fraction(self.w)
        return[x, y, w]


class CoordinateTriple:
    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r
        self.orient = 0
