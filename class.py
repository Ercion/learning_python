# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 09:56:49 2020

@author: Ercan Karaçelik
"""

# CLASS
# naming class and function
# my_function
# MyClass


class Patience(object):
    ''' Class Definition'''
    status='patience'
    
    def __init__(self,name,age):
       self.var_name=name
       self.var_age=age
       self.conditions=[]
    
    def get_details(self):
        print(f'Patience Record:{self.var_name}, {self.var_age}'\
              f'Current Informaion: {self.conditions}')
    
    def add_info(self,information):
        self.conditions.append(information)
       
ercan= Patience("Ercion",58)

ercan.add_info('he is awesome')

print(ercan.get_details())
