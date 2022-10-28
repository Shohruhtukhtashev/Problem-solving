a=[2,6,8,0,1,3,3,2,4]
for i in range(len(a)):
	if i>=len(a):
		break
	q=a[i]
	if a.count(a[i])==2:
		for k in range(a.count(a[i])):
			a.remove(q)
print(a,'\nsoni:',len(a))