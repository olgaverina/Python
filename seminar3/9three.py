#9. Реализовать алгоритм перемешивания списка.

# import sys
# sys.path.append('/Users/ayugazin/Desktop/GB/Python/my_library')
# from library import fill_array as fill

from library import fill_array as fill
import random

array = []
print(fill(array))
random.shuffle(array)
print(array)
