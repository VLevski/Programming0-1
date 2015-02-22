a = input("Enter a: ")
b = input("Enter b: ")
a = int(a)
b = int(b)
oper = input("Enter Operator: ")
if oper == "+":
	sum = a + b
	print("Result is: {}".format(sum))
elif oper == "-":
	dif = a - b
	print("Result is: {}".format(dif))
elif oper == "*":
	product = a * b
	print("Result is: {}".format(product))
elif oper == "/":
	quotient = a / b
	print("Result is: {}".format(quotient))
else:
	print("You Have Entered Unsupported Operator!")