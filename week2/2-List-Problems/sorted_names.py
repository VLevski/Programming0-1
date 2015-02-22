n = input("Enter n: ")
n = int(n)

start = 1
names = []
print("Enter {} names!".format(n))

while start <= n:
    name = input()
    names += [name]
    start += 1

print("Sorted names are:")

names_sorted = sorted(names)

for name in names_sorted:
    print(name)


