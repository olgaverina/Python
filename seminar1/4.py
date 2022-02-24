# 4. Найти максимальное из трех чисел
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
third_number = int(input('Enter the third number: '))

if first_number > second_number > third_number:
    print(f'Maximum is the {first_number}')
elif second_number > first_number > third_number:
    print(f'Maximum is the {second_number}')
else:
    print(f'Maximum is the {third_number}')