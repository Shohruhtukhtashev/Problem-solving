# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 05:19:00 2022

@author: Shohruh Tukhtashev
"""

s1="ASSALOMU ALAYKUM AKA MANAM ANA AYA"
sana=0
a=s1.split()
print(a)
for i in a:
    if i[0]==i[len(i)-1]:
      sana+=1
print(sana)