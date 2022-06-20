#Для натурального n создать словарь индекс-значение, 
#состоящий из элементов последовательности 3n + 1.
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num = 6
dict = {}
digits_key = []
digits_value = []

for d in range(1, num+1):           #делаю список с ключами
    digits_key.append(d)
print (digits_key)

for d in range(1, num+1):           #делаю список со значениями
    digits_value.append(d*3 + 1)
print (digits_value)

for i in range(0, len(digits_key)):     #собираю их в массив
    dict[digits_key[i]] = digits_value[i]

print(dict)

#or

dict = {}
for k in range(1,num+1):
    dict[k] = 3*k + 1
print(dict)