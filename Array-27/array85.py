from random import randint
n=int(input('n='))
k=int(input('k='))
a=[randint(1,9) for i in range(n)]
print(a)

a.reverse()
#b=a[0]
for i in range(k,n):
	a[i-k]=a[i]
#a[n-1]=b
a.reverse()
print(a)