# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:29:15 2020

@author: Ercan Karaçelik
"""

def add(L):
    '''
    Adds the integer items of a list
    '''
    size =len(L)
    total=0
    iterator=0
    print('Reached the wile loop')
    while iterator < size:
        total +=L[iterator]
        iterator+=1
        print(f'Iterator is {iterator} total is {total}')
    return total

my_list=[1,2,3,4,5]
add(my_list)