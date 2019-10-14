import math
import scipy.stats

class sample:
    population_variance = None
    arr = []

    def __init__(self):
        pass

    def add_element(self, val):
        self.arr.append(val)

    def size(self):
        return len(self.arr)

    def mean(self):
        total = 0
        for a in self.arr:
            total += a
        avg = total / len(self.arr)
        return avg

    def variance(self):
        ans = 0
        x = 0
        x2 = 0
        n = len(self.arr)
        for a in self.arr:
            x = x + a
            x2 = x2 + a ** 2
        ans = (x2 - x **2 / n) / (n - 1)
        return ans

    def standard_deviation(self):
        return math.sqrt(self.variance())

    def critical_value_of_z(self, tail_area):
        return scipy.stats.norm.ppf(1 - tail_area)

    def confidence_interval_of_population_mean(self, confidence_level, sample_size=None, sample_mean=None, sample_standard_deviation=None):
        if sample_size == None:
            sample_size = self.size()
            sample_mean = self.mean()
            sample_standard_deviation = self.standard_deviation()
        mean = sample_mean
        standard_deviation = sample_standard_deviation / math.sqrt(sample_size)
        confidence_coefficient = confidence_level / 100
        alpha_level = 1 - confidence_coefficient
        tail_area = alpha_level / 2
        z_score = self.critical_value_of_z(tail_area)
        return [mean - z_score * standard_deviation, mean + z_score * standard_deviation]

