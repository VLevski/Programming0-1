n = input("Enter 3 digit Number: ")
n = int(n)

n_chek = n
N = 0
while n_chek != 0:
    n_chek //= 10
    N += 1
if N != 3:
    print("You Have to enter 3 digit number!")
else:
    a = n % 10
    b = (n // 10) % 10
    c = (n // 100) % 10

    if a >= b and a >= c:
        max_dig = a
        if b >= c:
            mid_dig = b
            min_dig = c
        else:
            mid_dig = c
            min_dig = b
    elif b >= a and b >= c:
        max_dig = b
        if a >= c:
            mid_dig = a
            min_dig = c
        else:
            mid_dig = c
            min_dig = a
    elif c >= a and c >= b:
        max_dig = c
        if a >= b:
            mid_dig = a
            min_dig = b
        else:
            mid_dig = b
            min_dig = a

    hi_dig = max_dig*100 + mid_dig*10 + min_dig
    lo_dig = min_dig*100 + mid_dig*10 + max_dig

    print("The higest number is: " + str(hi_dig))
    print("The lowest number is: " + str(lo_dig))
