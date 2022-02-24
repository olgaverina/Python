# 14. Найти третью цифру числа или сообщить, что её нет

number = int(input('Enter the number:'))

if number // 100 > 0:
    print (int(number / 100 % 10))
else:
    print ('The third letter does not exists')

