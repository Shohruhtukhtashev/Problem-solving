#if1
'''a=int(input('a='))
if a>0:
    print(a+1)
else:
    print(a)

'''
#if2
import math

'''a=int(input('a='))
if a>0:
    print(a+1)
else:
    print(a-2)


'''
#if3
'''a=int(input('a='))
if a==0:
    a=10
if a>0:
    print(a+1)
else:
    print(a-2)
'''
#if4
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a>0 and b>0 and c>0:
    print(3)
elif a>0 and b>0 or a>0 and c>0 or b>c and c>0:
    print(2)
elif a>0 or b>0 or c>0:
    print(1)
else:
    print('musbat son yuq')
'''
#if5
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a>0 and b>0 and c>0:
    print('3 ta musbat')
elif a>0 and b>0 or a>0 and c>0 or b>c and c>0:
    print('2 ta musbat va 1 ta maniy')
elif a>0 or b>0 or c>0:
    print("1 ta musbat va 2 manfiy")
else:
    print('3 ta manfiy')
'''
#optimal yechim
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
s=0
if a>0:
    s=s+1
if b>0:
    s=s+1
if c>0:
    s=s+1
print(s,'ta musbat va',3-s,'ta manfiy')
'''
#if6
'''a=int(input('a='))
b=int(input('b='))
if a>b:
    print(a)
else:print(b)
'''
#if7
'''a=int(input('a='))
b=int(input('b='))
if a>b:
    print(b)
'''
#if8
'''a=int(input('a='))
b=int(input('b='))
if a>b:
    print(a,b)
else:print(b,a)
'''
#if9
'''a=float(input('a='))
b=float(input('b='))
if a>b:
    print(b,a)
else:print(a,b)
'''
#if10
'''a=int(input('a='))
b=int(input('b='))
if a!=b:
    a=a+b
    print(f"a={a}, b={a}")
else:
    a,b=0,0
    print('a=',a,'b=',b)
'''
#if11
'''a=int(input('a='))
b=int(input('b='))
if a!=b:
    if a>b:
        print(f"a={a}, b={a}")
    else:print(f"a={b}, b={b}")
else:
    a,b=0,0
    print('a=',a,'b=',b)

'''
#if12
'''a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a>=b>=c or b>=a>=c:
    print(c)
elif a>=c>=b or c>=a>=b:
    print(b)
else:
    print(a)

'''
#if13
'''a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a>b>c or c>b>a:
    print(b)
elif b>a>c or c>a>b:
    print(a)
else:
    print(c)
'''
#if14
'''a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a>b>c:print(c,a)
elif c>b>a:print(a,c)
elif b>a>c:print(c,b)
elif c>a>b:print(b,c)
elif a>c>b:print(b,a)
elif b>c>a:print(a,b)
'''
#if15
'''a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a>=b>c:
    print(a,b)
elif a>=c>b:
    print(a,c)
elif b>=a>c:
    print(b,a)
elif b>=c>a:
    print(b,c)
elif c>=a>b:
    print(a,c)
elif c>=b>a:
    print(b,c)

'''
#optimal yechim
'''
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a>b<c:
    print(a,c)
elif a>c<b:
    print(a,b)
else:
    print(b,c)
'''
#if16
'''a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a<b<c:
    print(2*a,2*b,2*c)
else:
    print(-a,-b,-c)

'''
#if17
'''a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a<b<c or a>b>c:
    print(2*a,2*b,2*c)
else:
    print(-a,-b,-c)

'''
#if18
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a==b:
    print(3)
elif a==c:
    print(2)
else:
    print(1)

'''
#if19
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))
if a==b==c:
    print(4)
elif a==b==d:
    print(3)
elif b==c==d:print(1)
elif a==c==d:print(2)
else:
    print('Uchta bir xil son kiritmadingiz')

