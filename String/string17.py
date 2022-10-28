a=input("a=")
c=''
for i in a:
	if i.isupper():
		c+=i.lower()
	else:
		c+=i
print(c)