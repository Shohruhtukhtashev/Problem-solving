#Boolean1
'''a=int(input('a soni musbat a='))
b=a>0
print(b)
'''
#Boolean2 a soni toq son
'''a=int(input('a='))
print(a%2!=0)
'''
#Boolean3 a soni juft son
'''a=int(input('a='))
print(a%2==0)
'''
#Boolean4
'''a=int(input('a='))
b=int(input("b="))
print(a>2 and b<=3)
'''
#Boolean5
'''a=int(input('a='))
b=int(input("b="))
print(a>=0 or b<-2)
'''
#Boolean6
'''a=int(input('a='))
b=int(input("b="))
c=int(input("b="))
print(a<=b<=c)
'''
#Boolean7
'''a=int(input('a='))
b=int(input("b="))
c=int(input("b="))
print(a<b<c)
'''
#Boolean8 a va b sonlari toq sonlar true
'''a=int(input('a='))
b=int(input("b="))
print(a%2!=0 and b%2!=0)
'''
#Boolean9
'''a=int(input('a='))
b=int(input("b="))
print(a%2!=0 or b%2!=0)
'''
#Boolean10
'''a=int(input('a='))
b=int(input("b="))
print((a%2!=0 or b%2!=0) and (a%2==0 or b%2==0))
'''
#Boolean11
'''a=int(input('a='))
b=int(input("b="))
print((a%2==0 and b%2==0) or (a%2!=0 and b%2!=0))
'''
#Boolean12
'''a=int(input('a='))
b=int(input("b="))
c=int(input("c="))
print(a>0 and b>0 and c>0)
'''
#Boolean13
'''a=int(input('a='))
b=int(input("b="))
c=int(input("c="))
print(a>0 or b>0 or c>0)
'''
#Boolean14 Faqat bittasi musbat bo'lsa.
'''a=int(input('a='))
b=int(input("b="))
c=int(input("c="))
print((a>0 and b<0 and c<0) or (b>0 and a<0 and c<0) or (c>0 and b<0 and a<0))
'''
#Boolean15 Faqat ikkitasi musbat
'''a=int(input('a='))
b=int(input("b="))
c=int(input("c="))
print((a>0 and b>0 and c<0) or (b<0 and a>0 and c>0) or (c>0 and b>0 and a<0))
'''
#Boolean16 Berilgan son ikki xonali juft son. True
'''a=int(input('a='))
ten=a//100==0
juft=a%2==0
print(ten and juft)
'''
#Boolean17 Berilgan son uch xonali toq. True
'''a=int(input('a='))
ten=a//1000==0 and a//100!=0
toq=a%2!=0
print(ten and toq)
'''
#Boolean18
'''a=int(input('a='))
b=int(input("b="))
c=int(input("c="))
print((a==b and a==c or b==c) or (a==b and b==c or a==c) or (b==c and a==c or a==b))
'''
#Boolean19
'''
a=int(input('a='))
b=int(input("b="))
c=int(input("c="))
print(a==-b or a==-c or b==-c)
'''
#Boolean20
'''a=int(input("Uch xonali son kiriting: "))
b=a//100
c=a%100//10
d=a%10
print(b!=c and b!=d and c!=d)
print(b!=c!=d)
'''
#Boolean21
'''a=int(input("Uch xonali son kiriting: "))
b=a//100
c=a%100//10
d=a%10
print(b<c<d)
'''
#Boolean22
'''a=int(input("Uch xonali son kiriting: "))
hundred=a//100
ten=a%100//10
one=a%10
print(hundred<ten<one or hundred>ten>one)
'''
#Boolean23
'''a=int(input("Uch xonali son kiriting: "))
hundred=a//100
ten=a%100//10
one=a%10
print(hundred==one)
'''
#Boolean24
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
a>0
d=b*b-4*a*c
print(d>=0)
'''
#Boolean25
'''x=int(input('x='))
y=int(input('y='))
print(x<0 and y>0)
'''
#Boolean26
'''x=int(input('x='))
y=int(input('y='))
print(x>0 and y<0)
'''
#Boolean27
'''x=int(input('x='))
y=int(input('y='))
print((x<0 and y>0) or (x<0 and y<0))
'''
#Boolean28
'''x=int(input('x='))
y=int(input('y='))
print((x>0 and y>0) or (x<0 and y<0))
'''
#Boolean29
'''x=int(input('x='))
y=int(input('y='))
x1=int(input('x1='))
y1=int(input('y1='))
x2=int(input('x2='))
y2=int(input('y2='))
print((x<x2 and y<y1) or (x>x1 and y> y2))
print(x1<x<x2 and y2<y<y1)
'''
#Boolean30
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
print(a==b and a==c and b==c)
'''
#Boolean31
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
print((a==b and b!=c) or (a==c and c!=b) or (b==c and c!=a))
'''
#Boolean32
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
print(a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b)
'''
#Boolean33
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
print(a<b+c and b<a+c and c<a+b)
'''
#Boolean34
'''x=int(input('x='))
y=int(input('y='))
print((x+y)%2!=0)
'''
#Boolean35
'''x1=int(input('x1='))
y1=int(input('y1='))
x2=int(input('x2='))
y2=int(input('y2='))
print((x1+y1)%2!=0 and (x2+y2)%2!=0 or (x1+y1)%2==0 and (x2+y2)%2==0)
'''
#Boolean36
'''x1=int(input('x1='))
y1=int(input('y1='))
x2=int(input('x2='))
y2=int(input('y2='))
print(x1==x2 or y1==y2)
'''
#Boolean37

#Boolean38
#Boolean39
x1=int(input('x1='))
y1=int(input('y1='))
x2=int(input('x2='))
y2=int(input('y2='))
print(abs(x1-x2)==abs(y1-y2) or x1==x2 or y1==y2)
#Boolean40
x1=int(input('x1='))
y1=int(input('y1='))
x2=int(input('x2='))
y2=int(input('y2='))
print((x1==x2 or abs(y1-y2)==1) and (y1==y2 or abs(x1-x2)==1))
