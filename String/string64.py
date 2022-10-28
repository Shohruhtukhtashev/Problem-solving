# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:38:13 2022

@author: Shohruh Tukhtashev
"""

s=input('s=')
k=int(input('k='))
b=''
for i in range(len(s)):
    a=ord(s[i])-k
    b+=s[i].replace(s[i],chr(a))
print(b)
