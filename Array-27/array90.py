from random import randint
n=int(input('n='))
k=int(input('k='))
a=[randint(1,100) for i in range(n)]
print(a)

a.pop(k)
print(a)