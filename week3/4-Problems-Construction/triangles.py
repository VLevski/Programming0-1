def is_triangle(a, b, c):
    sides = [a, b, c]
    sides = sorted(sides)
    condition_1 = False
    condition_2 = False
    condition_3 = False

    if (sides[2] - sides[1]) < sides[0] and sides[0] < (sides[2] + sides[1]):
        condition_1 = True
    if (sides[2] - sides[0]) < sides[1] and sides[1] < (sides[2] + sides[0]):
        condition_2 = True
    if (sides[1] - sides[0]) < sides[2] and sides[2] < (sides[1] + sides[0]):
        condition_3 = True

    return condition_1 and condition_2 and condition_3

def area(a, b, c):
    from math import sqrt
    p = (a + b + c)/2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return s

def is_pythagorean(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

def max_area(triangles):
    s_max = 0
    triangle_index = 0
    
    for element in triangles:
        a = element[0]
        b = element[1]
        c = element[2]
        if is_triangle(a, b, c):
            s = area(a, b, c)
            if s > s_max:
                s_max = s
                biggest_triangle_index = triangle_index
        triangle_index += 1    
                    
    return triangles[biggest_triangle_index]

