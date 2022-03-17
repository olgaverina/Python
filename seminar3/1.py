#1. Сформировать список из  N членов последовательности.

num = int(input("Enter the number>> "))

array = []

def fill_array(arr, n):
    for i in range(0, n):
        arr.append(i)
    return arr

print(fill_array(array, num))

