from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)
#a=[2,2,2,3,4,4,4,4,3,3,3]
b=[];c=[]
sana=1
for i in range(len(a)-1):
	if a[i]==a[i+1]:
		sana+=1
	else:
		b.append(sana)
		c.append(a[i])
		sana=1
b.append(sana)
c.append(a[n-1])
print(f"Seriya uzunligi:{b}\nSeriya elenti: {c}")