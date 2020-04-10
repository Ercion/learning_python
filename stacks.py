# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:22:42 2020

@author: Ercan Karaçelik
"""

# STACK IN PYTHON

def balanced_brackets(s):
    stack=[]
    d={')':'(',
       '}':'{',
       ']':'['
       }
    
    for char in s:
        if not stack:
            stack.append(char)
        elif char not in d:
            stack.append(char)
        elif d[char]==stack[-1]:
            stack.pop()
        else:
            stack.append(char)
            
    
    if not stack:
        return True
    else:
        return False
    
    


true_string='[[[{}]]]'

false_string='[[[{}]]]'


print(balanced_brackets(true_string))
   