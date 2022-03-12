#23. Показать таблицу квадратов чисел от 1 до N

num = int(input('Enter N: '))

def square(n):
    line = ''
    res = 0
    for i in range(1, n+1):
        line += '\n'
        for j in range(1, 11):
            res = i * j
            line += str(res) + ' '
    line += '\n'
    return line

print(square(num))