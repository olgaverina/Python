#Задать список из n чисел последовательности (1+1/n)ˆn 
# и вывести на экран их сумму

n = 10
arr = []

def create_dict(num):
    return {i: ((1+ (1/i))**i) for i in range(1, num+1)}

def create_list(num):
    return [((1 + (1/i))**i) for i in range(1, num+1)]

print(create_dict(n))

arr = create_list(n)

def sum(array):
    sum = 0
    for i in array:
        sum += i
    return sum

print(sum(arr))




