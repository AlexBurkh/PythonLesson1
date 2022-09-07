# -*- coding: utf-8 -*-

def define_vars_range(number : int):
    if (1 <= number <= 4):
        if number == 1:
            print('X: [0 : Infinite]')
            print('Y: [0 : Infinite]')
        elif number == 2:
            print('X: [-Infinite : 0]')
            print('Y: [0 : Infinite]')
        elif number == 3:
            print('X: [-Infinite : 0]')
            print('Y: [-Infinite : 0]')
        elif number == 4:
            print('X: [0 : Infinite]')
            print('Y: [-Infinite : 0]')

quarter_number = input("Enter quarter number (1, 2, 3, 4): ")
define_vars_range(int(quarter_number))