import sys
import dcstat

def main():
    sample = dcstat.sample()
    print(sample.confidence_interval_of_mean(90, 50, 32, 6))
    print(sample.confidence_interval_of_mean(95, 50, 32, 6))
    print(sample.confidence_interval_of_mean(99, 50, 32, 6))

if __name__ == "__main__":
    main()
