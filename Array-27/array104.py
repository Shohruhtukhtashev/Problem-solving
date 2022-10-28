from random import randint
n=int(input('n='))
k=int(input('k='))
m=int(input('m='))
a=[randint(1,9) for i in range(n)]
print(a)

'''if 0<=k<n and 1<=m<=10:
	for i in range(m):
		a.insert(k,0)
	print(a)
else:
	print('Bunga amal qiling: 0<=k<n, 1<=m<=10')'''
x=False
y=False
if 0<=k<n:
	x=True
	pass
else:print(f"Bunga e'tibor qiling: 0<=k<n")
if 1<=m<=10:
	y=True
	pass
else:print(f"Bunga e'tibor qiling: 1<=m<=10")
if x and y:
	for i in range(m):
		a.insert(k,0)
	print(a)