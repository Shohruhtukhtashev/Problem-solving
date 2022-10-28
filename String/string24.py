a=input('a=')
c=0;s=0
for i in a[::-1]:
   c+=int(i)*2**s
   s+=1
print(c)