n = input("Enter n: ")
n = int(n)

N = 6
num_perfect = 0

while True:
    start = 1
    num_div = []

    while start < N:
        if N % start == 0:
            num_div += [start]
        start += 1

    sum_div = 0

    for number in num_div:
        sum_div += number

    if N == sum_div:
        print(N)
        num_perfect += 1

    if num_perfect == n:
        break

    N += 1
