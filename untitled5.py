# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 20:52:38 2021

@author: joysi
"""


def convert(s): 
	if(len(s) == 0): 
		return
	s1 = '' 
	s1 += s[0].upper() 
	for i in range(1, len(s)): 
		if (s[i] == ' '): 
			s1 += s[i + 1].upper() 
			i += 1
		elif(s[i - 1] != ' '): 
			s1 += s[i] 
	return s1
    
def camel_snake(str):
	res = [str[0].lower()]
	for c in str[1:]:
		if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
			res.append('_')
			res.append(c.lower())
		else:
			res.append(c)
	
	return ''.join(res)
	


x=convert('first second')

print(camel_snake(x))

	
