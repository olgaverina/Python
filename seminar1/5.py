# 5. Написать программу вычисления значения функции y = f(a) y = y в степени y

number = int(input('Enter the number: '))

def func(num):
    return num ** num

print(func(number))