# 8. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

import random

num = int(input("Enter the number: "))

array = []
rand_array = []

def n_reversed(arr, n): #Задать список из N элементов, заполненных числами из [-N, N]
    for i in range(0, n):
        arr.append(random.randint(-n, n))
    return arr

array = n_reversed(array, num)
print(array)

def create_custom_arr(n): #Задать позиции элементов, которые генерятся рандомно
    rand_arr = []
    for i in range(0, n):
        rand_arr.append(str(random.randint(0, n-1)))
    return rand_arr

element_positions = create_custom_arr(num)
print(f'Elements positions: {element_positions}')

def create_file(elements, n):
    data = open('file.txt', 'w') #a - данные дозаписались
    for e in elements:
        data.writelines(f'{str(e)}\n')
        #print(f'element - {e}')
    data.close()

create_file(element_positions, num)

print()

def read_file(arr):
    prod = 1
    data = open('file.txt', 'r')
    for i in data:
        print(i)
        prod *= arr[int(i)]
        print(arr[int(i)])
    data.close()
    return prod

print(f'sum = {read_file(array)}')
