from divisors import divisors
from sum_divisors import sum_ints

def is_perfect(n):
    perfect = False

    if n == sum_ints(divisors(n)):
        perfect = True

    return perfect

def main():
    n = input("Enter n: ")
    n = int(n)

    if is_perfect(n):
        print(n, "is perfect")
    else:
        print(n, "is not perfect")

if __name__ == "__main__":
    main()
