n = input("Enter n: ")
n = int(n)

start = 1
even = []

while start <= n:
    number = input("Enter a number: ")
    number = int(number)
    if number % 2 == 0:
        even = even + [number]
    start += 1

print("Count of evens: " + str(len(even)))
print("Evens are:")

for number in even:
    print(number)
    
