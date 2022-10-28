#1
'''
n=int(input('n='))
a=[];s=0;c=1
while s<n:
	a.append(c)
	s+=1
	c+=2
print(a)
'''
#2
'''
n=int(input('n='))
s=0
a=[]
while s<n:
	a.append(2**s)
	s+=1
print(a)
'''
'''
import random
n=int(input('n='))
a=[random.randint(1,100) for i in range(n)]
print(a)
a=[i for i in a if i%2==0]
print(a)
'''
#3
'''
a0=int(input('a0='))
d=int(input('d='))
n=int(input('n='))
a=[];s=1
while s<=n:
	a.append(a0+d)
	a0+=d
	s+=1
print(a)
'''
#4
'''
a0=int(input('a='))
d=int(input('d='))
n=int(input('n='))
a=[];s=1
while s<=n:
	a.append(a0*d)
	a0*=d
	s+=1
print(a)
'''
#5
'''
n=int(input('n='))
f=[0,1]
i=2
while i<=n:
	f.append(f[i-1]+f[i-2])
	i+=1
print(f)
'''
#6
#incomplite
'''
n=int(input('(n>2)n='))
a=int(input('a='))
b=int(input('b='))
s=0;m=[]
while s<n:
	m.append(a+b)
	b=a+b
	s+=1
print(m)'''
#7
'''
n=int(input('n='))
x=[]
for i in range(n):
	a=int(input('a='))
	x.append(a)
x.reverse()
print(x)
'''
#8
'''n=int(input('n='))
m=[]
for i in range(n):
	a=int(input('a='))
	if a%2!=0:m.append(a)
m.sort()
print(m)'''
#9
'''n=int(input('n='))
m=[]
for i in range(n):
	a=int(input('a='))
	if a%2==0:m.append(a)
m.sort(reverse=True)
print(m)
'''
#10
'''
n=int(input('n='))
m=[];s=[]
for i in range(n):
	a=int(input('a='))
	if a%2==0:
		m.append(a)
	else:
		s.append(a)
m.sort()
s.sort(reverse=True)
print(*(m+s))
'''
#11
'''import random
print("1<=k<n")
n=int(input('n='))
k=int(input("k="))
a=[random.randint(0,9) for i in range(n)]
print(a)
a=a[::k]
print(a)'''

'''import random
print("1<=k<n")
n=int(input('n='))
k=int(input("k="))
l=int(input('l='))
a=[random.randint(0,9) for i in range(n)]
print(a)
a=[a[i] for i in range(len(a)) if i%k!=0 and i%l!=0]
print(a)'''
#12
'''
n=int(input('(n juft son)n='))
m=[]
for i in range(n):
	a=int(input('a='))
	m.append(a)
print(m[::2])
'''
'''
import random
n=int(input('n='))
a=[random.randint(n) for i in range(n) if i%2==0]
print(a)
'''
#13
'''n=int(input('(n toq son) n='))
m=[]
for i in range(n):
	a=int(input('a='))
	m.append(a)
print(m[])'''
#14
'''
n=int(input('n='))
m=[]
for i in range(n):
	a=int(input('a='))
	m.append(a)
print(*m[::2],*m[1::2])
'''
#15
'''
n=int(input('(n juft son)n='))
m=[]
for i in range(n):
	a=int(input('a='))
	m.append(a)
print(*m[1::2],*m[(n-2)::-2])
'''
#16
'''
n=int(input('n='))
m=[]
for i in range(n):
	a=int(input('a='))
	m.append(a)
print(*m[::]+m[n-1::-1])
'''
#17

#18
'''from random import randint
n=int(input('n='))
a=[randint(0,9) for i in range(n)]
print(a)
x=a[n-1]
for i in a:
	if i<x:
		print(i)
		break
if i>=x:
	print(0)'''
