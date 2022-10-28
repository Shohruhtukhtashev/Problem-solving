# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 05:09:29 2022

@author: Shohruh Tukhtashev
"""

a=input('a=')
sana=0
for i in range(len(a)):
    if a[i]==' ':
        sana+=1
if sana!=1:
    for i in range(len(a)):
        if a[i]==' ':
            for j in range(i+1,len(a)):
                if a[j]!=' ':
                    print(a[j],end='')
                else:
                    break
            break