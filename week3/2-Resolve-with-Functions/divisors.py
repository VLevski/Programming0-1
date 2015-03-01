def divisors(n):
    start = 1
    divs = []

    while start < n:
        if n % start == 0:
            divs += [start]
        start += 1

    return divs

def main():
    n = input("Enter n: ")
    n = int(n)

    for number in divisors(n):
        print(number)
        
if __name__ == "__main__":
    main()
