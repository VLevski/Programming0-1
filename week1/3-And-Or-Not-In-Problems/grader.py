n = input("Enter Test Result: (0-100) ")
n = int(n)

if n >= 0 and n <= 50:
	print("Слаб 2")
elif n >= 51 and n <= 60:
	print("Среден 3")
elif n >= 61 and n <= 70:
	print("Добър 4")
elif n >= 71 and n <= 80:
	print("Много Добър 5")
elif n >= 81 and n <= 99:
	print("Отличен 6")
elif n == 100:
	print("Много Отличен 7")
else:
	print("Test Result Should be in interval 1 to 100")