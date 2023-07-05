class Index:

    def __init__(self):
        self.ind = self.sum(self.diff(self.prod(1,
                                                self.diff(self.prod(1, 1),
                                                          self.prod(1, 1))),
                                      self.prod(1,
                                                self.diff(self.prod(1, 1),
                                                          self.prod(1, 1)))),
                            self.prod(1,
                                      self.diff(self.prod(1, 1),
                                                self.prod(1, 1))))

    def sum(self, ind_a, ind_b):
        epsilon = pow(2, -53)
        return 1 + max(ind_a, ind_b) * (1 + epsilon)

    def diff(self, ind_a, ind_b):
        return sum(ind_a, ind_b)

    def prod(self, ind_a, ind_b):
        epsilon = pow(2, -53)
        return 1 + ind_a * (1 + epsilon) + ind_b * pow(1 + epsilon, 2)
