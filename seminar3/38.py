38. #Реализовать алгоритм перемешивания списка.
import random
from random import randint

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 13]

count = len(array)
while count >= 0:
    rand = random.choice(array)
    rand_index = array.index(rand)
    array.pop(rand_index)
    array.append(rand)
    count -= 1
print(array)

