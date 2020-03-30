# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:07:45 2020

@author: Ercan Karaçelik
"""


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


#Dictionary Comprehension

from collections import Counter

print(Counter(lorem_ipsum.lower()))

new_dict = dict(Counter(lorem_ipsum.lower()))


new_dict={k:v for k,v in new_dict.items() if k.isalpha()}

print(new_dict)




#List Comprehension

new_List=[x**5 for x in range(10)]


empty_List=[]

for i in range(10):
    empty_List.append(i**5)


print(empty_List)