a=input("a=")
c=''
for i in a:
	if i.isupper() and 65<=ord(i)<=90:
		c+=i.lower()
	else:
		c+=i
print(c)