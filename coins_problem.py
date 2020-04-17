# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:33:01 2020

@author: Ercan Karaçelik
"""


n=100
coins=[0]*n

for i in range(1,n):
    for j in range(0,n,i):
        coins[j]=1-coins[j]
        

d={}

for i,v in enumerate(coins):
    if v !=0:
        d[i]=v
        
        
print(d)

L=[]

for k,v in d.items():
    L.append(k)
    