# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:51:24 2020

@author: Ercan Karaçelik
"""

def insertion_sort(my_list):
    n=len(my_list)
    
    for i in range(1,n):
        print(my_list)
        value=my_list[i]
        j=i
        while j>0 and my_list[j-1] > value:
            my_list[j] = my_list[j-1]
            j-=1
        my_list[j]=value
        
    return my_list



test=[70,24,87,45,2,3,8,9]

print(insertion_sort(test))

 