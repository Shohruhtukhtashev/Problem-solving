# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:52:57 2022

@author: Shohruh Tukhtashev
"""

s=input('s=')
a=''
for i in s[::2]:
    a+=i
if len(s)%2!=0:
    for i in s[len(s)-2::-2]:
        a+=i
else:
    for i in s[len(s)-1::-2]:
        a+=i
print(a)