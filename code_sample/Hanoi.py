# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:31:42 2016

@author: ericgrimson
"""

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        c += 1
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
c=0
print(Towers(4, 'P1', 'P2', 'P3'))
print(c)