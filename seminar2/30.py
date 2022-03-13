#30. Показать кубы чисел, заканчивающихся на четную цифру

def cube_1():
    for i in range(2, 10, 2):
        print(f"cube of number", i, "equals", i*i*i)

cube_1()
