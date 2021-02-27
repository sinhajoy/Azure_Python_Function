# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:43:06 2021

@author: joysi
"""

try:
    for i in range(int(input())):
        x=int(input())
        x=input().split()
        lis=[]
        for i in x:
            lis.append(int(i))
        s=sorted(lis)
        ans = str(s[0])+' '+str(s[1])
except:
    pass


print(ans)