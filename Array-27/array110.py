from random import randint
n=int(input('n='))
a=[randint(-10,10) for i in range(n)]
print(a)

for i in range(n):
	if a[i]%2==0 and a[i]>0:
		a.append(a[i])
print(a)