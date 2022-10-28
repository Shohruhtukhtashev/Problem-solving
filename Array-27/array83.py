from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)

a.reverse()
b=a[0]
for i in range(n-1):
	a[i]=a[i+1]
a[n-1]=b
a.reverse()
print(a)