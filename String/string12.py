a=input("a=")
n=int(input("n="))
c=''
for i in a[:len(a)-1]:
	c+=i+'*'*n
c+=a[len(a)-1]
print(c)