#20
'''n=int(input('n='))
k=int(input('k='))
l=int(input('l='))
m=[]
for i in range(n):
	a=int(input('a='))
	m.append(a)
x=m[k:l+1]
s=0
while k<l:
	k=k
print(x)'''


'''m=[2,3,5,7]
m.pop(3)
print(m)'''


'''import random
a=[random.randint(1,30) for i in range(30)]
b=random.randint(1,30)
print(a,b)'''
#25 discussion
'''n=int(input('n='))
b=[]
for  i in range(n):
	a=int(input('a='))
	b.append(a)
d=b[1]/b[0]
for i in range(2,n-1):
	if b[i+1]/d==b[i]:
		x=True
	else:
		x=False
if x:
	print(d)
else:
	print(0)
'''
#25
# Saidislomga rahmat!
'''a=[2,4,8,16,32]
print(a)
for i in range(len(a)-2):
	if a[i+1]/a[i]==a[i+2]/a[i+1]:
		d=a[i+1]/a[i]
	else:
		d=0
		break
print(d)'''

#26 discussion
'''a=[2,3,3,7,8]
print(a)
for i in range(len(a)):
	if i%2==0 and a[i]%2==0:
		x=0
		continue
	if i%2==0 and a[i]%2!=2:
		x=i+1
		break
	if i%2==1 and a[i]%2==0:
		x=i+1
		break
print(x)'''
#27
'''
a=[1,-5,6,-4,-8]
print(a)
for i in range(len(a)):
	if i%2==0 and a[i]>=0:
		x=0
		continue
	if i%2==0 and a[i]<0:
		x=i+1
		break
	if i%2!=0 and a[i]>0:
		x=i+1
		break
print(x)

a=[1,-5,6,-4,-8]
print(a)
for i in range(len(a)):
	if a[i]*a[i+1]=>0:
		print(i+1)
		break
else:
	print(0)
'''
#28
'''a=[1,2,3,4,5,6,3,4]
b=[]
print(a)
for i in range(len(a)):
	if i%2==0:
		b.append(a[i])
print(b)
print(min(b))'''
#29
'''a=[1,2,3,4,5,6,3,4]
b=[]
print(a)
for i in range(len(a)):
	if i%2!=0:
		b.append(a[i])
print(b)
print(max(b))
'''
#30
'''a=[1,23,4,1]
print(a)
sana=0
for i in range(len(a)-1):
	if a[i]>a[i+1]:
		print(i,end=' ')
		sana+=1
print('soni:',sana)
'''
#31
'''a=[6,3,4,5]
print(a)
sana=0
for i in range(len(a)-1,0,-1):
	if a[i]>a[i-1]:
		print(i,end=' ')
		sana+=1
print('soni:',sana)'''
#32
'''a=[10,11,11,6,7]
print(a)
for i in range(1,len(a)-1):
	if a[i-1]>a[i]<a[i+1]:
		print(i)
		break'''
#33
'''a=[10,11,1,6,5]
print(a)
x='bunday son yuq'
for i in range(1,len(a)-1):
	if a[i-1]<a[i]>a[i+1]:
		x=i
print(x)'''
#34
'''a=[5,2,3,2,6,5,7,3,4]
b=[]
print(a)
for i in range(1,len(a)-1):
	if a[i-1]>a[i]<a[i+1]:
		b.append(a[i])
print(b)
print(max(b))'''
#35
'''a=[10,11,1,6,7]
b=[]
print(a)
for i in range(1,len(a)-1):
	if a[i-1]<a[i]>a[i+1]:
		b.append(a[i])
print(b)
if b!=[]:
	print(max(b))
'''
#36
'''a=[5,2,3,2,6,5,7,3,4]
print(a)
for i in range(1,len(a)-1):
	if a[i-1]<a[i]>a[i+1] or a[i-1]>a[i]<a[i+1]:
		a.pop(i)
print(a)
if a!=[]:
	print(max(a))
'''
#37
'''import random
a=[random.randint(0,9) for i in range(int(input("N=")))]
print(a)
b=a[0]
s=c=0
for i in a:
	if b<i:
		b=i
		s+=1
	else:
		b=i
		s=0
	if s==1:
		c+=1
print(c)'''

