# 4. Пользователь задаёт две строки. 
# Определить количество вхождений одной строки в другой.

s1 = "wgsdhfgfggkhfg"
s2 = "fg"

count = 0
if s1.split(s2):
    print(s1)
    count += 1

print(count)