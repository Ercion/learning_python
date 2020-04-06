# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:47:00 2020

@author: Ercan Karaçelik
"""


'''

Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.

'''

def two_sum(nums,target):
    d={}
    
    
    for i in range(len(nums)):
        if target - nums[i] in d:
            print (d)
            return [d[target-nums[i]],i]
        else:
            d[nums[i]] = i
    return -1


my_list=[1,2,3,5]

print(two_sum(my_list,8))
    