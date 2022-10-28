from random import randint
n=int(input('n='))
a=[randint(-10,10) for i in range(n)]
print(a)
b=a.copy()
k=0
for i in range(n):
	if a[i]<0:
		b.insert(k,0)
		k+=2
	else:
		k+=1
print(b)