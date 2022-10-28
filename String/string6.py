a=input("a=")
if a.isdigit():
	print("digit")
elif 97<=ord(a)<=122 or 65<=ord(a)<=90:
	print("lotin")
else:print(0)