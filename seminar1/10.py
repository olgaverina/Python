# 10. Показать вторую цифру трёхзначного числа

number = int(input('Enter the number:'))

print(int(number / 10 % 10))
print(number // 10 % 10)