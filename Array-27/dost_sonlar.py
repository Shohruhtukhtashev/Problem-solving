'''son1=int(input('Son1: '))
son2=int(input('Son2: '))
summa1=0
summa2=0
for i in range(1,son1//2+1):
	if son1%i==0:
		summa1+=i
for i in range(1,son2//2+1):
	if son2%i==0:
		summa2+=i
print(summa1)
print(summa2)
if summa1==son2 and summa2==son1:
	print(f"Kiritilagan {son1} va {son2} 'Do'st sonlar'.")
else:print("'Do'st sonlar' emas")
'''
n=int(input('n='))
summa1=0
summa2=0
son1=0
son=64
for i in range(220,n,2):
	