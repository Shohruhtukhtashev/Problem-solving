# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 15:48:38 2022

@author: Shohruh Tukhtashev
"""

a='samom ljlkhljl'
a=a.split()
for i in range(len(a)):
    b=a[i][len(a[i])-1]
    c=a[i].count(b)
    print(a[i].replace(b,'.',c-1))