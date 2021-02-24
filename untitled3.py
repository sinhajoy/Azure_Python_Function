# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:22:52 2021

@author: joysi
"""

import numpy
v1=[8, 9, 8, 9]
v2=[2, 3, 5, 3, 4]
v3=[2, 10, 3, 3, 2, 10]
s = numpy.array(v1) 
sort_index = numpy.argsort(s) 
x=[]
for i in sort_index:
    x.append(i+1)
pair=[]
for i in range(len(v1)):
    a=[v1[i],x[i]]
    pair.append(a)
    
print(pair)