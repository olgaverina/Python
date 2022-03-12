#24. Найти кубы чисел от 1 до N

num = int(input('Enter N: '))

def cube(n):
    res = 0
    line = ''
    for i in range(1, n+1):
        res = i*i*i
        line += str(i) + ' - ' + str(res) + '; '
    return line

print(cube(num))