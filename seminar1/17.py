#17. По двум заданным числам проверять является ли одно квадратом другого

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

print('Первое квадрат второго' if num1*num1 == num2 else 'Первое не квадрат второго')
print('Второе квадрат первого' if num2*num2 == num1 else 'Второе не квадрат первого')