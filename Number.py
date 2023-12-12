'''
Number Guessing Game
-------------------------------------------------------------
'''

import random

attempts_list = []

def show_score():
    if not attempts_list:
        print('There is currently no high score,'
              ' it\'s yours for the taking!')
        
    else:
        print(f'The current high score is'
              f' {min(attempts_list)} attempts')