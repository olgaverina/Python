#9. Реализовать алгоритм перемешивания списка.
import random
array = []

def fill_array(arr):
    for i in range(1, 10):
        arr.append(random.randint(1,100))
    return(arr)


def mix_array(arr):
    for i in range(0, len(arr)):
        arr[i] = arr.insert(i-1, arr.pop(i))
    return arr

print(fill_array(array))
print(mix_array(array))
