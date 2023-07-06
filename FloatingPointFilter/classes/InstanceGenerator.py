# standard library imports
import sys
from random import randint


class InstanceGenerator:
    def __init__(self, n):
        self.max = sys.maxsize
        self.data = {}
        self.generate_points(n)

    def generate_points(self, n):
        points = ["p", "q", "r"]

        for i in range(0, n):
            self.data[i] = {"p": [],
                            "q": [],
                            "r": []}

            for point in points:
                x = randint(-self.max, self.max)
                y = randint(-self.max, self.max)
                w = randint(1, self.max)
                self.data[i][point] = [str(x), str(y), str(w)]

    def generate_collinear_points(self, n, start_index):
        """
        Ideally this function would deliberately add some collinear points
        But I don't have time, so we just hope some are generated randomly
        """
        points = ["p", "q", "r"]
        for i in range(0, n):
            start_index = start_index + 1

            self.data[start_index] = {"p": [],
                                      "q": [],
                                      "r": []}
