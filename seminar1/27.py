#27. Определить количество цифр в числе

number = int(input("Enter the number: "))

def amount(num):
    i = 1
    if num < 0:
        num *= -1
    while (int(num / 10)) > 0:
        num /= 10
        i += 1
    return i

print(amount(number))