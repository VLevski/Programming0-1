n = input("Enter n: ")
n = int(n)

start = 1
num_del = []

while start < n:
    if n % start == 0:
        num_del += [start]
    start += 1

print("Divider of {} are: ".format(n))

for number in num_del:
    print(number)

index = 0
text = ""

while index < len(num_del):
    text += str(num_del[index])
    text += ", "
    index += 1

print("Divider of {} are:".format(n), text)
