# 7. Показать числа от -N до N

number = int(input('Enter the number: '))

def negative_n_positive(num):
    str = ''
    for i in range(-num, num + 1):
        str += i + ' '
    return str
    
print(negative_n_positive(number))
