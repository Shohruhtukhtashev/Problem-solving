# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 19:03:10 2022

@author: Shohruh Tukhtashev
"""

a=input('a=')
b=''
for i in range(len(a)-1):
    b+=a[i]+'.'
print(b+a[len(a)-1])