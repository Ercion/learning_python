# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:22:07 2020

@author: Ercan Karaçelik
"""


star='*'

for i in range(6):
    for j in  range(6):
        if i==0 and j<6:
            print(star,end='')
        elif i==1 and j<1:
            print()
            print(star)
        elif i==2 and j<5:
            print(star,end='')
        elif i==3 and j<1:
            print()
            print(star,end='')
        elif i==4 and j<1:
            print()
            print(star,end='')
        elif i==5 and j<1:
            print()
            print(star,end='')