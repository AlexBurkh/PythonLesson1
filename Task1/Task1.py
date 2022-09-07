# -*- coding: utf-8 -*-

def define_position(x, y):
    if (x > 0) and (y > 0):
        return "first quarter"
    elif (x < 0) and (y > 0):
        return "second quarter"
    elif (x < 0) and (y < 0):
        return "third quarter"
    elif (x > 0) and (y < 0):
        return "fourth quarter"
    elif (y == 0):
        return "OX axis"
    elif (x == 0):
        return "OY axis"

x = float(input("Enter X ( -1 : 1) "))
y = float(input("Enter Y (-1 : 1) "))

if (-1 <= x <= 1) and (-1 <= y <= 1):
    position = define_position(x, y)
    print(position)