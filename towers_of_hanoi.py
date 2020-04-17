# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 21:41:37 2020

@author: Ercan Karaçelik
"""


A=[3,2,1]
B=[]
C=[]

count=0

def towers_of_hanoi(A,B,C,n):
    global count
    if n==1:
        disk=A.pop()
        C.append(disk)
        count+=1
    else:
        towers_of_hanoi(A,C,B,n-1)
        towers_of_hanoi(A,B,C,1)
        towers_of_hanoi(B,A,C,n-1)
    return count


print(towers_of_hanoi(A,B,C,3))