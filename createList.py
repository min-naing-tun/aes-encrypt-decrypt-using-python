userInput = []


for i in range(4):
	userInput.append(input("Enter List (0 0 0 0) : ").split())

result = ""

for i in range(4):
	result += "["
	for s in range(4):
		if(s==3):
			result += "\""+userInput[s][i]+"\"]\n"
		else:
			result += "\""+userInput[s][i]+"\", "

print("\nCopy this")
print(result)