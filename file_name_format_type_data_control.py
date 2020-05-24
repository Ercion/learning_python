# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:01:09 2020

@author: Ercan Karacelik
"""

import os
import datetime
import csv
from string import ascii_letters, digits



x= datetime.date.today()
file_format=x.strftime('_%Y%m%d')+'.csv'


# Wrong format of the input files names

print('question 1\n')

for file in os.listdir("../../input"):
    if not file.endswith(file_format):
       print(file)
       

# Extra comma or wrong delimiter used


print('\nquestion 2\n')

os.chdir("../../input")
    
for file in os.listdir("."): 
        try:
            with open(file, newline='') as csvfile:
                 dialect = csv.Sniffer().sniff(csvfile.read(1024))
                 csvfile.seek(0)
                 reader = csv.reader(csvfile, dialect)
                 print(file,reader.dialect.delimiter==',')
                 if not reader.dialect.delimiter==',':
                      print(f'this file has wrong delimiter - > {file} and delimeter is ',reader.dialect.delimiter)
                 
        except:
            print("an error occurred while reading file, control file size : ",file)


# Missing Header


print('\nquestion 3\n')

#os.chdir("../../input")
    
for file in os.listdir("."): 
        try:
            with open(file, newline='') as csvfile:
                 dialect = csv.Sniffer().has_header(csvfile.read(1024))
                 print(file,dialect)
                 
        except:
            print("This file has no header : ",file)


# Empty File      

print('\nquestion 4\n')
            
#os.chdir("../../input")
for file in os.listdir("."):
    filesize = os.path.getsize(file)
    if filesize == 0:
        print(f"The file is empty: {file} and size: " + str(filesize))
    

                  
# Names having special characters

print('\nquestion 5\n')          

#os.chdir("../../input")
for file in os.listdir("."): 
        try:
            with open(file,'r') as csvfile:
                 
                 text = csvfile.read()
                 text =set(text).difference(ascii_letters+digits)
                 
                 for i in [' ','_','\n',',']:
                     if i in text: 
                        text.remove(i)                     
                 
                 if  text:
                     print(f'{file} has special characters. {text}')
                 else:
                     print(f"{file} hasn't special characters.")   
                 
        except:
            print("an error occurred while reading file : ",file)


   
            
            
            
            

