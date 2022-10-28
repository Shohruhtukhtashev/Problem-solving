from random import randint
n=int(input('n='))
k=int(input('k='))
a=[randint(1,9) for i in range(n)]
print(a)
a.reverse()
for i in range(1,n-1):
	a[n-i]=a[i-1-k]
a.reverse()
for i in range()
print(a)