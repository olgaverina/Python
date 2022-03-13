#26. Возведите число А в натуральную степень B используя цикл

a = 3
b = 5

def square_1(m, n):
    sum = 1
    while (n > 0):
        sum *= m
        n -= 1
    return sum

print(square_1(a, b))

def square_2(m, n):
    sum = 1
    for i in range (n):
        sum *= m
    return sum

print(square_2(a, b))