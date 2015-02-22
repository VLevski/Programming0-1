n = input("Enter firs number: ")
m = input("Enter second number: ")
n = int(n)
m = int(m)

if n % 10 > m % 10:
    print("The result is: " + str(n))
elif n % 10 < m % 10:
    print("The result is: " + str(m))
else:
    if n > m:
        print("The result is: " + str(n))
    elif n == m:
        print("Tie Numbers {} = {}".format(n, m))
    else:
        print("The result is: " + str(m))
