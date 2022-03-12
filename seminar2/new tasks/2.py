# Задача 2
# Задать положительное вещественное число m = 2,35. Cоставить целое число n из цифр   123,45

# десятков 2 и сотых m 5 = 25
# единиц 3 и сотых m 5 = 35
# сотен 1 и десятых m 4 = 14 

from ssl import SO_TYPE


number = 123.45

sotni = int(number/100%10)
print('Сотни - ', sotni)
decyatki = int(number/10%10)
print('Десятки - ', decyatki)
edinitsy = int(number%10)
print('Единицы - ', edinitsy)

desyatye = int(number*10%10)
print('Десятые - ', desyatye)
sotye = int(number*100%10)  #123,45
print('Сотые - ', sotye)


#1 десятков 2 и сотых m 5 = 25
print(decyatki * 10 + sotye)
#2 единиц 3 и сотых m 5 = 35
print(edinitsy * 10 + sotye)
#3 сотен 1 и десятых m 4 = 14 
print(sotni * 10 + desyatye)