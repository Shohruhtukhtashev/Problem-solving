# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 18:47:28 2022

@author: Shohruh Tukhtashev
"""

s1="Boshqarish apparatlariga elektr markazlashtirish (EM) xizmat ko’rsatish vaqtini qisqartirish maqsadida"
s2='a'
a=s1[::-1]
a=a.replace(s2,"",1)
print(a[::-1])