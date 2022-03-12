#16. Дано число обозначающее день недели. 
# Выяснить является номер дня недели выходным

import random

num = random.randint(1,7)
print(num)
print('Будни' if num < 6 else 'Выходной')