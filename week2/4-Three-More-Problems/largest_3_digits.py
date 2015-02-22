n = input("Enter n: ")
n = int(n)

start = n
numbers = []

while start != 0:
    digit = start % 10
    numbers += [digit]
    start //= 10

numbers_min = sorted(numbers)
numbers_max = sorted(numbers, reverse=True)

max_number = 0

for number in numbers_max:
    max_number = max_number * 10 + number

min_number = 0

for number in numbers_min:
    min_number = min_number * 10 + number

print("The biggest number is:", max_number)
print("The smallest number is:", min_number)

    
    
    
    
