text = input("Enter text with 16 char (a a a a --- ) : ").split()

for i in range(len(text)):
	text[i] = hex(ord(text[i]))[2:]

print(text)
