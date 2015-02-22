n = input("Enter n: ")
n = int(n)

start = 1
numbers = []

while start <= n:
    number = input("Enter a number: ")
    number = int(number)
    numbers += [number]
    start += 1

sum_of_numbers = 0

for number in numbers:
    sum_of_numbers += number

avg_of_numbers = sum_of_numbers / len(numbers)

# или:
# avg_of_numbers = sum_of_numbers / n

print("Average of numbers is", avg_of_numbers)
