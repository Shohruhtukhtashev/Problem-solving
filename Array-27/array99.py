a=[2,3,6,6,6,6,8,0,1,2,3,3,2,4]
for i in range(len(a)):
	q=a[i]
	if a.count(a[i])>2:
		for k in range(a.count(a[i])):
			a.remove(q)
	if i>=len(a):
		break
print(a,'\nsoni:',len(a))