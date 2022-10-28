from random import randint
n=int(input('n='))
k=int(input('k='))
a=[randint(1,9) for i in range(n)]
print(a)

b=[]
b=a[:k]
for i in range(k,n+2):
	if i<n:
		a[i-k]=a[i]
	else:
		a[i-k]=b[i-n]
print(a)