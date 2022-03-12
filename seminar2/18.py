#18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
x = bool
y = bool


z = (not(x or y)) == (not x and not y)
print (f'x - {x}, y - {y}, z - {z}')