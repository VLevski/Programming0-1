n = input("Enter n: ")
n = int(n)

N = n
numbers = []

while N != 0:
    number = N % 10
    numbers += [number]
    N //= 10

numbers_up = sorted(numbers)
numbers_down = sorted(numbers, reverse=True)

max_number = 0
min_number = 0

for number in numbers_down:
    max_number = max_number*10 + number

for number in numbers_up:
    min_number = min_number*10 + number

print("Largest:", max_number)
print("Smallest:", min_number)
