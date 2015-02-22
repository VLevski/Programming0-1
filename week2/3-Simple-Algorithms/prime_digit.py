n = input("Enter n: ")
n = int(n)

prime = False
prime_dig = [2, 3, 5, 7]
N = n

while N != 0:
    digit = N % 10
    if digit in prime_dig:
        prime = True
        break
    N //= 10

if prime:
    print("Yes")
else:
    print("No")

    
