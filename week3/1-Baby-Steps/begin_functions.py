def square(a):
    return a ** 2

def fact(n):
    start = 1
    f = 1

    while start <= n:
        f *= start
        start += 1

    return f

def count_elements(a):
    count = 0

    for element in a:
        count += 1

    return count

def member(x, xs):
    is_it = False

    for element in xs:
        if x == element:
            is_it = True
            return is_it

    return is_it

def grades_that_pass(students, grades, limit):
    index = 0
    passed = []

    for grade in grades:
        if grade > limit:
            passed += [students[index]]
        index += 1

    return passed
