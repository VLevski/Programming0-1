def fib(n):
    fib_list = []
    counter = 3
    
    if n == 1:
        fib_list = [1]
    if n >= 2:
        fib_list = [1, 1]

    while counter <= n:
        next_fib_number = fib_list[counter-3] + fib_list[counter-2]
        fib_list += [next_fib_number]
        counter += 1

    return fib_list

def add_n_to_number(num, n):
    numbers = []

    while n != 0:
        numbers += [n % 10]
        n //= 10

    index = len(numbers) - 1

    while index >= 0:
        num = num*10 + numbers[index]
        index -= 1

    return num
    

def fib_number(n):
    numbers = fib(n)
    fib_num = 0

    for number in numbers:
        fib_num = add_n_to_number(fib_num, number)

    return fib_num

        


    
