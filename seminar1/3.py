
# 3. По заданному номеру дня недели вывести его название

day_of_week = int(input('Enter the number:'))

def day (number):
    if number == 1:
        return 'Monday'
    elif number == 2:
        return 'Tuesday'
    elif number == 3:
        return 'Wednesday'
    elif number == 4:
        return 'Thursday'
    elif number == 5:
        return 'Friday'
    elif number == 6:
        return 'Saturday'
    elif number == 7:
        return 'Sunday'
    else:
        return 'You have entered the wrong number'

print(day(day_of_week))