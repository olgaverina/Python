#5. Подсчитать сумму цифр в вещественном числе.

num = (input("Enter the number >>"))

def count_n(number):
    count = 0
    for n in number:
        if n != '.' and n != ',':
            count += 1
    return count

print(count_n(num))