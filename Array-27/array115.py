from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)
b=[]
for i in range(n-1):
	for j in range(n-i-1):
		if a[j]>a[j+1]:
			x=a[j]
			a[j]=a[j+1]
			a[j+1]=x
	b.append(a[i])
print(a)
print(b)
