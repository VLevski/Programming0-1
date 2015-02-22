n = input("Enter a number: ")
n = int(n)

n_f = 1

if n > 0 :
    start = 1
    end = n
elif n < 0:
    start = n
    end = -1
else:
    start = 2
    end = 1

while start <= end:
    n_f *= start
    start += 1

print("The result of {}! is: {}".format(n, n_f))
