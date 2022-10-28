from random import randint
n=int(input('n='))
k=int(input('k='))
a=[randint(0,9) for i in range(n)]
print(a)
for i in range(n):
	if a[i]==0:
		a.insert(k,0)
		break
print(a)