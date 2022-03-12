# 12. Удалить вторую цифру трёхзначного числа

number = int((input('Enter the number: ')))

print('The new number is', int(number/100), int(number%10))
print()
print(f'The new number is {number//100}{int(number%10)}')