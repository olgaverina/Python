# 12. Удалить вторую цифру трёхзначного числа

number = int((input('Enter the number: ')))

print(f'The new number is {number//100 * 10 + int(number%10)}')

