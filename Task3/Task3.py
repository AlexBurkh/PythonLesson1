# -*- coding: cp1251 -*-
# Найти расстояние между двумя точками пространства
import math

def calc_distance(point_1, point_2):
    return math.sqrt((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2 + (point_2[2] - point_1[2])**2)

#          X  Y  Z
point_1 = (2, 3, 1)
point_2 = (3, 4, 5)

print(calc_distance(point_1, point_2))