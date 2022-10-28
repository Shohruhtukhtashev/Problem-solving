# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:25:52 2022

@author: Shohruh Tukhtashev
"""

a='Hi My deAR'
'''
sana=0
for i in a:
    for j in range(65,91):
        if ord(i)==j:
            sana+=1
print(sana)'''
s=0
for i in a:
    if i.isupper():
        s+=1
print(s)