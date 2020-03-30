# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:23:49 2020

@author: Ercan Karaçelik
"""

"""
w - write - if not exists, then create 
Note: the "w" method will overwrite the entire file.
r - read
a - append
"""

# WRITE

my_file=open('my_file.txt','w')



my_file.write('deneme first\n')

my_file.write('deneme second\n')

my_file.write('deneme third')

my_file.close()



# READ

my_file = open('my_file.txt','r')

content = my_file.read()

print(content)

my_file.close()


# READLINE  - The readline() method returns one line from the file.


f = open("my_file.txt", "r")
print(f.readline())


# READLINES - Return all lines in the file, as a list where each line is an item in the list object:

f = open("my_file.txt", "r")
print(f.readlines())



# APPEND 

my_file = open("my_file.txt", "a")
my_file.write('\nThis line was appended\n')

my_file.close()


# read it again 

my_file = open('my_file.txt','r')

content = my_file.read()

print(content)

my_file.close()




# WITH OPEN METHOD - 

"""
Notice, that we didn't have to write "file.close()". 
That will automatically be called.
"""

with open("my_file.txt",'a') as file:
    file.write('This line was added using With Open Method')
 

with open("my_file.txt",'r') as file:
    print('WITH OPEN METHOD')
    print(file.read())
