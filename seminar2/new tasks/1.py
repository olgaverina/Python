# Задача 1
# Подсчитать количество натуральных чисел, не превосходящих заданного числа n, которые

# делятся на k, но не на l
# делятся хотябы на k или на l
# не делятся на (k + l)

number = int(input('Enter the number:'))

k = 3
l = 2

def divide_k_not_l(number, k, l):
    count = 0
    for i in range(1, number + 1):
        if i % k == 0 and i % l != 0:
            count += 1
    return count

print(divide_k_not_l(number, k, l))

def divide_k_or_l(number, k, l):
    count = 0
    for i in range(1, number + 1):
        if i % k == 0 or i % l != 0:
            count += 1
    return count

print(divide_k_or_l(number, k, l))

def divide_nor_k_plus_l(number, k, l):
    count = 0
    for i in range(1, number + 1):
        if i % (k + l) != 0:
            count += 1
    return count

print(divide_nor_k_plus_l(number, k, l))