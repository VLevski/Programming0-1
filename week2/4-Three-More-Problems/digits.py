n = input("Enter n: ")
n = int(n)

numbers = []
start = n

while start != 0:
    numbers = [start % 10] + numbers
    start //= 10

print(numbers)

N = 0

for number in numbers:
    N = N * 10 + number

print(N)

