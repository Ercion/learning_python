import re
import math

my_str ='hey! how r u doing?'

print(re.sub('[^\w\s]','',my_str))

my_str = re.sub('[^\w\s]','',my_str)

my_list = my_str.split(' ')

print(my_list)

cnt=0

for i in range(len(my_list)):
  cnt += len(my_list[i])

print('cnt',cnt,len(my_list))
cnt /=len(my_list)

print(math.ceil(cnt))