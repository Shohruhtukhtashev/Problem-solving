#Bir qatorda kod yozish
'''
a=int(input("a="))
print("Musbat") if a>0 else print("No'l") if a==0 else print("Manfiy")
'''
'''
a=int(input('a='))
a = a+2 if a>0 else 1 if a==0 else a-2
print(a)
'''
#Case1
'''a=int(input('a='))
if a==1:
    print("Dushanba")
if a==2:
    print("Seshanba")
if a==3:
    print("Chorshanba")
if a==4:
    print("Payshanba")
if a==5:
    print("Juma")
if a==6:
    print("Shanba")
if a==7:
    print("Yakshanba")
'''
#Case2
'''a=int(input("a="))
if a==1:
    print("yomon")
if a==2:
    print("qoniqarsiz")
if a==3:
    print("qoniqarli")
if a==4:
    print("yaxshi")
if a==5:
    print("a'lo")
    '''
#Case 3
'''a=int(input("a="))
if a==1 or a==2 or a==12:
    print("QISH")
if a==3 or a==4 or a==5:
    print("Bahor")
if a==6 or a==7 or a==8:
    print("Yoz")
if a==9 or a==10 or a==11:
    print("Kuz")
    '''
#Case4
'''a=int(input("a="))
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print("Bu oyda 31 kun bor")
if a==2:
    print("Bu oyda 28 yoki 29 kun bor")
if a==4 or a==6 or a==9 or a==11:
    print("Bu oyda 30 kun bor")
    '''
#Case5
'''a=float(input("a="))
b=float(input("b="))
amal=input("amal: ")
if amal=='+':
    print(a+b)
if amal=='-':
    print(a-b)
if amal=='*':
    print(a*b)
if amal=='/':
    print(a/b)
    '''
#Case 6
'''a=float(input("a="))
b=int(input("Birligi: "))
if b==1:
    print(a*0.1,'m')
if b==2:
    print(a*1000,"m")
if b==3:
    print(a,'m')
if b==4:
    print(a*0.001,'m')
if b==5:
    print(a*0.01,'m')
    '''
#Case 7
'''a=int(input('a='))
b=int(input('Birligi:'))
if b==1:
    print(a,'kg')
if b==2:
    print(a*10**(-6),'kg')
if b==3:
    print(a*10**(-3),"kg")
if b==4:
    print(a*1000,'kg')
if b==5:
    print(a*100,'kg')
    '''
#Case8
'''a=int(input('a='))
b=int(input('b='))
if b==1:
    print(a,'-yanvar')
if b==2:
    print(a,'-fevral')
if b==3:
    print(a,'-Mart')
if b==4:
    print(a,'-aprel')
if b==5:
    print(a,'-may')
if b==6:
    print(a,'-iyun')
if b==7:
    print(a,'-iyul')
if b==8:
    print(a,'-avgust')
if b==9:
    print(a,'-sentabr')
if b==10:
    print(a,'-oktabr')
if b==11:
    print(a,'-noyabr')
if b==12:
    print(b,'-dekabr')
    '''
#Case9
'''d=int(input("d="))
m=int(input("m="))
if m==1 and d<31:
    print(d+1,'-Yanvar')
elif m==1 and d==31:
    print(1,'-Fevral')
if m==2 and d<28:
    print(d+1,'-Fevral')
elif m==2 and d==28:
    print(1,'-Mart')
if m==3 and d<31:
    print(d+1,'-Mart')
elif m==3 and d==31:
    print(1,'-Aprel')
if m==4 and d<30:
    print(d+1,'-Aprel')
elif m==4 and d==30:
    print(1,'-May')
if m==5 and d<31:
    print(d+1,'-May')
elif m==5 and d==31:
    print(1,'-Iyun')
if m==6 and d<30:
    print(d+1,'-Iyun')
elif m==6 and d==30:
    print(1,'-Iyul')
if m==7 and d<31:
    print(d+1,'-Iyul')
elif m==7 and d==31:
    print(1,'Avgust')
if m==8 and d<31:
    print(d+1,'-Avgust')
elif m==8 and d==31:
    print(1,'-Sentabr')
if m==9 and d<30:
    print(d+1,'-Sentabr')
elif m==9 and d==30:
    print(1,'-Oktabr')
if m==10 and d<31: print(d+1,'-Oktabr')
elif m==10 and d==31:print(1,'-Noyabr')
if m==11 and d<30:print(d+1,'-Noyabr')
elif m==11 and d==30: print(1,'-Dekabr')
if m==12 and d<31:print(d+1,'-dekabr')
elif m==12 and d==31: print(1,'-Yanvar')
'''
#Case10
'''y=input("Robot yunalishi: ")
k=int(input("Harqkatni kiriting: "))
if y=="s" and k==0 or y=="s" and k==1 or y=="s" and k==2:
    if k==0:
        print("shimolga harakatni davom ettirdi")
    if k==1:
        print("")
        '''
