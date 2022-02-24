# 1. По двум заданным числам проверять является ли первое квадратом второго

first_number = int(input('Enter the first number:'))
second_number = int(input('Enter the second number:'))

if first_number == second_number**2:
    print(f'The first number {first_number} is a square of the second number {second_number}')
else:
    print(f'The first number {first_number} IS NOT a square of the second number {second_number}')
