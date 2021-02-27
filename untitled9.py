# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:59:01 2021

@author: joysi
"""


try:  
    a=input()
    x=input().split()
    counter = 0
    num = int(x[0])
    lis=[]
    for j in x:
        i=int(j)
        curr_frequency = x.count(str(i))
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i
        
    
    print(num)
except:
    pass