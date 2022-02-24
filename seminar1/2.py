# 2. Даны два числа. Показать большее и меньшее число

first_number = int(input('Enter the first number:'))
second_number = int(input('Enter the second number:'))

if first_number > second_number:
    print(f'Maximum is the first number {first_number}, minumum is the second number {second_number}')
elif second_number > first_number:
    print(f'Maximum is the second number {second_number}, minimum is the first number {first_number}')
else:
    print('The numbers are equal')