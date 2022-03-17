#33. Задать массив из 12 элементов, заполненных числами из [0,9]. 
# Найти сумму положительных/отрицательных элементов массива

import random

array = list()
def fill_array(arr):
    for i in range(0, 12):
        arr.append(random.randint(0,10))
        print(arr[i])
    return arr

array = fill_array(array)
print(array)

def sum_elem_arr(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

print(sum_elem_arr(array))