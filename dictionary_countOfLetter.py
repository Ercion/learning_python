# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:04:34 2020

@author: Ercan Karaçelik
"""

#Dictionaries, Zip Command, Matplotlib

lorem_ipsum="""
What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a and
type specimen book. It has survived not only five centuries, but also the leap
into electronic typesetting, remaining essentially unchanged. It was popularised
in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus PageMaker including
versions of Lorem Ipsum.
"""

letter_counts = dict()
for i in lorem_ipsum:
  letter_counts[i] = letter_counts.get(i, 0) + 1
  
  


import matplotlib.pyplot as plt

x,y= zip(*letter_counts.items())

"""
 If we want to extract the zip, we have to use the same zip()function. 
 But we have to add an asterisk(*) in front of that list you get 
 from the zipped variable.

"""

plt.bar(x,y)
plt.show()
  


letter_counts_isalpha={}


for i in lorem_ipsum:
    if i.isalpha():
        letter_counts_isalpha[i.lower()] = letter_counts_isalpha.get(i.lower(), 0) + 1
        

print(letter_counts_isalpha)

x,y= zip(*letter_counts_isalpha.items())

plt.bar(x,y)
plt.show()








