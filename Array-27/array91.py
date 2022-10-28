from random import randint
n=int(input('n='))
k=int(input('k='))
m=int(input('m='))
a=[randint(1,9) for i in range(n)]
print(a)

x=m+1
for i in a[k:x]:
	a.remove(i)
print(a)