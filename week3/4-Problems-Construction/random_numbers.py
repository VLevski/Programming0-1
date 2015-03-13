def generate_random_list(n, start, end):
    from random import randint
    counter = 1
    random_list = []

    while counter <= n:
        random_list += [randint(start, end)]
        counter += 1

    return random_list
