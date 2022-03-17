#35. Определить, присутствует ли в заданном массиве, некоторое число

import random

num = int(input("Enter the number less than 10: "))

array = list()

def fill_array(arr):
    new_arr = list()
    for i in range(0,20):
        new_arr = arr.append(random.randint(0,10))
    return new_arr

array = fill_array(array)

def find_num(arr, n):
    if n in arr:
        print(f'{n} is in array')

find_num(array, num)