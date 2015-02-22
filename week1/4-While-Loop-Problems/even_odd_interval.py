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
	if a % 2 == 0:
		par = "even"
	else:
		par = "odd"
	print("You must enter different numbers!\nBy the way your number {} is {} number ;)".format(a, par))

while n <= N:
	if n % 2 == 0:
		print(str(n) + " - even")
	else:
		print(str(n) + " - odd")
	n += 1
