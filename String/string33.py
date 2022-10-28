# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 18:01:10 2022

@author: Shohruh Tukhtashev
"""

s1="Boshqarish apparatlariga elektr markazlashtirish"
s2="a"
if s2 in s1:
    print(s1.replace(s2, "",1))
else:
    print(s1)