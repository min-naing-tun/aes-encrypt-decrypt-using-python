a = input("Enter text in decimal : ")

a = a.split()

for i in range(len(a)):
	if(i+1==len(a)):
		a[i] = hex(int(a[i],10))[2:].rjust(2, "0")
	else:
		a[i] = hex(int(a[i],10))[2:].rjust(2, "0")+" "	

print("".join(a))