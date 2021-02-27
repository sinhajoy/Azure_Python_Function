# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:35:54 2021

@author: joysi
"""

for i in range(int(input())):
    x=int(input())
    a=x
    for i in range(1,x-1):
        a=a*(x-i)
        
    print(a)