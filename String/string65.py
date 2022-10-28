# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:42:08 2022

@author: Shohruh Tukhtashev
"""

s=input('s=')
c=input('c=')
b=''
x=True
for i in range(len(s)):
    if x:
        k=ord(s[i])-ord(c)
        x=False
    a=ord(s[i])-k
    b+=s[i].replace(s[i],chr(a))
print(k,b)

