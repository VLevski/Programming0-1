def reverse_int(n):
    reverse_numbers = []
    reverse_number = 0

    while n != 0:
        reverse_numbers += [n % 10]
        n //= 10
        
    for number in reverse_numbers:
        reverse_number = reverse_number * 10 + number

    return reverse_number

def sum_digits(n):
    numbers = []
    sum_numbers = 0
    
    while n != 0:
        numbers += [n % 10]
        n //= 10
        
    for number in numbers:
        sum_numbers += number

    return sum_numbers

def product_digits(n):
    numbers = []
    product_numbers = 1

    while n != 0:
        numbers += [n % 10]
        n //= 10

    for number in numbers:
        product_numbers *= number

    return product_numbers

def digits(n, operand):
    numbers = []
    sum_numbers = 0
    product_numbers = 1

    while n != 0:
        numbers += [n % 10]
        n //= 10
    if operand:
        for number in numbers:
            sum_numbers += number
        return sum_numbers
    else:
        for number in numbers:
            product_numbers *= number
        return product_numbers
    
if __name__ == "__main__":
    n = input("Enter a number: ")
    n = int(n)

    print("Reverset number is:", reverse_int(n))
    print("Sum of number's digits is:", digits(n, 1))
    print("Product of number's digits is:", digits(n, 0))
