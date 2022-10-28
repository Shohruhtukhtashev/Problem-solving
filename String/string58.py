# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:52:19 2022

@author: Shohruh Tukhtashev
"""

s=input("s=")
'''s=s.split('\\')
x=s[-1].rsplit('.',1)
print(x[0])'''
print(s[s.rfind('\\')+1:s.rfind('.')])