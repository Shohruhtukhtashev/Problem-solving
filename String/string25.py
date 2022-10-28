# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 08:52:51 2022

@author: Shohruh Tukhtashev
"""

a=input('a=')
c=a;q=''
while c!=0:
    q+=str((int(c)%2))
    c=int(c)//2

print(q[::-1])
    