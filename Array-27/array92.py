from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)
b=[]
for i in range(n):
	x=a[i]
	if x%2==0:
		b.append(x)
print(b,'\n','elementlar soni:',len(b))