#32. Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран

array = list()
print(type(array))
print(array)
for i in array:
    print(i)

for i in range(0, 4):
    array.append(0)
    array.append(1)

for i in array:
    print(i)

print(array)
print(len(array))
