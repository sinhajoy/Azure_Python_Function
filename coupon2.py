# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:45:19 2021

@author: joysi
"""

for i in range(int(input())):
    a=input().split()
    b=input().split()
    c=input().split()
    day1=0
    day2=0
    for i in b:
        day1=day1+int(i)
    for i in c:
        day2=day2+int(i)
                                #a[1]=Coupon a[0]=Delivery
    i_cup=day1+day2
    i_d=day1+day2++int(a[0])+int(a[0])
    
    if day1>=150 and day2>=150:
        i_cup=i_cup+int(a[1])
    elif day1>=150 or day2>=150:
        i_cup=i_cup+int(a[1])+int(a[0])
    else:
        i_cup=i_cup+int(a[0])+int(a[0])
        
    if (i_cup<i_d):
        print("YES")
        
    else:
        print('NO')
        