class Measure:

    def __init__(self, p, q, r):
        self.mes = self.sum(self.diff(self.prod(float(p.x),
                                                self.diff(self.prod(float(q.y), float(r.w)),
                                                          self.prod(float(r.y), float(q.w)))),
                                      self.prod(float(p.y),
                                                self.diff(self.prod(float(q.x), float(r.w)),
                                                          self.prod(float(r.x), float(q.w))))),
                            self.prod(float(p.w),
                                      self.diff(self.prod(float(q.x), float(r.y)),
                                                self.prod(float(r.x), float(q.y)))))

    def sum(self, mes_a, mes_b):
        return mes_a + mes_b

    def diff(self, mes_a, mes_b):
        return self.sum(mes_a, mes_b)

    def prod(self, mes_a, mes_b):
        return mes_a * mes_b
