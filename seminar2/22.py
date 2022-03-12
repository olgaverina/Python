#22. Найти расстояние между точками в пространстве 2D/3D

from math import sqrt
import random

#2D

def two_d(x1, y1, x2, y2):
    return(float(sqrt(((x2 - x1)**2)+((y2-y1)**2))))

print(two_d(random.randint(-10,10), random.randint(-10,10), random.randint(-10,10), random.randint(-10,10)))

#3D

def three_d(x1, y1, z1, x2, y2, z2):
    return(float(sqrt((x2 - x1)**2 + (y2-y1)**2+(z2-z1)**2)))

print(three_d(random.randint(-10,10), random.randint(-10,10), random.randint(-10,10), random.randint(-10,10), random.randint(-10,10), random.randint(-10,10)))

