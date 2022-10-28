# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 18:54:02 2022

@author: Shohruh Tukhtashev
"""

a=input('a=')
a=a.split()
x=True
for i in a:
    if x:
        mini=len(i)
        soz=i
        x=False
    if mini>len(i):
        mini=len(i)
        soz=i
print(f"so'z: {soz}\nUzunlik: {mini}")