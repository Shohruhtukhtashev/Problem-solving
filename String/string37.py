# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 05:02:19 2022

@author: Shohruh Tukhtashev
"""

s1="siz buyuk insonsiz siz"
s2='siz'
s2=s2[::-1]
s3='u'
s1=s1[::-1]
s1=s1.replace(s2,s3,1)
print(s1[::-1])