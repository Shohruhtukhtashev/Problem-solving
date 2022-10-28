a=input("a=")
c=0
for i in a:
	if 97<=ord(i)<=122 or 1074<=ord(i)<=1103:
		c+=1
print(c)