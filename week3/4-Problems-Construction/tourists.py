# return the difference of the sums of the numbers in two lists - f(list, list) = int

def weight_difference(a, b):
    sum_a = 0
    sum_b = 0

    for number in a:
        sum_a += number

    for number in b:
        sum_b += number

    return sum_a - sum_b

# returns True if the firs argument's list is on turn to accept a new member - f(list, list) = boolean

def will_go(a, b):
    dif_in_weight = weight_difference(a, b)
    more_members = len(a) - len(b)

    if more_members < 0 or ( more_members == 0 and dif_in_weight < 0):
        return True
    else:
        return False

# return an index of number from a list, that is closest to the argument - f(int, list) = int

def closest(n, list_weights):
    index = 0
    space_index = 0
    space = list_weights[index] - n
    if space < 0:
        space *= -1

    for weight in list_weights:
        new_space = weight - n
        if new_space < 0:
            new_space *= -1
        if new_space < space:
            space = new_space
            space_index = index
        index += 1

    return space_index
    

# delete specified member of a list - f(int, list) = list

def del_list(index, old_list):
    old_list[index] = 0
    new_list = []

    for member in old_list:
        if member != 0:
            new_list += [member]

    return new_list

# return the index of the biggest if n=True or smallest if n=False number from list - f(list, init) = int

def max_min(a, n):
    index = 0
    index_number = 0
    number = a[index]

    if n:
        for member in a:
            if member > number:
                number = member
                index_number = index
            index += 1
    else:
        for member in a:
            if member < number:
                number = member
                index_number = index
            index += 1

    return index_number

def main():
# for skiping manual input while testing diferent algorithms
#    names = ["Katya", "Nina", "Petya", "Didi", "Petko", "Doncho", "Nikola", "Krasio",
#             "Bojo", "Ilia", "Dobri", "Botio",  "Bojana", "Leila", "Snejana", "Kremena",
#             "Nadja", "Sasho", "Yuri", "Desi", "Lili", "Pancho", "Kosyo"]
#    weights = [11, 14, 17, 13, 89, 74, 86, 88, 78, 74, 94, 92, 37, 29, 36, 24, 49, 18, 60, 75, 89, 107, 119]

    lo_weight = 10
    hi_weight = 120
    tourist_no = 1
    names = []
    weights = []
    print("When you wont to finish type 'end' when prompt for a tourist name.")

    while True:
        name = input("Enter a tourist name #{}: ".format(tourist_no))
        if name == "end":
            break
        weight = input("Enter a tourist #{} weight: ".format(tourist_no))
        weight = int(weight)
        if weight < lo_weight or weight > hi_weight:
            print("The weight must be between {}kg. - {}kg.! Enter next tourist.".format(lo_weight, hi_weight))
        else:
            names += [name]
            weights += [weight]
            tourist_no += 1

    weights_left = weights
    names_left = names
    weights_a = []
    names_a = []
    weights_b = []
    names_b = []

    while True:
        destination = will_go(weights_a, weights_b)
        
        current_weight_difference = weight_difference(weights_a, weights_b)
        if current_weight_difference < 0:
            current_weight_difference *= -1
        index_current_smallest = max_min(weights_left, False)
        current_smallest = weights_left[index_current_smallest]

        if current_weight_difference < current_smallest:
            index_current_biggest = max_min(weights_left, True)
            current_biggest_weight = weights_left[index_current_biggest]
            current_biggest_weight_name = names_left[index_current_biggest]

            if destination:
                weights_a += [current_biggest_weight]
                names_a += [current_biggest_weight_name]
            else:
                weights_b += [current_biggest_weight]
                names_b += [current_biggest_weight_name]

            weights_left = del_list(index_current_biggest, weights_left)
            names_left = del_list(index_current_biggest, names_left)

        else:
            index_current_closest = closest(current_weight_difference, weights_left)
            current_closest_weight = weights_left[index_current_closest]
            current_closest_weight_name = names_left[index_current_closest]
            
            if destination:
                weights_a += [current_closest_weight]
                names_a += [current_closest_weight_name]
            else:
                weights_b += [current_closest_weight]
                names_b += [current_closest_weight_name]

            weights_left = del_list(index_current_closest, weights_left)
            names_left = del_list(index_current_closest, names_left)

        if len(weights_left) == 0:
            break

    print("Group A are:")
    index = 0
    total_weight_a = 0
    
    for name in names_a:
        print("#{} - {} - {}kg.".format(index + 1, name, weights_a[index]))
        total_weight_a += weights_a[index]
        index += 1

    print("====\nTotal weight of group A is:", total_weight_a)
    print("\nGroup B are:")

    index = 0
    total_weight_b = 0

    for name in names_b:
        print("#{} - {} - {}kg.".format(index + 1, name, weights_b[index]))
        total_weight_b += weights_b[index]
        index += 1

    print("====\nTotal weight of group B is:", total_weight_b)

if __name__ == "__main__":
    main()
