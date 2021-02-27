# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:46:06 2021

@author: joysi
"""

def find_ele(arr,n):
    x=[]
    diff=10**20
    arr=sorted(arr)
    for i in range(n-1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]
            x.append(arr[i+1])
            x.append(arr[1])
			
    print(diff)
    print(x)

arr = [1, 5, 3, 19, 18, 25] 
n = len(arr) 
find_ele(arr,n)