#Case 11
'''c=input("Lokatrning boshlangich holatini kiriting: ")
k1=int(input('kamanda 1: '))
k2=int(input('kamanda 2: '))
if c=="s" and k1==0 and k2==0 or c=="s" and k1==1 and k2==1 or c=="s" and k1==2 and k2==0 or c=='q' and k1==1 and k2==2 or c=='q' and k1==2 and k2==1 or c=="g'" and k1==0 and k2==2 or c=="g'" and k1==2 and k2==0:
    print("janub")
if c=="s" and k1==0 and k2==1 or c=="s" and k1==1 and k2==0 or c=="s" and k1==2 and k2==2 or c=='j' and k1==0 and k2==1 or c=='j' and k1==1 and k2==0 or c=='j' and k1==2 and k2==2 or c=='q' and k1==0 and k2==1 or c=='q' and k1==1 and k2==0 or c=='q' and k1==2 and k2==2 or c=="g'" and k1==0 and k2==1 or c=="g'" and k1==1 and k2==0 or c=="g'" and k1==2 and k2==2:
    print("dastlabki holat")
if c=="s" and k1==0 and k2==2 or c=="s" and k1==2 and k2==0 or c=='j' and k1==1 and k2==2 or c=='j' and k1==2 and k2==1 or c=='q' and k1==0 and k2==0 or c=='q' and k1==1 and k2==1:
    print("g'arb")
if c=="s" and k1==1 and k2==2 or c=="s" and k1==2 and k2==1 or c=='j' and k1==0 and k2==2 or c=='j' and k1==2 and k2==0 or c=="g'" and k1==0 and k2==0 or c=="g'" and k1==1 and k2==1:
    print("sharq")

if c=='j' and k1==0 and k2==0 or c=='j' and k1==1 and k2==1 or c=='q' and k1==0 and k2==2 or c=='q' and k1==2 and k2==0 or c=="g'" and k1==1 and k2==2 or c=="g'" and k1==2 and k2==1:
    print('shimol')
    '''
#Case 12
'''a=int(input("elimentni kiriting:"))
b=int(input('uzunligini kiriting:'))
p=3.14
if a==1:
    r=b
    d = 2 * r
    l = 2 * p * r
    s = p * r * r
    print('d=',d,"l=",l,"s=",s)
if a==2:
    d=b
    r=d/2
    l=2*p*r
    s=p*r*r
    print('r=',r,"l=",l,"s=",s)
if a==3:
    l=b
    r=l/(2*p)
    d=2*r
    s=2*p*r
    print('r=',r,'d=',d,"s=",s)
if a==4:
    s=b
    r=(s/p)**(1/2)
    d=2*r
    l=2*p*r
    print(f"r={r} d={d} l={l}")
    '''
#Case 13
'''n=int(input("Karta qiymatini kiriting:"))
m=int(input("Karta turini kiriting:"))
o="olti"
y="yetti"
s="sakkiz"
t="to'qqiz"
on="o'n"
obir="valet"
oikki="dama"
ouch="qirol"
oturt="tuz"
bir="g'isht"
ikki="olma"
uch="chillak"
turt="qarg'a"
if n==6:
    if m==1:
        print(o,bir)
    if m==2:
        print(o,ikki)
    if m==3:
        print(o,uch)
    if m==4:
        print(o,turt)
if n==7:
    if m==1:
        print(y,bir)
    if m==2:
        print(y,ikki)
    if m==3:
        print(y,uch)
    if m==4:
        print(y,turt)
if n==8:
    if m==1:
        print(s,bir)
    if m==2:
        print(s,ikki)
    if m==3:
        print(s,uch)
    if m==4:
        print(s,turt)
if n==9:
    if m==1:
        print(t,bir)
    if m==2:
        print(t,ikki)
    if m==3:
        print(t,uch)
    if m==4:
        print(t,turt)
if n==10:
    if m==1:
        print(on,bir)
    if m==2:
        print(on,ikki)
    if m==3:
        print(on,uch)
    if m==4:
        print(on,turt)
if n==11:
    if m==1:
        print(obir,bir)
    if m==2:
        print(obir,ikki)
    if m==3:
        print(obir,uch)
    if m==4:
        print(obir,turt)
if n==12:
    if m==1:
        print(oikki,bir)
    if m==2:
        print(oikki,ikki)
    if m==3:
        print(oikki,uch)
    if m==4:
        print(oikki,turt)
if n==13:
    if m==1:
        print(ouch,bir)
    if m==2:
        print(ouch,ikki)
    if m==3:
        print(ouch,uch)
    if m==4:
        print(ouch,turt)
if n==14:
    if m==1:
        print(oturt,bir)
    if m==2:
        print(oturt,ikki)
    if m==3:
        print(oturt,uch)
    if m==4:
        print(oturt,turt)
'''
#Case 16
'''a=int(input("Yoshingizni kiriting: "))
onlik=a//10
birlik=a%10
if onlik==2:
    print("Yigirma", end=' ')
if onlik==3:
    print("Uttiz", end=' ')
if onlik==4:
    print("Qirq", end=' ')
if onlik==5:
    print("Ellik", end=' ')
if onlik==6:
    print("Oltmish", end=' ')

if birlik==1:
    print("bir")
if birlik==2:
    print("ikki")
if birlik==3:
    print("uch")
if birlik==4:
    print("to'rt")
if birlik==5:
    print("besh")
if birlik==6:
    print("olti")
if birlik==7:
    print("yetti")
if birlik==8:
    print("sakkiz")
if birlik==9:
    print("to'qqiz")
    '''
