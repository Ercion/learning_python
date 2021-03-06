# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:51:13 2020

@author: Ercan Karaçelik
"""

def fibonacci(n):
    '''
    
    Parameters
    ----------
    n : number of fibonacci numbers

    Returns
    -------
    fib_list : this list will keep fibonacci numbers

    '''
    a=0
    b=1
    fib_list=[]
    for i in range(n):
        a,b=b,a+b
        fib_list.append(a)
    return fib_list


print(fibonacci(15)) 
