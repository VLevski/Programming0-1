def is_prime(n):
    prime = True
    start = 2

    if n == 1:
        prime = False

    while start < n:
        if n % start == 0:
            prime = False
            break
        start += 1

    return prime

def to_digits(n):
    digits_list = []

    while n != 0:
        digits_list = [n % 10] + digits_list
        n //= 10

    return digits_list

def main():
    n = input("Enter n: ")
    n = int(n)

    digits = to_digits(n)
    prime = False
    
    for digit in digits:
        if is_prime(digit):
            print("Yes")
            prime = True
            break

    if not prime:
        print("No")

if __name__ == "__main__":
    main()
