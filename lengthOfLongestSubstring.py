# -*- coding: utf-8 -*-
"""
Spyder Editor
link -> https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
class Solution:
    def lengthOfLongestSubstring(s):
        
        
        max_len=0
        unique_list=[]
        i=0
        j=0

        while j <len(s) and i <len(s) :
            if s[j] not in unique_list:
               unique_list.append(s[j])
               j+=1
    
               if (j-i) > max_len:
                   max_len= (j-i)
    
            else:
               unique_list.clear()
               i=j


        return max_len


print(Solution.lengthOfLongestSubstring('pwwkew'))

