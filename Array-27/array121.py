'''from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)'''

l=int(input('k='))
a=[2,2,2,3,4,4,4,4,3,3,3]
k=0;sana=0
for i in range(len(a)-1):
	if a[i]!=a[i+1]:
		k=1
		if l==k:
			for i in range(sana):
				a.insert()
			sana=1
		else:
			sana+=1