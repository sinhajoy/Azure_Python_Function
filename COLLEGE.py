# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:35:37 2021

@author: joysi
"""

for i in range(int(input())):
    x=int(input()) #Number of Season
    y=input().split() #Intro Song In the ith season
    z=input().split()# Number of Episod
    o=input().split()
    
    lis1=[]
    lis2=[]
    lis3=[]
    for i,j,l in x,y,z:
        lis1.append(i)
        lis2.append(j)
        lis3.append(l)
        
    print(lis1)
    print(lis2)
    print(lis3)