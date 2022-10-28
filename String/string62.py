# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:11:42 2022

@author: Shohruh Tukhtashev
"""

s=input('s=')
b=''
for i in range(len(s)):
    a=ord(s[i])+1
    b+=s[i].replace(s[i],chr(a))
print(b)
