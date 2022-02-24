# 6. Выяснить является ли число чётным
number = int(input('Enter the number:'))

if number % 2 == 0:
    print(f'Entered number {number} is even')
else:
    print(f'Entered number {number} is odd')