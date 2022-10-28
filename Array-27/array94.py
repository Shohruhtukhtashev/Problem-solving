from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)
b=[]
for i in range(0,len(a),2):
	b.append(a[i])
print(b,'\nElemantla soni:',len(b))