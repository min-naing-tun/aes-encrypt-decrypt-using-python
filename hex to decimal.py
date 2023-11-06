a = input("Enter text in hex : ")

a = a.split()

for i in range(len(a)):
	if(i+1==len(a)):
		a[i] = str(int(a[i],16)).rjust(2,"0")
	else:
		a[i] = str(int(a[i],16)).rjust(2,"0")+" "	

print("".join(a))