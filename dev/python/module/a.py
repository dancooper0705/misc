import sys
import dcstat

def main():
    sample = dcstat.sample()
    for i in range(30):
        sample.add_element(i)
    print(sample.mean())
    print(sample.variance())
    print(sample.deviation())
    print(sample.mean_confidence_interval(90))

if __name__ == "__main__":
    main()
