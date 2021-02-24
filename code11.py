# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:36:16 2021

@author: joysi
"""
try
for i in range(int(input())):
    a=input().split()
    f=int(a[1])*int(a[1])
    x=int(a[0])/f
    if(x<=18):
        print(1)
    if x in range(19,25):
        print(2)
    if x in range(25,30):
        print(3)
    if(x>=30):
        print(4)