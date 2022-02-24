#20. Задать номер четверти, показать диапазоны для возможных координат

from json.encoder import INFINITY
import random
import math

num = random.randint(1,4)

def coordinates(n):
    if n == 1:
        print('x = from', 0, 'to', INFINITY, '; y = from', 0, 'to', INFINITY)
    elif n == 2:
        print('x = from', 0, 'to', INFINITY, '; y = from', 0, 'to', INFINITY)
    elif n == 3:
        print('x = from', 0, 'to', -INFINITY, '; y = from', 0, 'to', -INFINITY)
    else:
        print('x = from', 0, 'to', INFINITY, '; y = from', 0, 'to', -INFINITY)

print(num)
coordinates(num)