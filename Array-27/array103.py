from random import randint
n=int(input('n='))
a=[randint(1,9) for i in range(n)]
print(a)

i=a.index(min(a))
a.insert(i,0)
i=a.index(max(a))
a.insert(i+1,0)
print(a)