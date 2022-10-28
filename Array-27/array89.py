a=[1,2,3,1,4,5,6,7]
for i in range(1,len(a)):
	if a[i]>a[i-1]:
		b=i
	else:
		break
print(b)
#a.insert(b+1,)
for i in range(1,b+2):
	if a[i]>=a[b+1]>=a[i-1]:
		a.insert(i,a[b+1])
		a.pop(b+2)
		break
print(a)