# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:59:01 2022

@author: Shohruh Tukhtashev
"""

s=input('s=')
a=''
for i in range(len(s)//2):
    a+=s[i]+s[-(i+1)]
if len(s)%2!=0:
    a+=s[len(s)//2]
print(a)
