from is_perfect import is_perfect

n = input("Enter n: ")
n = int(n)

start = 6
counter = 0

while True:
    if is_perfect(start):
        print(start)
        counter += 1
    if counter == n:
        break
    start += 1
