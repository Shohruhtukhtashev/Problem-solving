#chala
a=[2,5,7,3,2,9,5]

for i in range(len(a)-1):
	for k in range(i+1,len(a)):
		if a[i]==a[k]:
			a.pop(k)
print(a)