from helpers import maths
from helpers import load_write
from helpers import latex_utils as latex


class TableData:

    def __init__(self, list_of_n, number_of_instances):
        self.number_of_instances = number_of_instances
        self.data = {}

        for n in list_of_n:
            self.data[n] = {"length_values": [],
                            "lengths_mean": 0, "lengths_variance": 0,
                            "subtour_values": [],
                            "subtours_mean": 0, "subtours_variance": 0,
                            "covariance": 0,
                            "z_values": [],
                            "z_mean": 0, "z_variance": 0}

        self.current_n = 0
        self.lengths = []
        self.subtours = []

    def add_solution_data(self, solution, n):
        if self.current_n == 0:
            self.current_n = n
            print("n =" + str(n))

        elif self.current_n == n:
            self.lengths.append(solution.total_length())
            self.subtours.append(solution.number_of_subtours())

        else:
            self.compute_results_for_n()
            self.current_n = n
            print("n = " + str(n))

    def last_solution_added(self):
        self.compute_results_for_n()

    def compute_results_for_n(self):
        n = int(self.current_n)
        # print("Computing Results for n = " + str(n))

        lengths_mean = maths.mean(self.lengths)
        lengths_variance = maths.variance(self.lengths, lengths_mean)
        self.data[n]["length_values"] = [x for x in self.lengths]
        self.data[n]["lengths_mean"] = lengths_mean
        self.data[n]["lengths_variance"] = lengths_variance
        # print("Length")
        # print(self.lengths)
        # print("Mean:", lengths_mean, "Variance:", lengths_variance)

        subtours_mean = maths.mean(self.subtours)
        subtours_variance = maths.variance(self.subtours, subtours_mean)
        self.data[n]["subtour_values"] = [x for x in self.subtours]
        self.data[n]["subtours_mean"] = subtours_mean
        self.data[n]["subtours_variance"] = subtours_variance
        # print("Subtours")
        # print(self.subtours)
        # print("Mean:", subtours_mean, "Variance:", subtours_variance)

        covariance = maths.covariance(self.lengths, lengths_mean, self.subtours, subtours_mean)
        self.data[n]["covariance"] = covariance
        # print("Covariance:", covariance)

        z_values = maths.random_variate(self.lengths, self.subtours, subtours_variance, covariance)
        # print("Z-Values:")
        # print(z_values)

        z_mean = maths.mean(z_values)
        z_variance = maths.variance(z_values, z_mean)
        self.data[n]["z_values"] = z_values
        self.data[n]["z_mean"] = z_mean
        self.data[n]["z_variance"] = z_variance
        # print("Z-Mean:", z_mean, "Z-Variance:", z_variance)

        self.lengths.clear()
        self.subtours.clear()

    def write_data_to_json(self, filepath):
        load_write.write_json(self.data, filepath)

    def write_data_to_latex_table(self, filepath):
        table = latex.dict_to_latex_table(self.data,
                                          exclude_columns=["length_values", "subtour_values", "z_values"])
        load_write.write_txt(table, filepath)
