a=input('a=')
for i in range(127):
	if a.startswith(chr(i)):
		print(chr(i),i)
		break
for i in range(127):
	if a.endswith(chr(i)):
		print(chr(i),i)
		break
