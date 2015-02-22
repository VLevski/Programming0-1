p = input("Enter p: ")
p = int(p)

twins = [p-2, p, p+2]
is_it = []

for twin in twins:
    start = 2
    prime = True

    if twin == 1:
        prime = False

    while start < twin:
        if twin % start == 0:
            prime = False
            break
        start += 1

    is_it += [prime]

if not is_it[1]:
    print(p, "ïs not prime.")
elif False in is_it:
    print(p, "is prime but:")
    if is_it[0]:
        print(twins[0], "is also prime") # p = 61
    else:
        print(twins[0], "is not")
    if is_it[2]:
        print(twins[2], "is also prime") # p = 59
    else:
        print(twins[2], "is not")
else:
    print("Twin primes with {}:".format(p))
    print("{}, {}".format(twins[0], p))
    print("{}, {}".format(p, twins[2]))
    
