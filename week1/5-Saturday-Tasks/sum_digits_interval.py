n = input("Enter N: ")
m = input("Enter M: ")
n = int(n)
m = int(m)

if n > m:
    start = m
    end = n
elif n < m:
    start = n
    end = m
else:
    start = n
    end = m
    print("Hint: Try with diferent numbers ;)")

while start <= end:
    current_number = start
    sum_dig = 0
    while current_number != 0:
        sum_dig = sum_dig + current_number % 10
        current_number //= 10
    print("Sum of digit of {} = {}".format(start, sum_dig))
    start += 1   
    


