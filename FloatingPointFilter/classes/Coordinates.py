class HomogenousCoordinate:

    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

    def floating_point_coordinate(self):
        return FloatingPointCoordinate(self.x/self.w,
                                       self.y/self.w)


class FloatingPointCoordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class CoordinateTriple:
    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r
        self.orient = 0
