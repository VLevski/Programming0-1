N = input("Entr a number: ")
N = int(N)
n = 1
sum = 0
if N > n:
    while n <= N:
        sum = sum + n
        n += 1
else:
    while n >= N:
        sum = sum + n
        n -= 1

print("The Sum is: " + str(sum))
