'''from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)'''
k=0
a=[2,2,2,3,4,4,4,4,3,3,3]
for i in range(len(a)-1):
	if a[k]!=a[k+1]:
		a.pop(k)
		k+=0
	else:
		k+=1
a.pop(-1)
print(a)
	