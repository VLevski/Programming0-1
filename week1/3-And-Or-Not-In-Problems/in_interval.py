a = input("Enter The Beginning of Interval: ")
b = input("Enter The End of Interval: ")
x = input("Enter a Number: ")
a = int(a)
b = int(b)
x = int(x)

if x == a:
	print("The number is equal to the lower bound of the interval")
elif x == b:
	print("The number is equal to the upper bound of the interval")
elif x > a and x < b:
	print("The number is in the interval")
elif x < a:
	print("The number is outside the interval, {} < {}".format(x, a))
else:
	print("The number is outside the interval, {} > {}".format(x, b))