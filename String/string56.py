# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:46:58 2022

@author: Shohruh Tukhtashev
"""

a='''Funksiyaga argument sifatida
konsolga chiqariluvchi qiymatlar'''
a=a.split()
x=True
for i in a:
    if x:
        len_min=len(i)
        soz=i
        x=False
    if len_min>=len(i):
        len_min=len(i)
        soz=i
print(f"lengs: {len_min}\nSo'z: {soz}")