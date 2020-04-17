# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:43:00 2020

@author: Ercan Karaçelik
"""

def binary_search(item,my_list):
    found=False
    first=0
    last=len(my_list) - 1 
    
    
    while first <= last and found==False:
        mid_point=(first+last)//2
        if my_list[mid_point]==item:
            found=True
        else:
            if my_list[mid_point]<item:
                first=mid_point+1
            else:
                last=mid_point-1
    return found


test =[1,2,3,4,5]
print(binary_search(5,test))
print(binary_search(88,test))
