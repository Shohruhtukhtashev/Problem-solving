a=[2,2,3,5,2,7,9,2]

for i in range(len(a)):
	x=a.count(a[i])
	print(x)
	if x<3:
		a.remove(a[i])

print(a