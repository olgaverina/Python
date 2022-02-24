#21. Программа проверяет пятизначное число на палиндром.

import random

#random.randint(10000, 99999)
#print (num)

num = 34543
print('Палиндром' if ((int(num / 10000) == int(num % 10)) \
                    and (int(num / 1000 % 10) == int((num / 10) % 10))) \
                    else 'Не палиндром')
