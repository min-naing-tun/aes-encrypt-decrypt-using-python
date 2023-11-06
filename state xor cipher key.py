l1 = []
l2 = []
result = ""


for i in range(4):
	l1.append(input("Enter "+str(i+1)+" ROW from state or mix_column (0 0 0 0) : ").split())

print("-----")

for i in range(4):
	l2.append(input("Enter "+str(i+1)+" ROW from key (0 0 0 0) : ").split())

print("-----")


for i in range(4):
	for j in range(4):
		result += hex(int(l1[i][j], 16)^int(l2[i][j], 16))[2:].rjust(2,"0")+" "
	result = result.strip()
	result += "\n"

print("state of round")
print(result)

