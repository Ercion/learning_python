# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 21:48:15 2020

@author: Ercan Karaçelik
"""


'''
PDB module 

The module pdb defines an interactive source code debugger for Python programs.

'''

import pdb


def add(L):
    '''
    Adds the integer items of a list
    '''
    size =len(L)
    total=0
    iterator=0
    pdb.set_trace()
    while iterator < size:
        total +=L[iterator]
        iterator+=1
        print(f'Iterator is {iterator} total is {total}')
    return total

my_list=[1,2,3,4,5]
add(my_list)