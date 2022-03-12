#28. Подсчитать сумму цифр в числе

# for x in range(10):
#     print(x, end = ",")

number = int(input("Enter the number: "))

def sum(n):
    if n < 0:
        n *= -1
    s = 0
    while int(n) > 0:
        s += int(n % 10)
        n /= 10
    return s

print(sum(number))