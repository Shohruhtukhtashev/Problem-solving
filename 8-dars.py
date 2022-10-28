#1
'''
n=int(input('n='))
i=1
while i<=n:
	if n%i==0:
		print(i)
	i+=1
'''
#2
'''
n=int(input('n='))
i=1
s=0
while i<=n:
	if n%i==0:
		s=s+i
	i+=1
print(s)
'''
#3
'''
n=int(input('n='))
i=1
s=0
while i<n:
	if n%i==0:
		s+=i
	i+=1
if s==n:
	print('Mukammal son')
else:
	print('Mukammal son emas')
'''
#4 
'''
n=int(input('n='))
i=1
while i<=n:
	if i%3==0 and i%5!=0:
		print(i)
	i+=1
'''
#5 N gacha bo'lgan sonlarda 3 ga bo'linadigan va 5 ga bo'linmaydiganlarini topuvchi dastur.
'''
n=int(input('n='))
i=1
while i<=n:
	if i%3==0 and i%5!=0:
		print(i)
	i+=1
'''
#8
#chala
'''
n=int(input('n='))
a=3
b=4
c=5
while c<=n:
	if c*c==b*b+a*a:
		print(c,a,b, end=' ')
	a*=3
	b*=4
	c*=5
'''
#11
'''
n=int(input('n='))
i=1
s=0
while i<=n:
	s=s+1/i**2
	i+=1
print(s)
'''
'''
n=int(input('n='))
i=1
s=0
while i<=n:
	s=s+1/i**3
	i+=1
print(s)
'''
'''
n=int(input('n='))
i=1
i1=1
s=0
while i<=n:
	i1=i1*i
	s=s+1/i1
	i+=1
print(s)
'''
'''
n=int(input('n='))
i=1
s=0
while i<=n:
	s+=1/(2*i)**2
	i+=1
print(s)
'''
'''
n=int(input('n='))
i=2
s=1
while i<=n:
	s*=(i+1)/(i+2)
	i+=2
print(s)
'''
'''
n=int(input('n='))
i=2
s=1
i1=1
while i<=n:
	i1*=i
	s*=(1+1/i1)**2
	i+=1
print(s)
'''
# f
import math
'''
n=int(input('n='))
i=1
a=0
s=0
while i<=n:
	a+=math.sin(i)
	s+=1/a
	i+=1
print(s)
'''
# g
'''
n=int(input('n='))
i=1
cs=0
sn=0
s=0
while i<=n:
	cs+=math.cos(i)
	sn+=math.sin(i)
	s+=cs/sn
	i+=1
print(s)
'''
'''
o='salom'
b=o[1:3]
a=o[2:]
print(b)
print(a)
'''

## 
'''
n=float(input('n='))
k=1
i=1
s=0
while s<=n:
	s+=1/i
	i+=1
print(i-1)
'''
## a sonini b ga (*) amalisiz kupaytirish.
'''
a=float(input('a='))
c=float(input('c='))
sana=1
s=0
while sana<=c:
	s+=a
	sana+=1
print(s)
'''
##
a=float(input('a='))
c=float(input('c='))
sana=0
while a>=c:
	sana+=1
	a-=c
print(sana)