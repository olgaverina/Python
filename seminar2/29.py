#29. Написать программу вычисления произведения чисел от 1 до N

number = int(input("Enter the number: "))

def product(num):
    if num < 0:
        num *= -1
    mult = 1
    for i in range(1, num + 1):
        mult *= i
    return mult

print(product(number))