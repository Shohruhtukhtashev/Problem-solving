# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:46:07 2022

@author: Shohruh Tukhtashev
"""

'''1'''
# n=int(input('n='))
# s=0
# for i in range(1,n+1):
#     s+=i
# print(f"{n} gacha sonlarni yig'indisi {s} ga teng")
'''2'''
# n=int(input('n='))
# sana=0
# for i in range(1,n+1):
#     if n%i==0:
#         sana+=1
# if sana==2:
#     print('Tub')
# else:
#     print('Tub emas')
'''3'''
# n=int(input('n='))
# sana=0
# for i in range(2,n+1,2):
#     k=i
#     if i%(k/2)==0:
#         print(i)
'''4'''
# n=int(input('n='))
# s=1
# for i in range(1,n+1):
#     s*=i
# print(s)
'''5'''

'''6'''
# a=int(input('a='))
# b=int(input('b='))
# while a!=0:
    
#     if b>a:
#         a,b=b,a
#     if a>b:
#         a%=b
# print(b)
'''8'''
'''10''' #chala
# ma=int(input('a='))
# mi=int(input('a='))
# sana=0
# a=True
# while a:
    
#     k=int(input('a='))
#     if ma==-1 or mi==-1 or k==-1:
#         a=False
#     if ma>k or ma>mi:
#         pass
#     elif ma<mi:
#         ma=mi 
#     else:
#         ma=k
#     if mi<k or mi<ma:
#         pass
#     else:
#         mi=k
#     if mi>0 or ma>0 or a>0:
#         sana+=1
# print(ma,mi,sana)
'''11''' #xato
# n=int(input('n='))
# sana=0
# for i in range(4,n+1):
#     for k in range(1,i+1):
#         if i%k==0:
            # sana+=1
# if sana!=2:    
#     print(i,end=' ')
'''12'''
# n=int(input('n='))
# for i in range(n):
#     for x in range(n):
#         print('#',end='')
#     print('\n',end='')
'''13
n gacha bolgan kara-kara jadvali
''' 
# n=int(input('n='))
# k=1
# while k<=n:
#     for i in range(1,11):
#         a=k*i
#         print(f"{k}*{i}={a}")
#     k+=1
'''
n gacha bo'lgan tub sonlar va ularning yig'indisini chiqaruvhi dastur
'''
# n=int(input('n='))
# i=3;s=0;k=0
# print(2,end=' ')
# while i<=n:
#     s=0;j=3
#     while j<i:
#         if i%j==0:
#             s=1
#             break
#         j+=2
#     if s==0:
#         k+=i
#         print(i,end=' ')
#     i+=2
# print(f"Yig'indisi: {k+2}")
'''
                14
 N musbat soni berilgan. Dastlabki N ta toq sonlarni ekranga chiqaruvchi va 
ularning yig’indisini aniqlovchi dastur tuzing.
'''
# n=int(input('n='))
# s=0
# for i in range(1,n*2,2):
#     print(i,end=' ')
#     s+=i
# print(f"Yig'indisi: {s}")
'''                 15
N musbat soni berilgan. Dastlabki Nta juft sonlarni ekranga chiqaruvchi 
va ularning yig’indisini aniqlovchi dastur tuzing.
'''
# n=int(input('n='))
# s=0
# for i in range(2,n*2+1,2):
#     print(i,end=' ')
#     s+=i
# print(f"Yig'indisi: {s}")
'''             16'''
# n=int(input('n='))
# k=0
# for i in range(1,n+1):
#     k=k*10+i
# print(k)
'''17'''
# n=int(input('n='))
# a1=1;a2=1
# print(a1,a2,end=' ')
# for i in range(3,n+1):
#     ai=a1+a2
#     a1=a2
#     a2=ai
#     print(ai,end=' ')
'''18'''
'''
n=int(input('n='))
i=3;s=0;k=0
print(2,end=' ')
while i<=n:
    s=0;j=3
    while j<i:
        if i%j==0:
            s=1
            break
        j+=2
    if s==0:
        x=1
        while x<i:     
            i+=2
'''
'''19'''
# n=int(input('n='))
# for i in range(1,n+1):
#     for x in range(i):
#         print('*',end='')
#     print('\n',end='')
'''20'''
# n=int(input('n='))
# for i in range(2,n+2):
#     for x in range(1,i):
#         print(x,end='')
#     print('\n',end='')
'''21'''
# n=int(input('n='))
# for i in range(1,n+1):
#     for x in range(i):
#         print(i,end='')
#     print('\n',end='')
'''22'''
# n=int(input('n='))
# s=0
# for i in range(1,n+1):
#     for x in range(i):
#         s+=1
#         print(s,end=' ')
#     print('\n',end='')
'''23'''
# n=int(input('n='))
# s=0
# for i in range(1,n+1) :
#     for x in range(n,i-1,-1):

#         print(' ',end='')
#         if x==i:
#             print()
#     print(s,'\n',end='')
'''27'''
# n=int(input('n='))
# for i in range(1,n+1):
#     if i%2==1:
#         for x in range(i):
#             if x%2==1:
#                 print(0,end='')
#             if x%2==0:
#                 print(1,end=(''))
#         print('\n',end='')
#     if i%2==0:
#         for x in range(i):
#             if x%2==1:
#                 print(1,end='')
#             if x%2==0:
#                 print(0,end=(''))
#         print('\n',end='')
'''27 optimali'''
# n = int(input("N = "))
# a = 1
# for i in range(n):
#     for j in range(i+1):
#         print(a,end='')
#         a = 0 if a==1 else 1
#     a = 0 if i%2==0 else 1
#     print()
'''24 archa masalasi'''
# n = int(input("N = "))
# for i in range(n):
#     print(end=' '*(n-i))
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
'''25 '''
# n=int(input('n='))
# for i in range(n):
#     print(end=' '*(n-i))
#     for j in range(i+1):
#         print(i+1,end=' ')
#     print()
'''26'''
# n=int(input('n='))
# for i in range(1,n):
#     print(end=(' ')*(n-i))
#     for j in range(i*2-1):
#         print('*',end=(''))
#     print()
'''28'''
# n=int(input('n='))
# for i in range(1,n+1):
#     print(end=' '*(n-i))
#     for j in range(i*2-1):
#         print('*',end='')
#     print()
# for x in range(n-1,0,-1):
#     print(end=' '*(n-x))
#     for y in range(x*2-1):
#         print('*',end='')
#     print()
'''29'''
# n=int(input('n='))
# s0=0;s1=1
# for i in range(n):
#     print(' '*(n-i))
#     for j in range(i+1):
#         sj=s0+s1
#         s0=s1
#         s1=sj
#         print(1,)
'''30'''
# n=int(input('n='))
# for i in range(1,n+1):
#     print(end=' '*(n-i))
#     for j in range(1,i+1):
#         print(j,end='')
#     for x in range(j-1,0,-1):
#         print(x,end=(''))
#     print()
'''31       OPTIMALLASHTIRISH KERAK'''
'''
n=int(input('n='))
for i in range(1,n+1):
    print(end=' '*(n-i))
    for j in range(i,i*2):
        print(j,end='')
    for x in range(i*2-2,i-1,-1):
        print(x,end=(''))
    print()
'''
'''
n=int(input('n='))
for i in range(n):
    for j in range(n):
        print(j,end='')
    print()
'''
'''
n=int(input('n='))
while n>0:
    q=n%2
    
    n//=2
print(q)
'''
'''n kiritilgan sonning birinchi va oxirgi raqamini chiqaruvchi dastur'''
# n=int(input('n='))
# k=n%10
# while n>9:
#     n//=10
# print(n,k)
'''
a=int(input('a='))
b=int(input('b='))
s=0
for i in range(a,b+1):
    s+=i**b
    b-=1
print(s)
'''
'''
a=int(input('a='))
b=int(input('b='))
for i in range(a,b+1):
    print((str(i)+' ')*(i-a+1),end='')
'''

# sana=0;x=True
# while True:
#     a=int(input('a='))
#     if x:
#         mi=ma=a
#         x=False
#     if a>0:
#         sana+=1
#     if a==-1:
#         break
#     if ma<a:
#         ma=a
#     if mi>a:
#         mi=a
# print(f"max={ma}, {sana} ta musbat, min={mi}")
# Program to check if a number is prime or not
'''
num = 50

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
'''
# from math import sqrt
# n=int(input('n='))
# s=1;i=3
# print(2,end=' ')
# while True:
#     tub=True
#     for j in range(3,int(sqrt(i))+1,2):
#         if i%j==0:
#             tub=False
#             break
#     if tub:
#         print(i,end=' ')
#         s+=1
#     if s==n:
#         break
#     i+=2
'''
n=int(input('n='))
for i in range(n,1-1,-1):
    for j in range(1,n+1):
        if j==i:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
'''
# Chala
n=int(input('n='))
s=0;b=0
while n>0:
    q=n%2
    n//=2
    s+=q*10**b
    b+=1
print(s)

    