#38
#import random
#a=[random.randint(0,9) for i in range(int(input('N=')))]
'''a=[9,3,9,4,4,7,7,0,6,7]
print(a)
b=a[0]
c=s=0
for i in a:
	if i<b:
		b=i
		s+=1
	else:
		b=i
		s=0
	if s==1:
		c+=1
print(c)'''

#39
'''import random
a=[random.randint(0,9) for i in range(int(input("N=")))]
print(a)
b=a[0]
s=c=0
for i in a:
	if b<i:
		b=i
		s+=1
	else:
		b=i
		s=0
	if s==1:
		c+=1
print(c)
b=a[0]
s=0
for i in a:
	if i<b:
		b=i
		s+=1
	else:
		b=i
		s=0
	if s==1:
		c+=1
print(c)'''
#40
'''a=[5,2,7,2,6,5,7,8,4]
r=3
b=[]
print(a)
for i in range(len(a)):
	b.append(a[i]-r)
print(min(b)+r)'''
#41
'''a=[5,2,3,2,6,5,7,3,4]
print(a)
x=True
for i in range(len(a)-1):
	if x:
		maxi=a[i]+a[i+1]
		one=a[i]
		two=a[i+1]
		x=False
	elif maxi<a[i]+a[i+1]:
		maxi=a[i]+a[i+1]
		one=a[i]
		two=a[i+1]
print(f"Yig'indisi:{maxi}")
print(one,two)'''
#42 discussion
'''a=[5,4,15,5,6,9,7,8,4]
r=10
print(a)
x=True
for i in range(len(a)-1):
	if x:
		maxi=abs(a[i]+a[i+1])-r
		one=a[i]
		two=a[i+1]
		x=False
	elif maxi>abs(a[i]+a[i+1])-r:
		maxi=a[i]+a[i+1]-r
		one=a[i]
		two=a[i+1]
print(f"Yig'indisi:{maxi+r}")
print(one,two)'''
#43 descussion
'''a=[10,9,8,9,5,3]
print(a)
s=0
if a[0]<a[0+1]:
	for i in range(1,len(a)-1):
		if a[i]<a[i+1]:
			pass
		else:
			s+=1
	
if a[0]>a[0+1]:
	for i in range(1,len(a)-1):
		if a[i]>a[i+1]:
			pass
		else:
			s+=1
print(s)
'''
#44
'''import random
a=[random.randint(0,9) for i in range(int(input("n=")))]
print(a)
x=0;s=0
while x<len(a)-2:
	for i in a[x+1:]:
		s+=1
		if a[x]==i:
			break
		else:
			continue
	if a[x]==i:
		break
	x+=1
	s=0
print(x,s+x)'''
'''
a=[2,3,4,5,6]			
for i in a[2:]:
	print(i)'''
#45
'''a=[1,15,4,2,7,8,5]
print(a)
x=True
for i in range(len(a)-1):
	if x:
		minm=abs(a[i]-a[i+1])
		one=a[i]
		two=a[i+1]
		x=False
	if minm>abs(a[i]-a[i+1]):
		minm=abs(a[i]-a[i+1])
		one=a[i]
		two=a[i+1]
print(minm)
print(one,two)'''
#46
'''a=[1,15,4,2,7,8,5]
r=10
x=True
print(a)
for i in range(-len(a),len(a)):
	if i<0:
		if x:
			mi=(a[i]-r)
			x=False
		if mi>(a[i]-r):
			mi=(a[i]-r)
	else:
		if i==0:
			m=mi+a[i]-r
			two=a[i]
		elif m>mi+a[i]-r:
			m=mi+a[i]-r
			two=a[i]
print(mi+r,two)
'''
#47
'''from random import randint
n=int(input('n='))
a=[randint(0,9) for i in range(n)]
print(a)

for i in range(len(a)):
	x=1
	for k in range(i):
		if a[k]==a[i]:
			x=0
			break
	if x==1:
		print(a[i],end=' ')'''
