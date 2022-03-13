#24. Найти кубы чисел от 1 до N

num = int(input('Enter N: '))

#first option
def cube_1(n):
    res = 0
    line = ''
    for i in range(1, n+1):
        res = i**3
        line += str(i) + ' - ' + str(res) + '; '
    return line

print(cube_1(num))

#second_option
def cube_2(num):
    return [n**3 for n in range(1, num + 1)]

print(cube_2(num))