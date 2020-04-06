# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:47:58 2020

@author: Ercan Karaçelik
"""

# CEASAR CIPHER


'''
Caesar cipher: Encode and decode
Method in which each letter in the plaintext is replaced by a letter 
some fixed number of positions down the alphabet. 
The method is named after Julius Caesar, 
who used it in his private correspondence.
'''


alphabet='abcdefghijklmnopqrstuvwxyz'

input_text='Ercion'


'''

str.find(sub[, start[, end]])

This function returns the lowest index in the string 
where substring “sub” is found within the slice s[start:end].

start default value is 0 and it’s an optional argument.

end default value is length of the string, it’s an optional argument.

If the substring is not found then -1 is returned.

'''



def encrypt(input_text,required_shift):
    output_text=''
    input_text=input_text.lower()
    for i in input_text:
        if i not in alphabet:
            output_text+=i
        else:
            alphabet_index=alphabet.find(i) #
            output_text+=alphabet[(alphabet_index+required_shift)%26]
    return output_text


print(encrypt(input_text,1))
        
    