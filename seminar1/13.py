#13. Выяснить, кратно ли число заданному, если нет, вывести остаток.

number1 = int((input('Enter the first number: ')))
number2 = int((input('Enter the second number: ')))

def check(n1, n2):
    return n1 if n1%n2 == 0 else int(n1%n2)

print(check(number1, number2))