n = input("Enter n: ")
n = int(n)

start = 1
numbers = []

while start <= n:
    number = input("Enter a number: ")
    number = int(number)
    numbers = numbers + [number]
    start += 1

sum_number = 0

for number in numbers:
    sum_number += number

print("The sum is: " + str(sum_number))
