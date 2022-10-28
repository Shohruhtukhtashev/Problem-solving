# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 19:01:37 2022

@author: Shohruh Tukhtashev
"""

a=input('a=')
a=a.split()
x=True
for i in a:
    if x:
        maxi=len(i)
        soz=i
        x=False
    if maxi<len(i):
        maxi=len(i)
        soz=i
print(f"so'z: {soz}\nUzunlik: {maxi}")