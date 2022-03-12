#15. Дано число. Проверить кратно ли оно 7 и 23

import random

num = random.randint(160,165) #ищем 161

print(f'{num}','Кратно' if num % 7 == 0 and num % 23 == 0 else 'Не кратно')