#48
'''a=[7,7,7,4,1,4,1,2,1,7]
print(a)
x=True
for i in range(len(a)):
	if x:
		sm=a.count(a[i])
		q=a[i]
		x=False
	if sm<a.count(a[i]):
		sm=a.count(a[i])
		q=a[i]
print(f"Element:{q}")
print(f"{sm} marta takrorlangan")'''
#49
'''n=6
a=[1,2,3,8,4,6]
x=False
for i in range(len(a)):
	if n<a[i]:
		print(f"Qiymati:{a[i]}\nIndeksi:{i}")
		break
		x=True
if x:
	pass
else:
	print(0)
'''
#50
'''a=[7,8,9,4,1,4,1,2,1,7]
print(a)
s=0
for i in range(len(a)-1):
	if a[i]<a[i+1]:
		s+=1
print(s)
'''
#51
'''a=[7,7,7,4,1,4,1,2,1,7]
b=[1,4,8,9]
print(b)
b=a
print(b)'''

'''   Takrorlash        '''
#25
'''a=[2,4,8,16,32]
print(a)
for i in range(len(a)-2):
	if a[i+1]/a[i]==a[i+2]/a[i+1]:
		d=a[i+1]/a[i]
	else:
		d=0
		break
print(d)'''
#26
'''a=[2,3,4,6]
print(a)
for i in range(len(a)):
	if i%2==0 and a[i]%2==0:
		ans=0
	elif i%2!=0 and a[i]%2!=0:
		ans=0
	if i%2==0 and a[i]%2!=0:
		ans=i
		break
	elif i%2!=0 and a[i]%2==0:
		ans=i
		break
print(ans)'''
#27
'''a=[2,-3,-1,-5,6]
print(a)
for i in range(len(a)):
	if i%2==0 and a[i]>0:
		d=0
	elif i%2!=0 and a[i]<0:
		d=0
	if i%2==0 and a[i]<0:
		d=i
		break
	elif i%2!=0 and a[i]>0:
		d=i
		break
print(d)
'''
#28
'''a=[2,3,5,6,9,12]
print(a)
b=[]
for i in range(0,len(a),2):
	b.append(a[i])
print(b)
print(min(b))'''
#qoshimcha listsiz
'''a=[2,3,1,6,9,12]
print(a)
x=True
for i in range(0,len(a),2):
	if x:
		mn=a[i]
		x=False
	if mn>a[i]:
		mn=a[i]
print(mn)'''

#29
'''a=[2,3,1,6,9,12]
print(a)
x=True
for i in range(1,len(a),2):
	if x:
		mx=a[i]
		x=False
	if mx<a[i]:
		mx=a[i]
print(mx)'''

#30
'''a=[4,3,2,1,9,12]
print(a)
sana=0
for i in range(len(a)-1):
	if a[i]>a[i+1]:
		print(i)
		sana+=1
print('son:',sana)'''

#31
'''a=[1,2,3,4,5,3]
print(a)
sana=0
for i in range(len(a)-1):
	if a[-i-1]<a[-i]:
		print(len(a)-i)
		sana+=1
print('soni:',sana)'''

