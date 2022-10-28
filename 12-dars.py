# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 11:23:58 2022

@author: Shohruh Tukhtashev
"""
'''for1'''
# k=int(input('k='))
# n=int(input('n='))
'''for2'''
# a=int(input('a='))
# b=int(input('b='))
# sana=0
# for i in range(a,(b+1)):
#     print(i)
#     sana+=1
# print(f"Orasida {sana} ta son bor")
'''for3'''
# a=int(input('a='))
# b=int(input('b='))
# sana=0
# for i in range(b-1,a,-1):
#     print(i)
#     sana+=1
# print(f"Orasida {sana} ta son bor")
'''for4'''
# cst_kg=float(input("1 kg konfitning narxini kiriting: "))
# for i in range(1,10+1):
#     print(f"{i}kg konfit → {i*cst_kg}")
'''for5'''
# cst_kg=float(input("1 kg konfitning narxini kiriting: "))
# for i in range(1,11):
#     print(f"{i/10}kg konfit → {(i/10)*cst_kg}")
'''for6'''
# cst_kg=float(input("1 kg konfitning narxini kiriting: "))
# for i in range(12,20+1):
#     print(f"{i/10}kg konfit → {(i/10)*cst_kg}")
'''for7'''
# a=int(input('a='))
# b=int(input('b='))
# s=0
# for i in range(a,b+1):
#    s+=i
# print(f'{a} dan {b} gacha sonlar yig\'indisi {s} ga teng. [a,b]')
'''for8'''
# a=int(input('a='))
# b=int(input('b='))
# s=1
# for i in range(a,b+1):
#     s*=i
# print(f"a dan b gacha bo'lgan sonlar ko'paytmasi {s} ga teng.[a,b]")
'''for 9'''
# a=int(input('a='))
# b=int(input('b='))
# s=0
# for i in range(a,b+1):
#     s+=i*i
# print(f"a dan b gacha sonlar kvadratining yig'indisi {s} ga teng. [a,b]")
'''for10'''
# n=int(input('n='))
# s=1
# for i in range(2,n+1):
#     s+=1/i
# print(s)
'''for 11'''
# n=int(input('n='))
# s=0
# for i in range(1,n+1):
'''for 12'''
# n=int(input('n='))
# s=1
# for i in range(11,10+n+1):
#     s*=i/10
# print(s)
'''for 13'''
# n=int(input('n='))
# s=0
# for i in range(11,10+n+1):
#     s+=i/10
# print(s)
'''for 14'''
# n=int(input('n='))
# s=0
# for i in range(1,n+1):
#     s+=(2*i-1)  
# print(s)
'''for 15'''
# a=float(input('a='))
# n=int(input('n='))
# s=1
# for i in range(1,n+1):
#     s*=a
# print(s)
'''for 16'''
# a=float(input('a='))
# n=int(input('n='))
# for i in range(1,n+1):
#     print(f"{a}^{i}={a**i}")
'''for 17'''
# a=float(input('a='))
# n=int(input('n='))
# s=1
# for i in range(1,n+1):
#     s+=a**i
# print(s)
'''for 18'''
# a=float(input('a='))
# n=int(input('n='))
# s=0
# for i in range(n+1):
#     p=(-1)**i*a**i
#     s+=p
# print(s)
'''for 19'''
# n=int(input('n='))
# s=1
# for i in range(1,n+1):
#     s*=i
# print(s)
'''for 20'''
# n=int(input('n='))
# s=0;p=1
# for i in range(1,n+1):
#     p*=i
#     s+=p
# print(s)
'''for 21'''
# n=int(input('n='))
# s=1;p=1
# for i in range(1,n+1):
#     p*=i
#     s+=1/p
# print(s)
'''for 22'''
'''
n=int(input('n='))
x=float(input('x='))
s=1;p=1
for i in range(1,n+1):
    p*=i
    s+=x**i/p
print(s)
'''
#import math
#print(math.exp(2))
'''for 23'''
'''
n=int(input('n='))
x=float(input('x='))
s=0;
for i in range(n+1):
    a=1
    for b in range(1,2*i+1+1):
        a*=b
    p=(-1)**i*x**(2*i+1)/a
    s+=p
print(s)
'''
'''for 24'''
# n=int(input('n='))
# x=float(input('x='))
# s=0
# for i in range(n+1):
#     p=1
#     for b in range(1,i+1+1):
#         p*=b
#       a=(-1) **n*x**(2*n)/p
#       s+=a
# print(s)
'''for 25'''
# n=int(input('(n>0) n='))
# x=float(input('(|x|<1) x='))
# s=0
# for i in range(1,n+1):
#     s+=(-1)**(n-1)*x**n/n
# print(s)
'''for 26'''
# n=int(input('(n>0) n='))
# x=float(input('(|x|<1) x='))
# s=0
# for i in range(1,n+1):
#     s+=(-1)**n*x**(2*n+1)/(2*n+1)
# print(s)
'''for 27'''
# n=int(input('(n>0) n='))
# x=float(input('(|x|<1) x='))
# s=0
# for i in range(1,n+1):
#     a=2
#     for x in range(2,i+1):
#         a*=(2*n)*(2*n+1)
#     o=1
#     for y in range(2,i+1):
#         o*=2*n-1
#     s+=o/a
# print(s)
'''28'''
'''29'''
# n=int(input('n='))
# a=float(input('a='))
# b=float(input('b='))
# for i in range(1,n+1) :
#     s=(b-a)/n*i
#     print(s)
'''30'''
# import math
# n=int(input('n='))
# a=float(input('a='))
# b=float(input('b='))
# for i in range(1,n+1):
#     s=(b-a)/n*i
#     f=1-math.sin(s)

'''31'''
# n=int(input('(n>0) n='))
# a0=2
# for i in range(1,n+1):
#     ai=2+1/a0
#     a0=ai
#     print(ai)
'''32'''
# n=int(input('(n>0) n='))
# a0=1
# for i in range(1,n+1):
#     ai=(a0+1)/i
#     a0=ai
#     print(f"{i}-hadi: {ai}")
'''33'''
# n=int(input('(n>1) n='))
# f1=1;f2=1
# for i in range(2,n):
#     fi=f1+f2
#     f1=f2
#     f2=fi
# print(fi)
'''34'''
# n=int(input('(n>1) n='))
# a1=1;a2=2
# for i in range(2,n):
#     ai=a1+a2
#     a1=a2
#     a2=ai
# print(ai)
'''35'''
# n=int(input('(n>2) n='))
# a1=1;a2=2;a3=3
# if n==2:print(a2)
# if n==3 or n>3:print(a2,a3)
# for i in range(4,n+1):
#     ai=a3+a2-2*a1
#     print(ai)
#     a1=a2;a2=a3;a3=ai
''' Ichma ich ochilgan siklllar ''' 
'''36'''
# n=int(input('n='))
# k=int(input('k='))
# s=0
# for i in range(1,n+1):
#     s+=i**k
# print(s)
'''37'''
# n=int(input('n='))
# s=0
# for i in range(1,n+1):
#     s+=i**i
# print(s)
'''38'''
# n=int(input('n='))
# s=0
# for i in range(1,n+1):
#     for k in range(i,):  
# print(s)
'''39'''
# a=int(input('a='))
# b=int(input('b='))
# for i in range(a,b+1):
#     for k in range(i):
#         print(i)
'''40'''
# a=int(input('a='))
# b=int(input('b='))
# sana=0
# for i in range(a,b+1):
#     sana+=1
#     for k in range(sana):
#         print(i)
'''n ta kirirtilgan sonlarning musbat eng kichigini chiqaruvchi dastur'''
# n=int(input())
# x=True
# for i in range(n):
#     a=float(input("=="))
#     if x and a>0:
#         kichik=a
#         x=False
#     elif x:
#         continue
#     if a<kichik and a>0:
#         kichik=a
# print(kichik)
'''17'''
#n=int(input('n='))
#a=float(input('a='))
#s=0
#for i in range(n+1):
#    j=a**i
#    s+=j
#print(s)
#27
'''
n=int(input('n='))
x=float(input('x='))
s=x;f=1;p=1
for i in range(3,n+4,2):
    f*=(i-2)
    p*=(i-1)
    s+=f*x**i/(p*i)
print(s)
'''
#36
'''
n=int(input('n='))
k=int(input('k='))
s=0
for i in range(1,n+1):
    s+=i**k
print(s)
'''
#38
'''
n=int(input('n='))
s=0
for i in range(1,n+1):
    s+=i**(n-i+1)
print(s)
'''
#39
'''
a=int(input('a='))
b=int(input('b='))
for i in range(a,b+1):
    for x in range(i):
        print(i,end=' ')
    print()

'''
'''takrorlash'''
'''40'''
# a=int(input('a='))
# b=int(input('b='))
# sana=0
# for i in range(a,b+1):
#     sana+=1
#     for j in range(sana):
#         print(i)
'''1'''
# n=int(input('n='))
# k=int(input('k='))
# for i in range(n):
#     print(k,end=' ')
