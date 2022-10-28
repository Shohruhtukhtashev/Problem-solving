# -*- coding: utf-8 -*-
"""
11-dars
"""
#23
'''
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
a=a+b+c
b=a-b-c
c=a-b-c
a=a-c-b
print(a,b,c)
'''
#24
'''
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
a=a+b+c
c=a-b-c
b=a-c-b
a=a-c-b
print(a,b,c)
'''
#25
'''x=int(input('x='))
y=3*pow(x,6)-6*x*x-7
print(f"y={y}")
'''
#26
'''
x=int(input('x='))
y=4*(x-3)**6-7*(x-3)**3+2
print(y)'''
#27
'''a=int(input('A='))
print(f"a*a={a*a}")
print(f"a^4={pow(a,4)}")
print(f"a^8={pow(a,8)}")
'''
##28
# a=int(input('A='))
# print(f"a*a={a*a}")
# print(f"a^3={a**3}")
# print(f"a^5={a**5}")
# print(f"a^10={a**10}")
# print(f"a^15={a**15}")
##29
# import math
# a=float(input('a='))
# rad=a/180*math.pi
# print(rad)
'''30'''
# import math
# a=float(input('a='))
# grad=a/math.pi*180
# print(grad)
'''31'''
# Tf=float(input('Tf='))
# Tc=(Tf-32)*5/9
# print(Tc)
'''33'''
# x=int(input('x='))
# a=int(input('a='))
# y=int(input('y='))
# kg=a/x
# ykg=(y*a)/x
# s=kg+ykg
# print(s)
'''34'''
# x=int(input('x='))
# a=int(input('a='))
# y=int(input('y='))
# b=int(input('b='))
# kg_sh=a/x
# kg_k=b/y
# print(kg_sh-kg_k)
'''35'''
# v_q=int('Qayiqning tezligi:')
# v_d=int(input('Daryoning tezligi: '))
# t1=int(input("t1="))
# t2=int(input("t2="))
# s=(v1+v2)*t1+(v1-v2)*t2
# print(s)
'''36'''
# v1=int(input())
# v2=int(input())
# s=int(input())
# t=int(input())
# s_u=s+(v1+v2)*t
# print(s_u)
'''37'''
# v1=int(input())
# v2=int(input())
# s=int(input())
# t=int(input())
# s_u=s-(v1+v2)*t
# print(s_u)
'''38'''
# a=int(input())
# b=int(input())
# x=-b/a
# print(x)
'''39'''
# a=int(input())
# b=int(input())
# c=int(input())
# d=b*b-4*a*c
# x1=(-b+d**(1/2))/(2*a)
# x2=(-b-d**(1/2))/(2*a)
# print(x1)
# print(x2)
'''40'''
# a1=int(input())
# b1=int(input())
# c1=int(input())
# a2=int(input())
# b2=int(input())
# c2=int(input())
# d=a1*b2-a2*b1
# x=(c1*b1-c2*b1)/d
# y=a1*c1-a2*c1
# print(d,x,y)
for i in range(1,101):
	if i%2==0:print(3*2-1)
	else:print(i**2)