import math
import scipy.stats

def confidence_interval_of_population_proportion(sample_size, sample_proportion, confidence_level):
    mean = sample_proportion
    standard_deviation = math.sqrt(sample_proportion * (1 - sample_proportion) / sample_size)
    confidence_coefficient = confidence_level / 100
    alpha_level = 1 - confidence_coefficient
    tail_area = alpha_level / 2
    z_score = scipy.stats.norm.ppf(1 - tail_area)
    return [mean - z_score * standard_deviation, mean + z_score * standard_deviation]

def confidence_interval_of_population_mean_with_normal_distribution(sample_size, sample_mean, sample_standard_deviation, confidence_level):
    mean = sample_mean
    standard_deviation = sample_standard_deviation / math.sqrt(sample_size)
    confidence_coefficient = confidence_level / 100
    alpha_level = 1 - confidence_coefficient
    tail_area = alpha_level / 2
    z_score = scipy.stats.norm.ppf(1 - tail_area)
    return [mean - z_score * standard_deviation, mean + z_score * standard_deviation]

def confidence_interval_of_population_mean_with_students_t_distribution(sample_size, sample_mean, sample_standard_deviation, confidence_level):
    mean = sample_mean
    standard_deviation = sample_standard_deviation / math.sqrt(sample_size)
    confidence_coefficient = confidence_level / 100
    alpha_level = 1 - confidence_coefficient
    tail_area = alpha_level / 2
    degree_freedom = sample_size - 1
    t_score = scipy.stats.t.ppf(1 - tail_area, degree_freedom)
    return [mean - t_score * standard_deviation, mean + t_score * standard_deviation]

def confidence_interval_of_population_mean(sample_size, sample_mean, sample_standard_deviation, confidence_level, is_population_standard_deviationi_known=False):
    if is_population_standard_deviationi_known == True or sample_size >= 30:
        return confidence_interval_of_population_mean_with_normal_distribution(sample_size, sample_mean, sample_standard_deviation, confidence_level)
    else:
        return confidence_interval_of_population_mean_with_students_t_distribution(sample_size, sample_mean, sample_standard_deviation, confidence_level)

class Sample:
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

    def confidence_interval_of_population_mean(self, confidence_level):
        sample_size = self.size()
        sample_mean = self.mean()
        sample_standard_deviation = self.standard_deviation()
        return confidence_interval_of_population_mean(sample_size, sample_mean, sample_standard_deviation, confidence_level)

def main():
    sample = Sample()
    ratings = [6, 4, 6, 8, 7, 7, 6, 3, 3, 8, 10, 4, 8, 7, 8, 7, 5, 9, 5, 8, 4, 3, 8, 5, 5, 4, 4, 4, 8, 4, 5, 6, 2, 5, 9, 9, 8, 4, 8, 9, 9, 5, 9, 7, 8, 3, 10, 8, 9, 6]
    sample = Sample()
    for a in ratings:
        sample.add_element(a)
    print('example1, sample size >= 30, use t-score to estimate confidence interval')
    print('sample.size(): ' + str(sample.size()))
    print('sample.mean(): ' + str(sample.mean()))
    print('sample.variance(): ' + str(sample.variance()))
    print('sample.standard_deviation(): ' + str(sample.standard_deviation()))
    print('90% confidence interval for population mean: ' + ' to '.join('{0:.2f}'.format(a) for a in sample.confidence_interval_of_population_mean(90)))
    print('95% confidence interval for population mean: ' + ' to '.join('{0:.2f}'.format(a) for a in sample.confidence_interval_of_population_mean(95)))
    print('99% confidence interval for population mean: ' + ' to '.join('{0:.2f}'.format(a) for a in sample.confidence_interval_of_population_mean(99)))
    print()

    print('example2, sample size < 30, use t-score to estimate confidence interval')
    sample_size = 20
    sample_mean = 17.25
    sample_standard_deviation = 3.3
    print('sample.size: ' + str(sample_size))
    print('sample.mean: ' + str(sample_mean))
    print('sample.standard_deviation: ' + str(sample_standard_deviation))
    print('90% confidence interval for population mean: ' + ' to '.join('{0:.2f}'.format(a) for a in confidence_interval_of_population_mean(sample_size, sample_mean, sample_standard_deviation, 90)))
    print('95% confidence interval for population mean: ' + ' to '.join('{0:.2f}'.format(a) for a in confidence_interval_of_population_mean(sample_size, sample_mean, sample_standard_deviation, 95)))
    print('99% confidence interval for population mean: ' + ' to '.join('{0:.2f}'.format(a) for a in confidence_interval_of_population_mean(sample_size, sample_mean, sample_standard_deviation, 99)))

    print('example3, p = sample proportion, n*p >= 5 && n*(1-p)>=5')
    sample_size = 800
    sample_proportion = 0.7
    print('sample_size: ' + str(sample_size))
    print('sample_proportion: ' + str(sample_proportion))
    print('90% confidence interval for population proportion: ' + ' to '.join('{0:.4f}'.format(a) for a in confidence_interval_of_population_proportion(sample_size, sample_proportion, 90)))
    print('95% confidence interval for population proportion: ' + ' to '.join('{0:.4f}'.format(a) for a in confidence_interval_of_population_proportion(sample_size, sample_proportion, 95)))

if __name__ == "__main__":
    main()
