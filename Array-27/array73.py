from random import randint
n=int(input('n='))
k=int(input('k='))
h=int(input('h='))
a=[randint(1,10) for i in range(n)]
print(a)
a=a[:k]+a[h-1:k:-1]+a[h:]
print(a)