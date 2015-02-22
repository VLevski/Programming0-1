n = input("Enter Number: ")
n = int(n)

parity = n % 2
if parity == 0:
	print(str(n) + " is even number")
else:
	print(str(n) + " is odd number")
