n = 1
N = 10

while n != 0:
	if n >= 1 and n <= N:
		print(n)
		n += 1
	elif n == N + 1:
		print("====")
		n = -N
	elif n >= -N and n < 0:
		print(-n)
		n += 1
		
