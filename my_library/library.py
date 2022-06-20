import random

array = []

def fill_array(arr):
    for i in range(1, 10):
        arr.append(random.randint(1,100))
    return(arr)