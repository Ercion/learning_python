# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:20:48 2020

@author: Ercan Karaçelik
"""


'''

Enumerate() method

adds a counter to an iterable and returns it in a form of enumerate object. 

enumerate(iterable, start=0)

'''

alpha_list=['a','b','c','d']

for count,item in enumerate(alpha_list):
         print(count,item)
         
         

for count,item in enumerate(alpha_list,start=12):
    print(count,item)

