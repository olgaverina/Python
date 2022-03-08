#25. Найти сумму чисел от 1 до А

num = int(input('Enter A: '))

def sum(n):
    return n*(1 + n)/2

print(int(sum(num)))