from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)

for i in range(n-1):
	for j in range(n-i-1):
		if a[j]>a[j+1]:
			a[j],a[j+1]=a[j+1],a[j]
			#x=a[j]
			#a[j]=a[j+1]
			#a[j+1]=x
print(a)
