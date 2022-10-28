import math
#Begin1
'''
a=int(input("Kvadratning tomonini kiriting: "))
P=4*a
print(f"Kvadratning perimetri {P} ga teng")
'''
#Begin2
'''
a=int (input("Kvadratning tomonini kiriting: "))
S=a*a
print(f"vadratning yuzasi {S} ga teng.")
'''
#Begin3
'''a=5
b=10
S=a*b
P=2*(a+b)
print(f"To'g'ri to'rtburchakni yuzasi {S} ga va perimetri {P} ga teng.")
'''
#Begin4
'''d=5
pi=3.14
L=pi*d
print(f"Aylananing uzunligi {L}ga teng.")
'''
#Begin5
'''a=5
V=a**3
S=6*(a**2)
print(f"Kubning hajmi {V} ga, va to'la sirtining hajmi {S} ga teng.")
'''
#Begin6
'''a=1
b=2
c=3
V=a*b*c
S=2*(a*b+b*c+a*c)
print(f"Paralelopepedning hajmi {V} ga va To'la sirti {S} ga teng.")
'''
#Begin 7
'''r=3
L=2*math.pi*r
S=math.pi*r*r
print(F"Doiraning uzunligi {L} ga teng, va yuzasi {S} ga teng.")
'''
#Begin 8
'''a=4
b=6
print(f"Ularning o'rta arifmetigi {(a+b)/2} ga teng.")
'''
#Begin 9
'''a=4
b=9
print(f"Ularning o'rta geometrigi {math.sqrt(a*b)}")
'''
#Begin 10
'''a=12
b=15
print(f"Ularning yig'indisi {a+b} ga teng.")
print(f"Ularning ko'paytmasi {a*b} ga teng.")
print(f"{a} ning kvadrati {a*a} ga, va {b} ning kvadrati {b*b} ga teng.")
'''
#Begin 11
'''a=-43
b=23
print(f"{a} ning moduli {math.m}")
'''
#Begin 12
'''a=4
b=3
c=math.sqrt(a*a+b*b)
P=a+b+c
print(f"To'g'ri burchakli uchburchaknikg gipotinuzasi {c} ga, va perimetri {P} ga teng.")
'''
#Begin 13
'''r1=10
r2=15
S1=math.pi*r1
S2=math.pi*r2
S3=math.pi*(r1-r2)
print(f"Ularning yuzalari S1={S1} ga,\n S2={S2} ga,\n S3={S3} ga teng.")
'''
#Begin 14
'''L=100
R=L/(2*math.pi)
S=math.pi*R*R
print(f"Aylananing radiusi {R} ga, va Yuzasi {S} ga teng.")
'''
#Begin 15
'''S=25
r=math.sqrt(S/math.pi)
d=2*r
print(f"Aylananing radius {r} ga, va diametri {d} ga teng.")
'''
#Begin 16
'''x1=3
x2=-5
print(f"Ikki nuqta orasidagi masofa {math.fabs(x2-x1)} ga teng.")
'''
#Begin 17
'''a=12
b=13
c=15
lenAC=c-a
lenBC=c-b
lenAB=b-a
len=lenAB+lenBC+lenAC
print(f"AC kesmaning uzunligi {lenAC} ga, va BC kesmaning uzunligi {lenBC} ga,\nKesmalar uzunligini yig'indisi {len} ga teng.")
'''
#Begin 18
'''a=10
c=15
b=20
lenAC=c-a
lenBC=b-c
kopaytma=lenAC*lenBC
print(f"AC va BC kesmalar ko'paytmasi {kopaytma} ga teng.")
'''
#Begin 19
'''x1=10
y1=15
x2=30
y2=20
a=y2-y1
b=x2-x1
S=a*b
P=2*(a+b)
print(f"To'g'ri to'rtrburchakning yuzasi: {S},\nPerimetri {P} ga teng.")
'''
#Begin 20
'''x1=10
x2=30
y1=15
y2=40
l=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f"Ikki nuqta orasidagi masofa {l} ga teng.")
'''
#Begin 22
'''a=25
b=35
c=a
a=b
b=c
print(a,b)
'''
#Begin 23
'''a=55
b=33
c=30
var=a
a=b
b=c
c=var
print(a,b,c)
'''
#Begin 24
'''a=55
b=33
c=30
var=a
a=c
c=b
b=var
print(a,b,c)
'''
#Begin 25
'''x=1
y=3*x**6-6*x**2-7
print(y)
'''
#Begin 26
'''x=1
y=4*(x-3)**6-7*(x-3)**3+2
print(y)
'''
#Begin 27
'''a=2
print(f"{a} ning kvadrati: {a**2},\n{a} ning turtinchisi {a**4},\n{a} ning sakkizinchisi {a**8} ga teng.")
'''
#Begin 29
'''grad=90
rad=(grad*math.pi)/180
print(f"{grad} gradus {rad} radianga teng.")
'''
#Begin 30
'''rad=1.57
grad=(rad*180)/math.pi
print(f"{rad} radian {grad} gradusga teng.")
'''
#Begin 31
'''
Tf=215
Tc=(Tf-32)*5/9
print(f"{Tf} Farengeyt {Tc} Selsiyga teng.")
'''
#Begin 33
'''kg=3
som=9000
onekg=som/kg
order=int(input("Necha kg konfet olasiz: "))
cost=(order*som)/kg+onekg
print(f"1kg va {order} kg konfetning narxi {cost} so'm bo'ladi.")
'''
#Begin 34
'''x=8
a=160000
y=10
b=100000
OneKgChoca=a/x
OneKgCandy=b/y
farq=OneKgChoca-OneKgCandy
print(f"1kg chokalat 1kg konfetdan {farq} qimmat. ")
'''
#Begin 35
'''v=25
u=10
t1=2
t2=5
s1=(u+v)*t1
s2=(v-u)*t2
s=s1+s2'''
#Begin 36
'''v1=10
v2=5
t=2
s=10
s=(v1+v2)*t+s
print(f"{t} sekunddan keyin ular orasidagi masofa {s} ga teng bo'ladi.")
'''
#Begin 37
'''v1=10
v2=5
t=2
s=100
s1=v1*t
s2=v2*t
s=s-(s1+s2)
print(f"Ular orasidagi masofa {s} a teng.")
'''
#Begin 38
'''a=1
b=4
x=-b/a
print(f"x={x}")'''
#Begin 39
'''a=1
b=10
c=3
d=b*b-4*a*c
if d>0:
    x1= (-b + d ** (1 / 2))
    print(f"x1={x1}")
    x2 = (-b - d ** (1 / 2))
    print(f"x2={x2}")'''
#Begin 40
'''a1=34
b1=45
c1=47
a2=78
b2=78
c2=54
d=(a1*b1-a2*b2)
x=(c1*b2-c2*b1)/d
y=(a1*c2-a2*c1)/d
print(f"d={d}\nx={x}\ny={y}")'''