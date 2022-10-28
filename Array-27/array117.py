'''from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)'''
a=[2,2,2,3,4,4,4,4,3,3,3]
b=0
for i in range(len(a)-1):
	if a[b]!=a[b+1]:
		a.insert(b+1,0)
		b+=2
	else:
		b+=1
a.insert(0,0)
print(a)