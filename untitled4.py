# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 20:36:38 2021

@author: joysi
"""


for i in range(int(input())):
    x=input().split()
    if(sorted(x[0])==sorted(x[1]) and sorted(x[0])==sorted(x[2])):
        print('Possible')
    else:
        print('Not Possible')
