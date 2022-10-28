# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 20:40:28 2022

@author: Shohruh Tukhtashev
"""

s=input('s=')
x=True
for i in s:
    if 97<=ord(i)<=122:
        if x:
            number=ord(i)
            x=False
        elif number<ord(i):
            a=0
        else:
            a=i
            break
print(a)