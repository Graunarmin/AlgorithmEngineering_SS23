# local imports
from maths import abs_fl


class Measure:

    def __init__(self, p, q, r):
        self.mes = self.sum(self.diff(self.prod(abs_fl(p.x),
                                                self.diff(self.prod(abs_fl(q.y), abs_fl(r.w)),
                                                          self.prod(abs_fl(r.y), abs_fl(q.w)))),
                                      self.prod(abs_fl(p.y),
                                                self.diff(self.prod(abs_fl(q.x), abs_fl(r.w)),
                                                          self.prod(abs_fl(r.x), abs_fl(q.w))))),
                            self.prod(abs_fl(p.w),
                                      self.diff(self.prod(abs_fl(q.x), abs_fl(r.y)),
                                                self.prod(abs_fl(r.x), abs_fl(q.y)))))

    def sum(self, mes_a, mes_b):
        return mes_a + mes_b

    def diff(self, mes_a, mes_b):
        return self.sum(mes_a, mes_b)

    def prod(self, mes_a, mes_b):
        return mes_a * mes_b
