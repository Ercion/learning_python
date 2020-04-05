# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:15:13 2020

@author: Ercan Karaçelik
"""



class Patience(object):
   
    status='patience'
    
    def __init__(self,name,age):
        '''
        Parameters
        ----------
        name : Patience name
        age : Patience age
        conditions : Existing medical situation

        '''
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

ercan.get_details()





class Infant(Patience):
    ''' Patience under 2 years '''
    
    def __init__(self, name, age):
        '''       

        Parameters
        ----------
        name : Patient name, inherited from Patience class
        age : Patient age, inherited from Patience class

        '''
        self.vacations=[]
        super().__init__(name, age)
    
    def add_vac(self,vacine):
        vacations.append(vacine)
    
    def get_details(self):
        print(f'Patience Record:{self.var_name}, {self.var_age}'\
              f'Current Informaion: {self.conditions}'\
              f'Patient has had {self.vacations} vacine' \
              f'\n {self.var_name} is AN INFANT, HAS HE HAD ALL HIS CHECKS?')
    

    
    
baby=Infant('nope',1)



baby.get_details()

