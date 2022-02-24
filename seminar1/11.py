#11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

import random

number = random.randint(10,100)
print('Generated number:', number)
def max_digit(num):
    return int(max(num%10, num/10))
print('Max digit:', max_digit(number))