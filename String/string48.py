# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 19:07:45 2022

@author: Shohruh Tukhtashev
"""

a='hellho worwldw'
# a=a.split()
# b=[]
# c=[]
# for i in range(len(a)):
#     b=[a[i][0]]
#     for j in range(1,len(a[i])):
#         if a[i][0]==a[i][j]:
#             b.append('.')
#         else:
#             b.append(a[i][j])
#     c.append(b)
# x=''
# for i in c:
#     a=''.join(i)
#     a+=' '
#     x+=a
# print(x)
a=a.split()
for i in range(len(a)):
    b=a[i][0]
    a[i]=a[i][1:]
    a[i]=str(a[i]).replace(b, '.')
    a[i]=str(b)+str(a[i])
print(*a)
