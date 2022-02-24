#9. Показать последнюю цифру трёхзначного числа

number = int(input('Enter the 3 digit number: '))

def last_digit(num):
    return num % 10

if -100 < number < 100:
    print('You gave the wrong number')
else:
    print(last_digit(number))



