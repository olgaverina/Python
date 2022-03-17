#9. Реализовать алгоритм перемешивания списка.
import random
array = []

def fill_array(arr):
    for i in range(1, 10):
        arr.append(random.randint(1,100))
    return(arr)

def copy_array(arr):
    new_arr = []
    for i in range(0, len(arr)):
        new_arr.append(arr[i])
    return new_arr

def mix_array(arr, new_arr):
    for i in range(0, len(arr)):
        arr[i] = new_arr[i-1]
    return arr

print(fill_array(array))
new_array = copy_array(array)
print(new_array)
print(mix_array(array, new_array))

