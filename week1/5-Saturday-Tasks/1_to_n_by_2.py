N = input("Enter a number: ")
N = int(N)
n = 1
steep = 2

if N > 1:
    while n <= N:
        print(n)
        n += steep
elif N < 0:
    while n >= N:
        print(n)
        n -= steep
else:
    print("Enter Bigger Number!")
        
