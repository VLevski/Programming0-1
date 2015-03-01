from prime_digit import is_prime

p = input("Enter p: ")
p = int(p)
q = p - 2
r = p + 2

is_p = is_prime(p)
is_q = is_prime(q)
is_r = is_prime(r)

if not is_p:
    print(p, "is not prime")
elif is_q or is_r: # such in case p = 41 or 43
    print("Twin primes with", p)
    if is_q:
        print("{}, {}".format(q, p))
    if is_r:
        print("{}, {}".format(p, r))
else:
    print("{} is prime, but {} and {} are not!".format(p, q, r))
