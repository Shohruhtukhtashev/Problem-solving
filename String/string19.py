a=input("a=")
c=0;k=0
for i in a:
	if i.isdigit():
		c+=1
	elif i=='.':
		k+=1
if c!=0 and k==0:
	print(1)
elif k!=0:
	print(2)
else:
	print(0)