# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:43:55 2021

@author: joysi
"""

try:
    for i in range(int(input())):
        x=input()
        a=input().split()
        test_list = []
        for i in a:
            test_list.append(int(i))  
        res = list(zip(test_list, test_list[1:] + test_list[:1])) 
        val=[]
        for i in res:
            a=(i[0]*i[1])+max(i[0]-i[1],i[1]-i[0])
            val.append(a)
        
        print(max(val))
        
except:
    pass
        
        
