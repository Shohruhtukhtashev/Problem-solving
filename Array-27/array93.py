from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)
b=[]
for i in range(1,len(a),2):
		b.append(a[i])
print(b,'\n','elementlar soni:',len(b))