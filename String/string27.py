# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 17:35:20 2022

@author: Shohruh Tukhtashev
"""

n1=int(input('n1='))
n2=int(input('n2='))
s1="BEM tizimida buyruq manba sxemasinin ya’ni knopka va yo’nalish relesi sxemasini tadqiq etish."
s2="Boshqarish apparatlariga elektr markazlashtirish (EM) xizmat ko’rsatish vaqtini qisqartirish maqsadida"
s=s1[:n1]+s2[len(s2)-n2:]
print(s)