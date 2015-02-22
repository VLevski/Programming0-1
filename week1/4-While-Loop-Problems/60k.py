n = 1

while True:
	if n <= 60000:
		n += 1
	else:
		print("You have reached final destination of {} turns".format(n-1))
		break
