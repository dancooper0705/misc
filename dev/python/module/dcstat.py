import math

class sample:
    arr = []

    def __init__(self):
        pass

    def add_element(self, val):
        self.arr.append(val)

    def mean(self):
        total = 0
        for a in self.arr:
            total += a
        avg = total / len(self.arr)
        return avg

    def count(self):
        return len(self.arr)

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

    def deviation(self):
        return math.sqrt(self.variance())

    def mean_confidence_interval(self, confidence_level):
        mean = self.mean)
        deviation = self.deviation() / math.sqrt(self.count())
        z_critial_value = 0
        if confidence_level == 80:
            alpha = 0.1
            z_critical_value = 1.28
        elif confidence_level == 90:
            alpha = 0.05
            z_critical_value = 1.645
        elif confidence_level == 95:
            alpha = 0.025
            z_critical_value = 1.96
        elif confidence_level == 98:
            alpha = 0.001
            z_critical_value = 2.33
        elif confidence_level == 99:
            alpha = 0.0005
            z_critical_value = 2.58
        return [mean - z_critical_value * deviation, mean + z_critical_value * deviation]
