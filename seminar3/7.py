#7. Задать список из n чисел последовательности (1+1/n)ˆn и 
# вывести на экран их сумму

num = int(input("Enter the number>> "))

def sum_array(n):
    sum = 0
    for i in range(1,n+1):
        sum += ((1+1/i)**i)
    return sum
print(f"{sum_array(num)} сумма")

def cool_dict(n):
    return {i: ((1 + 1/i)**i) for i in range(1, n)}
print(f"{cool_dict(num)} словарь")

def cool_list(n):
    return [((1 + 1/i)**i) for i in range(1, n)]
print(f"{cool_list(num)} список")
