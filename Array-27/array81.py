from random import randint
n=int(input('n='))
k=int(input('k='))
a=[randint(1,9) for i in range(n)]
print(a)

a.reverse()
for i in range(k,n):
	a[i-k]=a[i]
for i in range(n-k,n):
	a[i]=0
a.reverse()
print(a)