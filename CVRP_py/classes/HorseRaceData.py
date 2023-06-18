from helpers import maths
from helpers import load_write


class HorseRaceData:

    def __init__(self):
        self.data = {
            "greedy":
                {
                    "i1":
                        {
                            "length_values": [],
                            "length_mean": 0
                        },
                    "i2":
                        {
                            "length_values": [],
                            "length_mean": 0
                        }
                },
            "average_distance":
                {
                    "i1":
                        {
                            "length_values": [],
                            "length_mean": 0
                        },
                    "i2":
                        {
                            "length_values": [],
                            "length_mean": 0
                        }
                }
        }

    def add_solution_data(self, solution, heuristic, instance):

        if heuristic == "g":
            h = "greedy"
        else:
            h = "average_distance"

        if instance == 1:
            i = "i1"
        else:
            i = "i2"

        self.data[h][i]["length_values"].append(solution.total_length())

    def compute_mean(self):
        for heuristic in self.data.keys():
            for instance in self.data[heuristic].keys():
                values = self.data[heuristic][instance]["length_values"]
                if len(values) > 0:
                    self.data[heuristic][instance]["length_mean"] = maths.mean(values)

        self.data["results"] = {"D12": 0, "D21": 0, "D1": 0, "D2": 0}

        self.data["results"]["D12"] = self.data["average_distance"]["i1"]["length_mean"] - \
                                      self.data["greedy"]["i2"]["length_mean"]

        self.data["results"]["D21"] = self.data["average_distance"]["i2"]["length_mean"] - \
                                      self.data["greedy"]["i1"]["length_mean"]

        number_of_values = len(self.data["average_distance"]["i1"]["length_values"])

        mean_1 = 0
        for a, b in zip(self.data["average_distance"]["i1"]["length_values"],
                        self.data["greedy"]["i1"]["length_values"]):
            mean_1 += (a - b)

        self.data["results"]["D1"] = mean_1 / number_of_values

        mean_2 = 0
        for a, b in zip(self.data["average_distance"]["i2"]["length_values"],
                        self.data["greedy"]["i2"]["length_values"]):
            mean_2 += (a - b)

        self.data["results"]["D2"] = mean_2 / number_of_values

    def write_data_to_json(self, filepath):
        load_write.write_json(self.data, filepath)
