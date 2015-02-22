a = input("Enter a: ")
b = input("Enter b: ")
a = int(a)
b = int(b)

if a > b:
	n = b
	N = a
elif a < b:
	n = a
	N = b
else:
	n = 1
	N = 0
	print("Numbers should be different!")

while n <= N:
	print(n)
	n += 1		