'''
#if20
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a-b<a-c:
    print(abs(a-b))
else:print(abs(a-c))
'''
#if21
'''x=int(input('x='))
y=int(input('y='))
if x==y==0:print(0)
elif y==0:print(1)
elif x==0:print(2)
else:print(3)
'''
#if22
'''x=int(input('x='))
y=int(input('y='))
if x>0 and y>0:print('Nuqta 1-chorakda joylashgan')
elif x<0 and y>0:print('Nuqta 2-chorakda joylashgan')
elif x<0 and y<0:print('Nuqta 3-chorakda joylashgan')
else:print('Nuqta 4-chorakda joylashgan')
'''
#if23
'''
'''
#if24
'''x=int(input('x='))
if x<=0:print(x-6)
else:print(2*math.sin(x))
'''
#if25
'''x=int(input('x='))
if x<-2 or x>2:print(2*x)
else:print(-3*x)
'''
#if26
'''x=float(input('x='))
if x<=0:print(-x)
if 0<x<2:print(x*x)
if x>=2:print(4)
'''
#if27
'''x=int(float(input('x=')))
if x<0:print(0)
elif x>=0 and x%2==0:print(1)
elif x>0 and x%2:print(-1)
'''
#if28
'''yil=int(input('yil='))
kabisa=False
if yil%4==0:
    kabisa=True
if yil%100==0 and yil%400!=0:
    kabisa=False

if kabisa:
    print('kabesa')
else:
    print('kabesa emas')
'''
#if29
'''son=int(input('Butun son kiriting: '))
if son>0 and son%2==0:
    print('Musbat juft son')
if son>0 and son%2!=0:
    print('Musbat toq son')
if son<0 and son%2==0:
    print('Manfiy juft son')
if son<0 and son%2!=0:
    print('Manfiy toq son')
if son==0:
    print('Son nolga teng')
'''
#if30
'''son=int(input('1-999 oraliqda butun son kiriting: '))
if son//100!=0 and son%2==0:
    print('Uch xonali juft son')
elif son//100!=0 and son%2!=0:print('Uch xonali toq son')
if son//100==0 and son%100//10!=0 and son%2==0:
    print('Son ikki xonali juf')
elif son//100==0 and son%100//10!=0 and son%2!=0:print('Son ikki xonali toq')
if son//100==0 and son%100//10==0 and son%2==0:
    print('Son 1 xonali juf')
elif son//100==0 and son%100//10==0 and son%2!=0:print('Son 1 xonali toq')
'''
#if31
'''n=int(input('1-99 oralig\'ida son kiriting: '))
if n//10==0:
    if n%10==0:f='nol'
    if n%10==1:f='bir'
    if n%10==2:f='ikki'
    if n%10==3:f='uch'
    if n%10==4:f='to\'rt'
    if n % 10 == 5: f = 'besh'
    if n % 10 == 6: f = 'olti'
    if n % 10 == 7: f = 'yetti'
    if n % 10 == 8: f = 'sakkiz'
    if n % 10 == 9: f = 'to\'qqiz'
if n//10!=0:
    if n==10:f='o\'n'
    if n == 11: f = 'o\'n bir'
    if n == 12: f = 'o\'n ikki'
    if n == 13: f = 'o\'n uch'
    if n == 14: f = 'o\'n to\'rt'
    if n == 15: f = 'o\'n besh'
    if n == 16: f = 'o\'n olti'
    if n == 17: f = 'o\'n yetti'
    if n == 18: f = 'o\'n sakkiz'
    if n == 19: f = 'o\'n to\'qqiz'
    if n == 20: f = 'yigirma '
    if n == 21: f = 'yigirma bir'
    if n == 22: f = 'yigirma ikki'
    if n == 23: f = 'yigirma uch'
    if n == 24: f = 'yigirma to\'rt'
    if n == 25: f = 'yigirma besh'
    if n == 26: f = 'yigirma olti'
    if n == 27: f = 'yigirma yetti'
    if n == 28: f = 'yigirma sakkiz'
    if n == 29: f = 'yigirma to\'qqiz'
    if n == 30: f = 'uttiz '
    if n == 31: f = 'uttiz bir'
    if n == 32: f = 'uttiz ikki'
    if n == 33: f = 'uttiz uch'
    if n == 34: f = 'uttiz to\'rt'
    if n == 35: f = 'uttiz besh'
    if n == 36: f = 'uttiz olti'
    if n == 37: f = 'uttiz yetti'
    if n == 38: f = 'uttiz sakkiz'
    if n == 39: f = 'uttiz to\'qqiz'
    if n == 40: f = 'qirq '
    if n == 41: f = 'qirq bir'
    if n == 42: f = 'qirq ikki'
    if n == 43: f = 'qirq uch'
    if n == 44: f = 'qirq to\'rt'
    if n == 45: f = 'qirq besh'
    if n == 46: f = 'qirq olti'
    if n == 47: f = 'qirq yetti'
    if n == 48: f = 'qirq sakkiz'
    if n == 49: f = 'qirq to\'qqiz'
    if n == 50: f = 'ellik '
    if n == 51: f = 'ellik bir'
    if n == 52: f = 'ellik ikki'
    if n == 53: f = 'ellik uch'
    if n == 54: f = 'ellik to\'rt'
    if n == 55: f = 'ellik besh'
    if n == 56: f = 'ellik olti'
    if n == 57: f = 'ellik yetti'
    if n == 58: f = 'ellik sakkiz'
    if n == 59: f = 'ellik to\'qqiz'
    if n == 60: f = 'oltmish '
    if n == 61: f = 'oltmish bir'
    if n == 62: f = 'oltmish ikki'
    if n == 63: f = 'oltmish uch'
    if n == 64: f = 'oltmish to\'rt'
    if n == 65: f = 'oltmish besh'
    if n == 66: f = 'oltmish olti'
    if n == 67: f = 'oltmish yetti'
    if n == 68: f = 'oltmish sakkiz'
    if n == 69: f = 'oltmish to\'qqiz'
    if n == 70: f = 'yetmish '
    if n == 71: f = 'yetmish bir'
    if n == 72: f = 'yetmish ikki'
    if n == 73: f = 'yetmish uch'
    if n == 74: f = 'yetmish to\'rt'
    if n == 75: f = 'yetmish besh'
    if n == 76: f = 'yetmish olti'
    if n == 77: f = 'yetmish yetti'
    if n == 78: f = 'yetmish sakkiz'
    if n == 79: f = 'yetmish to\'qqiz'
    if n == 80: f = 'sakson '
    if n == 81: f = 'sakson bir'
    if n == 82: f = 'sakson ikki'
    if n == 83: f = 'sakson uch'
    if n == 84: f = 'sakson to\'rt'
    if n == 85: f = 'sakson besh'
    if n == 86: f = 'sakson olti'
    if n == 87: f = 'sakson yetti'
    if n == 88: f = 'sakson sakkiz'
    if n == 89: f = 'sakson to\'qqiz'
    if n == 90: f = 'to\'qson '
    if n == 91: f = 'to\'qson bir'
    if n == 92: f = 'to\'qson ikki'
    if n == 93: f = 'to\'qson uch'
    if n == 94: f = 'to\'qson to\'rt'
    if n == 95: f = 'to\'qson besh'
    if n == 96: f = 'to\'qson olti'
    if n == 97: f = 'to\'qson yetti'
    if n == 98: f = 'to\'qson sakkiz'
    if n == 99: f = 'to\'qson to\'qqiz'

print(f)

'''
#if32
'''a=int(input('a='))
onlik=a//10
birlik=a%10

if onlik==1:
    print("O'n")
if onlik==2:
    print("Yigirma")
if onlik==3:
    print("Uttiz")
if onlik==4:
    print("Qirq")
if onlik==5:
    print("Ellik")
if onlik==6:
    print("Oltmish")
if onlik==7:
    print("Yetmish")
if onlik==8:
    print("Sakson")
if onlik==9:
    print("To'qson")
if birlik==1:
    print("bir")
if birlik==2:
    print("Ikki")
if birlik==3:
    print("Uch")
if birlik==4:
    print("To'rt")
if birlik==5:
    print("Besh")
if birlik==6:
    print("Olti")
if birlik==7:
    print("Yetti")
if birlik==8:
    print("Sakkiz")
if birlik==9:
    print("To'qqiz")
'''
#if33
m='Million'
yu="Yuz"
mi="Ming"
bi='Bir'
i='Ikki'
u='Uch'
tu="To'rt"
b="Besh"
o="Olti"
y="Yetti"
s="Sakkiz"
t="To'qqiz"

