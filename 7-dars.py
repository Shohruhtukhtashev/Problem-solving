#1
'''a=int(input('a='))
s=a**(1/4)
print(s)
'''
#2
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a**2==b**2+c**2 or c**2==b**2+a**2 or b**2==a**2+c**2:
	print('True') 
else:
	print('False')
	'''
#3 Kiritilgan uch xonali sonni teskarisini chiqaruvchi dastur.
'''
a=int(input('uch xonali son kiriting: '))
yuz=a//100
on=a%100//10
bir=a%10
print(bir,on,yuz, sep='')
'''
#4 soniyani, necha sekund menut soat kun borligini chiqaruvchi dastur.
'''a=int(input('a='))
kun=a//86400
soat=a%86400//3600
minut=a%86400%3600//60
sekund=a%60
print(f"{kun} kun, {soat} soat, {minut} minut, {sekund} sekund.")
'''
#5 uchta sonning o'rtachasini topuvchi dastur
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
s=(a+b+c)/3
print(f"Kiritilgan sonlarning o'rtachasi {s} ga teng.")
'''
#6 Kiritilgan yilning kabisa yoki kabesa emasligini topuvchi dastur.
'''a=int(input('a='))
kabesa=False
if a%4==0:
	kabesa=True
if a%100==0 and a%400!=0:
	kabesa=False

if kabesa:
	print('kabesa')
else:
	print('kabesa emas')
'''
#7 Kiritilgan ucha sonning nechtasi musbat nechta manfiyligini ko'rsatuvchi dastur.
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a>0 and b>0 and c>0:
	print('hammai musbat')
if a>0 and b>0 and c<0 or a>0 and c>0 and b<0 or b>0 and c>0 and a<0:
	print('2 ta musbat va 1 ta manfiy')
if a>0 and b<0 and c<0 or b>0 and a<0 and c<0 or c>0 and b<0 and a<0:
	print('1 ta musbat va 2 ta manfiy')
if a<0 and b<0 and c<0:
	print('0 ta musbat va 3 ta manfiy')
'''
#8 palidrom son ekanligini topuvchi dastur. 
##Palidrom son deb boshidan ham oxiradan ham o'qiganda bir xil sonlarga aytiladi. M-n: 12121, 45454 va h.k
'''
x=a=int(input('a='))
s=0
while a>0:
	qoldiq=a%10
	s=s*10+qoldiq
	a//=10

if x==s:
	print('Bu son Palidrom son')
else:
	print('Bu son Palidrom son emas')

'''
# Mukammal yoki mukammal emasligini chiqarib beradi. Mukammal son deb o'zidan boshqa bo'uvchilarining yig'indisi o'ziga teng bo'ladigan songa aytiladi.

'''
a=int(input('a='))
i=1; s=0
while i<a:
	if a%i==0:
		s+=i
	i+=1
if s==a:
	print('Mukammal son')
else:
	print("Mukammal son emas")
'''
n=int(input('n='))
i=1
k=0
while i<=n:
	if n%i==0:
		print(i+1)
	i+=1
	
