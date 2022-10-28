from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)

for i in range(1,n-1):
	if a[i-1]>a[i]<a[i+1]:
		a[i]=a[i]**2
print(a)