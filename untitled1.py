# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:53:17 2021

@author: joysi
"""
def split(word):
    return [char for char in word] 
for i in range(int(input())):
    a=input().split()
    b=input().split()
    for i in range(int(a[0])):
        v=input()
        x=split(v)
        score=0
        for i in range(len(x)):
            if(int(x[i])==1):
                score=score+int(b[i])
        print(score)
            
        