# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:34:31 2022

@author: Shohruh Tukhtashev
"""

s=input('s=')
k=int(input('k='))
b=''
for i in s:
    if i.isalpha():
        if 65<=ord(i)<=90:
            if ord(i)+k<=90:
                b+=chr(ord(i)+k)
            else:
                b+=chr((ord(i)+k-90)+65)
        elif 90<=ord(i)<=122:
            if ord(i)+k<=122:
                b+=chr(ord(i)+k)
            else:
                b+=chr((ord(i)+k-90)+65)
        else:
            b+=i
print(b)