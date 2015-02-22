n = input("Enter n: ")
n = int(n)

start = 1
num_div = []

while start < n:
    if n % start == 0:
        num_div += [start]
    start += 1

sum_div = 0

for number in num_div:
    sum_div += number

if n == sum_div:
    print("The number of {} is Perfect!".format(n))
else:
    print("The number of {} is not Perfect!".format(n))
