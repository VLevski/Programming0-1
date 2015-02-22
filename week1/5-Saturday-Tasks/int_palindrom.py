n = input("Enter a Number: ")
n = int(n)

N = n
n_p = 0

while N != 0:
    last_digit = N % 10
    n_p = n_p * 10 + last_digit
    N //= 10

if n == n_p:
    print("The number is palindrom")
else:
    print("The number is not palindrom")
