from random import randint
n=int(input('n='))
a=[randint(1,20) for i in range(n)]
x=[randint(1,20) for i in range(1)]
a.sort()
a=x+a
print(a)
#a=[4,2,3,4,5,6,7]
for i in range(1,len(a)):
	if a[0]>=a[i]:
		b=i+1
a.insert(b,a[0])
a.remove(a[0])
print(a)