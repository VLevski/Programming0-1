N = input("Enter a Number: ")
N = int(N)
sum = 0
n = 1

if N > n:
    while n <= N:
        if n % 2 != 0:
            sum += n
        n += 1
elif N < 0:
    while n >= N:
        if n % 2 != 0:
            sum += n
        n -= 1
else:
    print("Enter Bigger Number!")

print("The sum is: " + str(sum))
