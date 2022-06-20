# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так: 
# [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

num = 10
neg_num = -num
print(neg_num)

def fib(n):
    if n in [0, 1]: return 1
    if n > 0: return fib(n-1) + fib(n-2)
    if n < 0: return fib(n+2) - fib(n+1)

def list_fib(neg, pos):
    num_fib = []
    for i in range(neg - 1, pos):
        num_fib.append(fib(i))
    return num_fib

array = list_fib(neg_num, num)

print(array)


