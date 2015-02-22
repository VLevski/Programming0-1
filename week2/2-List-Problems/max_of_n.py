n = input("Enter n: ")
n = int(n)

start = 1
numbers = []

while start <= n:
    number = input("Enter a number: ")
    number = int(number)
    numbers += [number]
    start += 1

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print("Max is: " + str(max_number))
