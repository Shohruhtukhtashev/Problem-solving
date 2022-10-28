# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:40:14 2022

@author: Shohruh Tukhtashev
"""

a='''Funksiyaga argument sifatida
konsolga chiqariluvchi qiymatlar'''
a=a.split()
x=True
for i in a:
    if x:
        len_max=len(i)
        soz=i
        x=False
    if len_max<len(i):
        len_max=len(i)
        soz=i
print(f"lengs: {len_max}\nSo'z: {soz}")