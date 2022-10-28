#integer1
'''sm=int(input("sm birligidagi uzunlikni kiriting: "))
m=sm/100
print(f"{sm}sm {m}m ga teng.")
'''
#integer2
'''kg=int(input("kg birligidagi og'irlikni kiriting: "))
tonna=kg/1000
print(f"{kg}kg {tonna}tonnaga teng.")
'''
#integer3
'''bayt=int(input("Baytdagi ma'lumotni kiriting: "))
kbayt=bayt/1024
print(f"{bayt} bayt {kbayt}Kbaytga teng")
'''
#integer4
'''DigetA=int(input("Birinchi musbat sonni kiriting: "))
DigetB=int(input("Ikkinchi musbat sonni kiriting: "))
aDivisionb=DigetA/DigetB
print(f"A kesmada B kesmani {int(aDivisionb)} marta joylashtirish mumkin.")
'''
#integer5
'''DigetA=int(input("Birinchi musbat sonni kiriting: "))
DigetB=int(input("Ikkinchi musbat sonni kiriting: "))
aDivisionb=DigetA/DigetB
aResidueb=DigetA%DigetB
print(f"A kesmada B kesmani {int(aDivisionb)} marta joylashtirish mumkin. Joylashmagan qismi esa {aResidueb} ga teng.")
'''
#integer6
'''son=input("Ikki xonali son kiriting: ")
ten=son[0]
one=son[1]
print(ten)
print(one)
'''
#integer7
'''son1=int(input("Birinchi sonni kiriting:"))
son2=int(input("Ikkinchi sonni kiriting: "))
yig=son1+son2
print(f"Ularning yig'indis {yig} ga teng.")
'''
#integer8
'''son=int(input("Ikki xonali son kiriting: "))
ten=son//10
one=son%10
print(one*10+ten)
'''
#integer9
'''son=input("Uch xonni kiriting: ")
hundred=son//100
print(hundred)
'''
#integer10
'''son=input("Uch xonali son kiriting: ")
one=son%10
ten=son%100//10
hundred=son//100
print(one)
print(ten)
print(hundred)
'''
#integer11
'''son=int(input("Uch xonali son kiriting: "))
hundred=son//100
ten=son%100//10
one=son%10
yig=hundred+ten+one
print(f"Raqamlar yig'indisi {yig} ")
'''
#integer12
'''son=int(input("Uch xonali son kiriting: "))
yuz=son//100
onlik=son%100//10
bir=son%10
print(100*bir+10*onlik+yuz)
'''
#integer13
'''
son=int(input("Uch xonali son kiriting: "))
hundred=son//100
ten=son%100//10
one=son%10
print(ten*100+one*10+hundred)
'''
#integer14
'''son=int(input("Uch xonali son kiriting: "))
hundred=son//100
ten=son%100//10
one=son%10
print(one*100+hundred*10+ten)
'''
#integer15
'''son=int(input("Uch xonali son kiriting: "))
hundred=son//100
ten=son%100//10
one=son%10
print(ten*100+hundred*10+one)
'''
#integer16
'''son=int(input("Uch xonali son kiriting: "))
hundred=son//100
ten=son%100//10
one=son%10
print(hundred*100+one*10+ten)
'''
#integer17
'''son=int(input("999 dan katta son kiriting: "))
hundred=son%1000//100
print(f"Yuzliklar xonasidagi raqam {hundred} ga teng")
'''
#INTEGER18
'''son=int(input("999 dan katta son kiriting: "))
ming=son//1000
print(f"Minglar xonasidagi raqam {ming} ga teng")
'''
#integer19
'''sekund=int(input("Sekund birligidagi vaqtni kiriting: "))
minut=sekund//60
print(f"{sekund} sekund to'la {minut} minutga teng.")
'''
#integer20
'''sekund=int(input("Sekund birligidagi vaqtni kiriting: "))
soat=sekund//3600
print(f"{sekund} sekund to'la {soat} soatga teng.")
'''
#integer21
'''sekund=int(input("Sekund birligidagi vaqtni kiriting: "))
s=sekund
minut=sekund//60
sekund=sekund%60
print(f"{s} sekund {minut} minut {sekund} sekundaga teng.")
'''
#integer22
'''sekund=int(input("Sekund birligidagi vaqtni kiriting: "))
s=sekund
soat=sekund//3600
sekund=sekund%60
print(f"{s} sekund {soat} soat {sekund} sekundaga teng.")
'''
#integer23
'''sekund=int(input("Sekund birligidagi vaqtni kiriting: "))
s=sekund
soat=sekund//3600
minut=sekund%3600//60
sekund=sekund%60
print(f"{s} sekund {soat} soat {minut} minut {sekund} sekundaga teng.")
'''
#integer24 1-yanvar dushanba bo'lganda
'''k=int(input('k='))
print(f"{k}-kun haftaning {k%7} kuni bo'ladi.")
'''
#integer25 1-yanvar seshanba bo'lganda.
'''k=int(input('k='))
b=(k+1)%7
print(f"{k}-kun haftaning {b}-kuni bo'ladi")
'''
#integer26 k qaysi kunligi. n 1-yanvar haftaning qaysi kuni bo'ishi.
'''
k=int(input('k='))
n=int(input('n='))
f=(k+n-1)%7
print(f"{k}-kun haftaning {f}-kuni bo'ladi")
'''
#integer29
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
turt_yuzi=a*b
kvad_yuzi=c*c
print(f"To'g'ri turtburchakka {turt_yuzi//kvad_yuzi}ta kvadrat sig'adi va {turt_yuzi%kvad_yuzi}qismi sig'maydi")
#integer30
'''yil=int(input("Yilni kiriting: "))
yuz=yil//100
print(f"{yuz+1}- asrga teng.")
'''
#Kiritilgan sonning 1000 chi xonada joylashgan raqamini chiqarib beradi.
'''a=int(input('a='))
b=a%10000//1000
print(b)
'''
a=18827772
b=a%1000
c=a//1000
print(str(b)+str(c))
