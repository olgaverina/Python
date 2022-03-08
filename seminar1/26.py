#26. Возведите число А в натуральную степень B используя цикл

a = 5
b = 3

def square(m, n):
    sum = 1
    while (n > 0):
        sum *= m
        n -= 1
    return sum

print (square(a, b))