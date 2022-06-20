# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

k = int(input("Enter the number: "))
coefficients = []

for i in range(0, k+1):
    coefficients.append(randint(0, 100))

print(coefficients)

def input_k(k):
    k -= 1
    return str(k)
res = ""
for i in coefficients:
    res += str(i)
    if (k == 0):
        break
    res += "*"
    res += "x"
    res += "ˆ"
    res += input_k(k+1)
    res += " + "
    k -= 1
print(res)