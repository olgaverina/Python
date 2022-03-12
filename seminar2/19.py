#19. Определить номер четверти плоскости, 
# в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

x = int(input('Please enter the x: '))
y = int(input('Please enter the y: '))

if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Начало координат')