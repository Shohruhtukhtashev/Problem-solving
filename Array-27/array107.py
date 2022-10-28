from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)
s=0
for i in range(1,n,2):
	s+=a[i]*2
print(s)