#32
'''a=[2,3,3,6,9,12,12,12]
print(a.index(12)+1)
print(a.count(3))
a.remove(12)
print(a)'''
'''import random
a = [3,-3,6,-9,13,-15,18]'''
#print(a)
#x=1
#for i in a[x:6:2]:print(i)
#b=[random.randint(1,10) for i in range(3)]
#print(b)
'''a=[i for i in a if i%2==1]
for i in a:
	if i%2==1:
		a.append(i)
print(a)'''
'''
x = 1 if a[0]>0 else 0

d = k = 0
for i in a[x:]:
    if k%2==0:
        i *= -1
    if i<0:
        d = a.index(i)
        break
    k += 1
print(d)'''
'''a = [1,2,3,4,5,9,8,7,6,5,11,12]
print(a)

b = c = 0
for i in range(len(a)):
    for k in range(i+1,len(a)):
        if a[i]==a[k]:
            b,c = i,k
            break
print(b,c)'''
#47
'''import random
a=[4, 2, 2, 4, 6, 5, 2, 8, 8, 2]#[random.randint(0,9) for i in range(int(input("n=")))]
print(a)
a.reverse()
print(a)
x=0
while x<len(a):
	for i in a[x+1:]:
		if a[x]==i:
			a.remove(i)
	x+=1
a.reverse()
print(a)'''

#52
'''
from random import randint
n=int(input('n='))
a=[randint(1,10) for i in range(n)]
print(a)
#b=[i for i in a 2*i if i<5 else i/2]
b=[]
for i in a:
	if i<5:
		b.append(2*i)
	else:
		b.append(i/2)
print(b)'''

#53
'''from random import randint
n=int(input('n='))
a=[randint(1,10) for i in range(n)]
b=[randint(1,10) for i in range(n)]
print('a=',a)
print('b=',b)
#c=[]
#for i in range(n) :
#	m=max(a[i],b[i])
#	c.append(m)
c=[max(a[i],b[i]) for i in range(n)]
print('c=',c)'''
'''from random import randint
n=int(input('n='))
a=[randint(1,10) for i in range(n)]
print(a)
b=a[1::2]+a[0::2]
print(b)
'''
#54
'''from random import randint
n=int(input('n='))
a=[randint(1,10) for i in range(n)]
print(a)
b=[i for i in a if i%2==0]
print(f"Elementlari soni: {len(b)}\nElementlari: {b}")'''

#55
'''from random import randint
print('n<=15')
n=int(input('n='))
a=[randint(1,10) for i in range(n)]
print(a)
b=[]
t=a[1::2]
b.append(t)
print(b)'''

#56
'''from random import randint
print('n<=15')
n=int(input('n='))
a=[randint(1,10) for i in range(n)]
print(a)
b=[]
b.append(a[3::3])
print(f"Elementlari soni: {len(b)}\nElementlar: {b}")'''

#57
'''from random import randint
n=int(input('n='))
a=[randint(1,10) for i in range(n)]
print(a)
b=[]
b.extend(a[::2])
b.extend(a[1::2])
print(b)'''

#58
'''from random import randint
n=int(input('n='))
a=[randint(1,10) for i in range(n)]
print(a)
b=[]
b=sum(a)
print(b)'''

#59
'''from random import randint
n=int(input('n='))
a=[randint(1,10) for i in range(n)]
print(a)
b=[]
b=sum(a)
print(b/n)'''

#60
'''from random import randint
n=int(input('n='))
a=[randint(1,10) for i in range(n)]
print(a)
b=[]
b=[sum(a[i:]) for i in range(n)]
print(b)
'''
'''from random import randint
n=int(input('n='))
a=[randint(1,10) for i in range(n)]
print(a)
b=[]
b=[sum(a[n-i-1:]) for i in range(n)]
print(b)'''
#61
'''from random import randint
n=int(input('n='))
k=int(input('k='))
a=[randint(1,10) for i in range(n)]
print(a)
b=[]
b=sum(a[k::])
l=len(a[k::])
print(b/l)'''

#62
'''from random import randint
n=int(input('n='))
a=[randint(-10,10) for i in range(n)]
print(a)
b=[i for i in a if i>0]
c=[i for i in a if i<0]
print(f"Elementlari soni: {len(b)}\nElementlari: {b}")
print(f"Elementlari soni: {len(c)}\nElementlari: {c}")'''

#63
'''a=[6,7,8,9,10]
b=[1,2,3,4,5]
if max(a)<max(b):
	print(a+b)
else:
	print(b+a)'''

