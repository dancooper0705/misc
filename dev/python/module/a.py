import math
import scipy.stats

def confidence_interval_of_population_mean(sample_size, sample_mean, sample_standard_deviation, confidence_level):
    mean = sample_mean
    standard_deviation = sample_standard_deviation / math.sqrt(sample_size)
    confidence_coefficient = confidence_level / 100
    alpha_level = 1 - confidence_coefficient
    tail_area = alpha_level / 2
    z_score = scipy.stats.norm.ppf(1 - tail_area)
    return [mean - z_score * standard_deviation, mean + z_score * standard_deviation]

def main():
    print('90% confidence interval for population mean: ' + str(confidence_interval_of_population_mean(50, 32, 6, 90)))
    print('95% confidence interval for population mean: ' + str(confidence_interval_of_population_mean(50, 32, 6, 95)))
    print('990% confidence interval for population mean: ' + str(confidence_interval_of_population_mean(50, 32, 6, 99)))

if __name__ == "__main__":
    main()
