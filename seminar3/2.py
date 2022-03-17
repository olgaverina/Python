#2. Для N = 5: 1, -3, 9, -27, 81 и т.д.

num = int(input("Enter the number >>"))
array = []

def create_array(arr, n):
    for i in range(0, n):
        arr.append(3**i)
        if i % 2:
            arr[i] = arr[i] * -1
    return arr

print(create_array(array,num))

