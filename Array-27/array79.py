from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)
a.reverse()
for i in range(1,n):
	a[i-1]=a[i]
a[n-1]=0
a.reverse()
print(a)