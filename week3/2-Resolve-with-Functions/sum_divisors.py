from divisors import divisors

def sum_ints(numbers):
    sum_numbers = 0

    for number in numbers:
        sum_numbers += number

    return sum_numbers

def main():
    n = input("Enter n: ")
    n = int(n)

    sum_divisors = sum_ints(divisors(n))

    print(sum_divisors)

if __name__ == "__main__":
    main()
    