a=int(input("1-9 999 999 oraliqdagi sonni kiriting: "))
million=a//1000000
yuz_ming=a%1000000//100000
on_ming=a%1000000%100000//10000
ming=a%1000000%100000%10000//1000
yuz=a%1000000%100000%10000%1000//100
onlik=a%1000000%100000%10000%1000%100//10
birlik=a%10
if million>9:
    print("Siz berilgan oraliqdagi sonni kiritmdingiz.\nIltimos oraliqga e'tibor bering!")
elif million<=9:
    if million == 1:
        print(bi, m, end=' ')
    if million == 2:
        print(i, m, end=' ')
    if million == 3:
        print(u, m, end=' ')
    if million == 4:
        print(tu, m, end=' ')
    if million == 5:
        print(b, m, end=' ')
    if million == 6:
        print(o, m, end=' ')
    if million == 7:
        print(y, m, end=' ')
    if million == 8:
        print(s, m, end=' ')
    if million == 9:
        print(t, m, end=' ')

    if yuz_ming == 1:
        print(bi, yu, end=' ')
    if yuz_ming == 2:
        print(i, yu, end=' ')
    if yuz_ming == 3:
        print(u, yu, end=' ')
    if yuz_ming == 4:
        print(tu, yu, end=' ')
    if yuz_ming == 5:
        print(b, yu, end=' ')
    if yuz_ming == 6:
        print(o, yu, end=' ')
    if yuz_ming == 7:
        print(y, yu, end=' ')
    if yuz_ming == 8:
        print(s, yu, end=' ')
    if yuz_ming == 9:
        print(t, yu, end=' ')

    if on_ming == 1:
        print("O'n", end=' ')
    if on_ming == 2:
        print("Yigirma", end=' ')
    if on_ming == 3:
        print("Uttiz", end=' ')
    if on_ming == 4:
        print("Qirq", end=' ')
    if on_ming == 5:
        print("Ellik", end=' ')
    if on_ming == 6:
        print("Oltmish", end=' ')
    if on_ming == 7:
        print("Yetmish", end=' ')
    if on_ming == 8:
        print("Sakson", end=' ')
    if on_ming == 9:
        print("To'qson", end=' ')

    if on_ming != 0 and ming == 0 or ming == 0 and yuz_ming != 0:
        print(mi, end=' ')
    if ming == 1:
        print(bi, mi, end=' ')
    if ming == 2:
        print(i, mi, end=' ')
    if ming == 3:
        print(u, mi, end=' ')
    if ming == 4:
        print(tu, mi, end=' ')
    if ming == 5:
        print(b, mi, end=' ')
    if ming == 6:
        print(o, mi, end=' ')
    if ming == 7:
        print(y, mi, end=' ')
    if ming == 8:
        print(s, mi, end=' ')
    if ming == 9:
        print(t, mi, end=' ')

    if yuz == 1:
        print(bi, yu, end=' ')
    if yuz == 2:
        print(i, yu, end=' ')
    if yuz == 3:
        print(u, yu, end=' ')
    if yuz == 4:
        print(tu, yu, end=' ')
    if yuz == 5:
        print(b, yu, end=' ')
    if yuz == 6:
        print(o, yu, end=' ')
    if yuz == 7:
        print(y, yu, end=' ')
    if yuz == 8:
        print(s, yu, end=' ')
    if yuz == 9:
        print(t, yu, end=' ')

    if onlik == 1:
        print("O'n", end=' ')
    if onlik == 2:
        print("Yigirma", end=' ')
    if onlik == 3:
        print("Uttiz", end=' ')
    if onlik == 4:
        print("Qirq", end=' ')
    if onlik == 5:
        print("Ellik", end=' ')
    if onlik == 6:
        print("Oltmish", end=' ')
    if onlik == 7:
        print("Yetmish", end=' ')
    if onlik == 8:
        print("Sakson", end=' ')
    if onlik == 9:
        print("To'qson", end=' ')

    if birlik == 1:
        print("bir")
    if birlik == 2:
        print("Ikki")
    if birlik == 3:
        print("Uch")
    if birlik == 4:
        print("To'rt")
    if birlik == 5:
        print("Besh")
    if birlik == 6:
        print("Olti")
    if birlik == 7:
        print("Yetti")
    if birlik == 8:
        print("Sakkiz")
    if birlik == 9:
        print("To'qqiz")
    if a == 0:
        print("Nol")
