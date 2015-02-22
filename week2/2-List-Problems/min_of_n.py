n = input("Enter n: ")
n = int(n)

start = 1
numbers = []

while start <= n:
    number = input("Enter a number: ")
    number = int(number)
    numbers += [number]
    start += 1

min_number = numbers[0]

for number in numbers:
    if number < min_number:
        min_number = number

print("The smalest number is:", min_number)