#Case 17
'''a=int(input("Son kiriting: "))
onlik=a//10
birlik=a%10
if onlik==1 and birlik!=0:
    print("O'n", end=' ')
if onlik==2 and birlik!=0:
    print("Yigirma", end=' ')
if onlik==3 and birlik!=0:
    print("Uttiz", end=' ')

if onlik==1 and birlik==0:
    print("O'nta masala", end=' ')
if onlik==2 and birlik==0:
    print("Yigirmata masala", end=' ')
if onlik==3 and birlik==0:
    print("Uttizta masala", end=' ')
if onlik==4 and birlik==0:
    print("Qirqta masala", end=' ')


if onlik<4:
    if birlik == 1:
        print("bitta masala")
    if birlik == 2:
        print("ikkita masala")
    if birlik == 3:
        print("uchta masala")
    if birlik == 4:
        print("to'rtta masala")
    if birlik == 5:
        print("beshta masala")
    if birlik == 6:
        print("oltita masala")
    if birlik == 7:
        print("yettita masala")
    if birlik == 8:
        print("sakkizta masala")
    if birlik == 9:
        print("to'qqizta masala")
'''
#Case 19
'''y=int(input("y="))
y=y-1983
if y%2==1:
    print('yashil')
if y%2==2:
    print('qizil')
if y%2==3:
    print('sariq')
if y%2==4:
    print('oq')
if y%2==0:
    print('qora')

if y%12==1:
    print('sichqon')
if y%12==2:
    print('sigir')
if y%12==3:
    print('yo\'lbars')
if y%12==4:
    print('quyon')
if y%12==5:
    print('ajdar')
if y%12==6:
    print('ilon')
if y%12==7:
    print('ot')
if y%12==8:
    print('qo\'y')
if y%12==9:
    print('maymun')
if y%12==10:
    print('tovuq')
if y%12==11:
    print('it')
if y%12==0:
    print('to\'ng\'iz')
'''
#Case 20
'''d=int(input("d="))
m=int(input("m="))
if 31>=d>=20 and m==1 or 18>=d>=1 and m==2:
    print("Qovg'a")
if 28>=d>=19 and m==2 or 20>=d>=1 and m==3:
    print("Baliq")
if 31>=d>=21 and m==3 or 19>=d>=1 and m==4:
    print("Qo'y")
if 30>=d>=20 and m==4 or 20>=d>=1 and m==5:
    print("Buzoq")
if 31>=d>=21 and m==5 or 21>=d>=1 and m==6:
    print("Egizaklar")
if 30>=d>=22 and m==6 or 22>=d>=1 and m==7:
    print("Qisqichbaqa")
if 31>=d>=23 and m==7 or 22>=d>=1 and m==8:
    print("Arslon")
if 31>=d>=23 and m==8 or 22>=d>=1 and m==9:
    print("Parizod")
if 30>=d>=23 and m==9 or 22>=d>=1 and m==10:
    print("Tarozi")
if 31>=d>=23 and m==10 or 22>=d>=1 and m==11:
    print("Chayon")
if 30>=d>=23 and m==11 or 21>=d>=1 and m==12:
    print("O'qotar")
if 31>=d>=22 and m==12 or 19>=d>=1 and m==1:
    print("Echki")
    '''
