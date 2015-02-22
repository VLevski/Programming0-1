n = input("Enter a number: ")
n = int(n)

if n > 1:
    start = 2
    end = n
else:
    start = n+1
    end = -1

prime = 1

while start < end and prime != 0:
    prime = n % start
    start += 1

if prime == 0:
    print("The number {} is prime!".format(n))
else:
    print("The number {} is not prime!".format(n))
