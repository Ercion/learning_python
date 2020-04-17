# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:18:00 2020

@author: Ercan Karaçelik
"""

def linear_search(item,my_list):
    i=0
    found=False
    
    while i<len(my_list) and found==False:
        if my_list[i]==item:
            found=True
        else:
            i+=1
    return found


test=[6,5,8,2,3,70]

print(linear_search(87,test))
print(linear_search(70,test))
