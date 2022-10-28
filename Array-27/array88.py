from random import randint
n=int(input('n='))
a=[randint(1,20) for i in range(n)]
x=[randint(1,20) for i in range(1)]
a.sort()
a=a+x
print(a)
#a=[4,2,3,4,5,6,7]
for i in range(len(a)-1):
	if a[n]>=a[i]:
		b=i+1
print(b)
a.insert(b,a[n])
a.pop(n+1)
print(a)