#64
'''from random import randint
n=int(input('n='))
a=[1,2,3,4,5]
b=[12,13,14,15,16]
c=[6,7,8,9,10]
print(f"{a}\n{b}\n{c}\n")
d=a+b+c
d.sort()
print(d)'''

#65
'''from random import randint
n=int(input('n='))
k=int(input('k='))
a=[randint(1,10) for i in range(n)]
print(a)
a=[a[i]+a[k] for i in range(n)]
print(a)
'''
#66
'''from random import randint
n=int(input('n='))
a=[randint(1,10) for i in range(n)]
print(a)
b=[]
x=True
for i in a:
	if i%2==0 and x:
		k=i
		b.append(i+k)
		x=False
	elif i%2==0:
		b.append(i+k)
	else:
		b.append(i)
print(b)'''


#67
'''from random import randint
n=int(input('n='))
a=[randint(1,10) for i in range(n)]
print(a)
b=[]
x=True
a.reverse()
for i in a:
	if i%2!=0 and x:
		k=i
		b.append(i+k)
		x=False
	elif i%2!=0:
		b.append(i+k)
	else:
		b.append(i)
b.reverse()
print(b)
'''
#68
'''from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)
maxi=max(a)
mini=min(a)
for i in range(n):
	if mini==a[i]:
		a[i]=maxi
	if a[i]==maxi:
		a[i]=mini
print(a)'''
#69
'''from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)
for i in range(0,n-1,2):
	#s=a[i]+a[i+1]
	#print(s)
	#a[i]=s-a[i]
	#a[i+1]=s-a[i]
	a[i],a[i+1]=a[i+1],a[i]
print(a)'''

#70
'''from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)
b=a[int(n/2):]
c=a[:int(n/2)]
b.extend(c)
print(b)'''

#71
'''from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)
for i in range(n):
	b=a[n-1-i]
print(b)'''

#72
'''from random import randint
n=int(input('n='))
k=int(input('k='))
h=int(input('h='))
a=[randint(1,9) for i in range(n)]
print(a)
for i in range(0,h-k+1,2):
	s=a[k+i]+a[k+i+1]
	a[k+i]=s-a[k+i]
	a[k+i+1]=s-a[k+i]
print(a)'''

#73
'''from random import randint
n=int(input('n='))
k=int(input('k='))
h=int(input('h='))
a=[randint(1,9) for i in range(n)]
print(a)
for i in range(1,h-k,2):
	s=a[k+i]+a[k+i+1]
	a[k+i]=s-a[k+i]
	a[k+i+1]=s-a[k+i]
print(a)'''

#74
'''from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)
mx=max(a)
mn=min(a)
for i in range(1,(a.index(mx)-a.index(mn))):
	a[a.index(mn)'+1]=0
print(a')'''

#75
'''from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)
mx=max(a)
mn=min(a)
for i in a:
    if a[a.index(mx)]>a[a.index(mn)] or a[a.index(mx)]<a[a.index(mn)]:
        x=a[a.index(mx)]
        a[a.index(mx)]=a[a.index(mn)]
        a[a.index(mn)]=x
print(a)'''

# from random import randint
# n=int(input('n='))
# a=[randint(1,9) for i in range(n)]
# print(a)
# k=14
# y=True


# for i in range(len(a)-1):
#     if y:
#         x=a[i]+a[i+1]-k
#         m,n=a[i],a[i+1]
#         y=False
#     if abs(x)>abs(a[i]+a[i+1]-k):
#         x=a[i]+a[i+1]-k
#         m,n=a[i],a[i+1]
# print(m,n)

'''n=int(input('n='))
x=True
for i in range(n):
    a=int(input('a='))
    if x:
        maxi=a
        mk=maxi-a
        x=False
    if maxi<a:
        maxi=a
    if mk>maxi-a:
        mk=maxi-a
print(maxi)
print(mk)
    '''