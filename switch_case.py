# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:13:45 2020

@author: Ercan Karaçelik
"""


# sdfsdf  Ctrl + 1 for comment line - Spyder IDE

# Implement Python Switch Case Statement using Dictionary 

print("""Learn how many days are there in that selected month \n
       1- January \n
       2- February \n
       3- March \n
       4- April \n
       5- May \n
       6- June \n
       7- July \n
       8- August \n
       9- September \n
       10- October \n
       11- November \n
       12- December""")


















i= int(input('please input the num of the month  -->'))

def getDaysNumOfMonth(i):
        switcher={
                1:'January - 31 days',
                2:'February - 28 days in a common year and 29 days in leap years',
                3:'March - 31 days',
                4:'April - 30 days',
                5:'May - 31 days',
                6:'June - 30 days',
                7:'July - 31 days',
                8:'August - 31 days',
                9:'September - 30 days',
                10:'October - 31 days',
                11:'November - 30 days',
                12:'December - 31 days'
             }
        return switcher.get(i,"Invalid num of month")
     
        
        
print(getDaysNumOfMonth(i))
        

            
        
        
        