#34. Написать программу замену элементов массива на противоположные

import random

array = list()

def fill_array(arr):
    for i in range(0,10):
        arr.append(random.randint(0, 100))
    return arr

print(fill_array(array))

def reverse_array(arr):
    new_arr = list()
    for i in arr:
        new_arr.append(i*(-1))
    return new_arr

print(reverse_array(array))