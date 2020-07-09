# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import re
from collections import OrderedDict


line_pattern=re.compile('^([\w\W]+)\.([\w\d]+)\s(\d+)b$')

'''
selected_file_types={
         'music':['mp3','acc','flac'],
         'images':['jpg','bmp','gif'],
         'movies':['mp4','avi','mkv'],
         'other':['7z','txt','zip','exe']
}
'''


def get_line_match(line):
     return line_pattern.match(line) if line_pattern.match(line) else False



def solution(S):
    lines=S.split('\n')
    results=''
    result="{0} {1}b\n"
    
    calculations={
        'music':int(0),
        'images':int(0),
        'movies':int(0),
        'other':int(0)
    }
    
    ordered_calculations=OrderedDict(calculations.items())

    for line in lines:
        file_match=get_line_match(line)
        if file_match and int(file_match.group(3)) > 0:
           if file_match.group(2) in ['mp3','acc','flac']:
              ordered_calculations['music']+= int(file_match.group(3))
           elif file_match.group(2) in ['jpg','bmp','gif']:
              ordered_calculations['images']+= int(file_match.group(3))
           elif file_match.group(2) in ['mp4','avi','mkv']:
              ordered_calculations['movies']+= int(file_match.group(3))
           else:
              ordered_calculations['other']+= int(file_match.group(3))
    
    for key,value in ordered_calculations.items():
        results +=result.format(key,value)
 


    return results
 
if __name__=="__main__":
  results = solution("my.song.mp3 11b\nburcu.bu 300b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b")
print(results)
