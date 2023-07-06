# standard library imports
from fractions import Fraction


class HomogenousPoint:

    def __init__(self, x, y, w):
        self.x = Fraction(x)
        self.y = Fraction(y)
        self.w = Fraction(w)

    def cartesian(self):
        return CartesianPoint(self.x / self.w, self.y / self.w)

    def print(self):
        print("X: " + str(self.x) + ", Y: " + str(self.y) + ", W: " + str(self.w))


class CartesianPoint:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


class CoordinateTriple:
    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r
        self.orient = 0
