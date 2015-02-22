n = input("Enter a number: ")
n = int(n)

n_bit = n
n_new = str(0)

while n_bit != 0:
    n_new += str(n_bit % 10)
    n_bit //= 10
n_new = int(n_new)
print(n_new)
    
