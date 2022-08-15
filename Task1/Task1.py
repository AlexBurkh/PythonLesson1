# -*- coding: cp1251 -*-
# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

def define_position(x, y):
    if (0 < x <= 1) and (0 < y <= 1):
        return "Первая четверть"
    elif (-1 <= x < 0) and (0 < y <= 1):
        return "Вторая четверть"
    elif (-1 <= x < 0) and (-1 <= y < 0):
        return "Третья четверть"
    elif (0 < x <= 1) and (-1 <= y < 0):
        return "Четвертая четверть"
    elif (y == 0):
        return "Ось ОХ"
    elif (x == 0):
        return "Ось ОY"

x = float(input("Введите координату Х (от -1 до 1): "))
y = float(input("Введите координату Y (от -1 до 1): "))

if (-1 <= x <= 1) and (-1 <= y <= 1):
    position = define_position(x, y)
    print(position)