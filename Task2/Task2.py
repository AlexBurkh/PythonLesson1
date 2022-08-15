# -*- coding: utf-8 -*-

def define_vars_range(number : int):
    if (1 <= number <= 4):
        if number == 1:
            print('X: [0 : 1]')
            print('Y: [0 : 1]')
        elif number == 2:
            print('X: [-1 : 0]')
            print('Y: [0 : 1]')
        elif number == 3:
            print('X: [-1 : 0]')
            print('Y: [-1 : 0]')
        elif number == 4:
            print('X: [0 : 1]')
            print('Y: [-1 : 0]')

quarter_number = input("Enter quarter number (1, 2, 3, 4): ")

define_vars_range(int(quarter_number))