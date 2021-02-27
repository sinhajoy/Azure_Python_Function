# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:43:06 2021

@author: joysi
"""



def findMinDiff(arr, n):
	arr = sorted(arr)
    lis=[]
	diff = 10**20
	for i in range(n-1): 
		if arr[i+1] - arr[i] < diff: 
			diff = arr[i+1] - arr[i]
            
	return diff 

# Driver code 
arr = [1, 5, 3, 19, 18, 25] 
n = len(arr) 
print("Minimum difference is " + str(findMinDiff(arr, n))) 

