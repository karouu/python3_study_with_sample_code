#!/usr/bin/python

import os
import re
from pprint import pprint

path = os.getcwd()+'/long.txt'

def word_static(path):
    f = open(path,'r+')
    word_static = {}
    for word in re.sub('[^0-9a-zA-Z]+', ' ', f.read()).split():
        if word not in word_static:
            word_static[word] = 1
        else:
            word_static[word] += 1
    
    pprint(word_static)

if __name__ == '__main__':
    word_static(path)

