# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 05:24:36 2022

@author: Shohruh Tukhtashev
"""
s="SALOM KUNINGIZ HAYRLI O'TSIN"
sana=0
s=s.split()
for i in s:
    if 'A' in i:
        sana+=1
print(sana)