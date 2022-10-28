from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)

for i in range(len(a)-1):
	#print('i=',i)
	mini=i
	for j in range(i+1,len(a)):
		if a[mini]>a[j]:
			mini=j
	a[i],a[mini]=a[mini],a[i]
print('saralangan array')
for i in range(len(a)):
	print(a[i],end=" ")

