a = input("Enter text in hex : ")

a = a.split()

for i in range(len(a)):
	a[i] = chr(int(a[i],16))

print("".join(a))