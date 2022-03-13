#28. Подсчитать сумму цифр в числе

# for x in range(10):
#     print(x, end = " ")

number = list(input("Enter the number: "))

print(number)

def sum(num):
    sum = 0
    for n in num:
        if not (n == '-' or n == '.' or n == ','):
            sum += int(n)
    return sum

print(sum(number))