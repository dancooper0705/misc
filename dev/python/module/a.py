import sys
import dcstat

def main():
    sample = dcstat.sample()
    for i in range(10):
        sample.add_element(i)
    print(sample.mean())
    print(sample.variance())

if __name__ == "__main__":
    main()
