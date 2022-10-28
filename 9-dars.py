#1
'''
a=int(input('a='))
b=int(input('b='))
if a>=b:
	print(a%b)
'''
#2
'''
a=int(input('a='))
b=int(input('b='))
x=a
s=0
while a>=b:
	s+=1
	a-=b
print(f"{x} uzunlikdagi kesmada {b} kesmadan {s} marta joylashadi.")
'''
#3
'''
n=int(input('N='))
k=int(input('K='))
sana=0
while n>=k:
	sana+=1
	n-=k
print(f"{n} ni {k}ga bo'lganda.\n Butun qismi:{sana}\nQoldig'i:{n}")
'''
#4
'''
n=int(input('n='))
while n>=9:
	n-=9
if n==0:
	print(f"3-ning darsjasi")
else:
	print('3-ning darsjasi emas')
'''
#5
'''
n=int(input('n='))
k=1
while 2**k!=n:
	k+=1
print(k)
'''
#6
'''
n=int(input('n='))
i=0
p=1
x=n
while x>2:
	p*=(n-i)
	x=n-i
	i+=2
print(p)
''' 
#7
'''
n=int(input('n='))
k=1
while k*k<=n:
	k+=1
print(k)
'''
#8
'''
n=int(input('n='))
k=1
while k*k<=n:
	k+=1
print(k-1)
'''
'''
n=int(input('n='))
k=1
if n>0:
	while k*k<=n:
		k+=1
print(k-1)
'''
#9
'''
n=int(input('n='))
k=1
if n>1:
	while 3**k<=n:
		k+=1
print(k)
'''
#10
'''
n=int(input('n='))
k=1
if n>1:
	while 3**k<=n:
		k+=1
print(k-1)
'''
#11
'''
n=int(input('n='))
k=0
s=0
if n>1:
	while s<=n:
		k+=1
		s+=k
print(s)
print(k)
'''
#12
'''
n=int(input('n='))
k=0
s=0
if n>1:
	while s<=n:
		k+=1
		s+=k
print(s-k)
print(k-1)
'''
#13
'''
a=int(input('a='))
if a>1:
	s=0
	i=0
	while s<=a:
		i+=1
		s+=1/i
print(i)
'''
#14
'''
a=int(input('a='))
if a>1:
	s=0
	i=0
	while s<=a:
		i+=1
		s+=1/i
print(i-1)
print(s-1/i)
'''
#15
'''
a=s=int(input('s='))
p=int(input('p='))
if 0<p<25:
	while s<=a*2:
		s+=p*0.01
		p*=2
print
'''
#16
'''
p=int(input('p='))
if 0<p<50:
	s=0
	sana=0
	while s<=200:
		p*=0.1
		s+=p
		sana+=1
print(sana)
print(s)
'''
#17
'''
n=int(input('n='))
m=int(input('m='))
if n>m:
	sana=0
	while n>=m:
		n-=m
		sana+=1
print(f"Butun qismi: {sana}")
print(f"Qoldiq qismi: {n}")


# N gacha bo'lgan mukammal sonlarni chiqaruvchi dastur.
'''
#18 Kiritilgan raqamni teskari qilib chiqaradigan dastur (faqat ikki xonali sonlar uchun)
'''
n=int(input('n='))
if n>0:
	sana=0
	while n>=10:
		n-=10
		sana+=1
print(n,sana, sep='')
'''
# N gacha kiritilgan sonni teskari chiqaradi.
'''
n=int(input('n='))
a=1
b=n
i=1
while b>0:
	a=b%10
	print(a,end='',sep='')
	b=n//(10*i)
	i*=10
'''
#19
'''
n=int(input('n='))
i=1
s=0
sana=0
while n>0:
	a=n%10
	sana+=1
	n//=10
	s+=a
print(s,sana)
'''
#20
'''
n=int(input('n='))
k=False
while n>0:
	q=n%10
	if q==2:
		k=True
	n//=10
if k:
	print("bor")
else:
	print("yo'q")
'''
#21
'''
n=int(input('n='))
x=False
while n>0:
	a=n%10
	if a%2!=0 and a!=1:
		x=True
	n//=10
if x:
	print("Bor")
else:
	print("Yo'q")
'''
#22
'''
n=int(input('n='))
j=1
sana=0
while j<=n:
	if n%j==0:
		sana+=1
	j+=1
print(sana)
if sana==2:
	print("tub")
else:
	print("tub emas")
'''
#23
'''
a=int(input('a='))
b=int(input('b='))
'''
#22
'''
n=int(input('n='))
i=2;u=True
while i<n:
	if n%i==0:
		u=False
	i+=1
if u:
	print('tub')
else: print('tub emas')
'''
# febonachi sonlari
'''
n=int(input('n='))
i,k=0,1;s=0; rost=False
if n<=0:
	print("Manfiy son kiritdingiz!")
if n==1:
	print("Kattaroq son kiritding!")
else:
	while s-1<=n:
		s=i+k
		i=k
		k=s
		if i==n or k==n:
			rost=True
		s+=1
if rost:
	print("Bor")
else:
	print("yo'q")
'''
# Febonachi sonlarini topuvchi dastur
'''
n=int(input('n='))
i,k=0,1;s=0
if n<=0:
	print("Manfiy son kiritdingiz!")
if n==1:
	print("Kattaroq son kiritding!")
else:
	print(i)
	while s-1<=n:
		print(k)
		s=i+k
		i=k
		k=s
		s+=1
'''
#25
'''
n=int(input('n='))
i,k=0,1;s=0
if n<=0:
	print("Manfiy son kiritdingiz!")
if n==1:
	print("Kattaroq son kiritding!")
else:
	while s<=n:
		s=i+k
		i=k
		k=s
print(k)
'''
#26
'''
n=int(input('n='))
i,k=0,1;s=0
if n<=0:
	print("Manfiy son kiritdingiz!")
if n==1:
	print("Kattaroq son kiritding!")
else:
	while k<=n:
		x=k
		sum=i+k
		i=k
		k=sum
		
print(x)
print(k)
'''
#27
'''
n=int(input('n='))
i,k=0,1;s=0
if n<=0:
	print("Manfiy son kiritdingiz!")
if n==1:
	print("Kattaroq son kiritding!")
else:
	while k<=n:
		sum=i+k
		i=k
		k=sum
		s+=1
print(s+1)
e=float(input('e='))
a1=2
k=2
k-1=1
while
'''
# fibonachi sonlari
n=int(input('n='))  
i=2;f0=0;f1=1
while i<=n:
	fi=f0+f1
	f0=f1
	f1=fi
	i+=1
	print(fi,end=' ')
'''
n=int(input('n='))
j=1
while j<=n:
	i=1; s=0
	while i<j:
		if j%i==0:
			s+=i
		i+=1
	if s==j:
		print(j)
	j+=1
'''
