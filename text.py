a = input("Enter text (16 char) : ")

temp1 = " "
temp2 = " "

keyState1 = ['00 01 02 03',
			 '10 11 12 13',
			 '20 21 22 23',
			 '30 31 32 33']


a = 0
b = 0
for i in a:
	temp1 += str(hex(ord(i)))[2:]+" "
temp1 = temp1.strip()

for i in a:
	temp2 += str(bin(ord(i))).replace("0b", "0")+" "
temp2 = temp2.strip()

print("hex : "+temp1) 
print("bin : "+temp2) 


# h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# for i in range(len(h)):
# 	# print(str(str(bin(h[i]))[2:]).rjust("0"))
# 	h[i] = str(bin(h[i]))[2:].rjust(8, "0")
# print(h)


# 00000001 00000010 00000011 00000100 00000101 00000110 00000111 00001000 00001001 00001010 00001011 00001100 00001101 00001110 00001111 00010000






