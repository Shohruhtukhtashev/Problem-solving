# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 18:42:05 2022

@author: Shohruh Tukhtashev
"""

a=input('a=')
a=a.upper()

sana=0;son=0
a=a.split()
for i in a:
    sana=0
    for j in i:
        if j=='A':
            sana+=1
    if sana==3:
        son+=1
print(son)