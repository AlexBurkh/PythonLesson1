# -*- coding: cp1251 -*-
# �������� � ����� �������� ������������ ��������� ��� �� ����� ��� ��������� ����� � ������������ � � �

def define_position(x, y):
    if (0 < x <= 1) and (0 < y <= 1):
        return "������ ��������"
    elif (-1 <= x < 0) and (0 < y <= 1):
        return "������ ��������"
    elif (-1 <= x < 0) and (-1 <= y < 0):
        return "������ ��������"
    elif (0 < x <= 1) and (-1 <= y < 0):
        return "��������� ��������"
    elif (y == 0):
        return "��� ��"
    elif (x == 0):
        return "��� �Y"

x = float(input("������� ���������� � (�� -1 �� 1): "))
y = float(input("������� ���������� Y (�� -1 �� 1): "))

if (-1 <= x <= 1) and (-1 <= y <= 1):
    position = define_position(x, y)
    print(position)