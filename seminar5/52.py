# Дана последовательность чисел. Получить список неповторяющихся элементов 
# исходной последовательности. Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

lst = [1, 2, 3, 5, 1, 5, 3, 10] 
print(set(lst))             #{} -- set
print(list(set(lst)))       #[] -- list