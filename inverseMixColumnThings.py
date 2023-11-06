def calculate(l1, l2):
	polynomial1 = []
	polynomial2 = []
	result_poly = []
	final_result_poly = []
	result = []
	final_result = ""
	temp = 0
	temp2 = 0
	ll1 = []
	ll2 = []
	for i in range(4): # convert hex to binary
		ll1.append(bin(int(l1[i], 16))[2:].rjust(8, "0"))
		ll2.append(bin(int(l2[i], 16))[2:].rjust(8, "0"))
	
	for i in range(4): # convert binary to polynomial
		polynomial1 = []
		polynomial2 = []
		temp = 7 # max polynomial
		for j in ll1[i]:
			if(j=="1"):
				polynomial1.append("x"+str(temp))
			temp = temp-1
		temp2 = 7 # max polynomial
		for j in ll2[i]:
			if(j=="1"):
				polynomial2.append("x"+str(temp2))
			temp2 = temp2-1
		# print(polynomial1)
		# print(polynomial2)
		for j in polynomial1:
			for s in polynomial2:
				# print("x"+str(int(j[1])+int(s[1])))
				if(len(j)==3 and len(s)==3): # i think not ness
					result_poly.append("x"+str(int(j[1]+j[2])+int(s[1]+s[2])))
				elif(len(j)==3):
					result_poly.append("x"+str(int(j[1]+j[2])+int(s[1])))
				elif(len(s)==3):
					result_poly.append("x"+str(int(j[1])+int(s[1]+s[2])))
				else:
					result_poly.append("x"+str(int(j[1])+int(s[1])))
		# print(result_poly,"\n")
		if(result_poly.count("x10")>=1):
			for ss in range(result_poly.count("x10")):
				result_poly.remove("x10")
				result_poly.append("x6")
				result_poly.append("x5")
				result_poly.append("x3")
				result_poly.append("x2")
		if(result_poly.count("x9")>=1):
			for ss in range(result_poly.count("x9")):
				result_poly.remove("x9")
				result_poly.append("x5")
				result_poly.append("x4")
				result_poly.append("x2")
				result_poly.append("x1")
		if(result_poly.count("x8")>=1):
			for ss in range(result_poly.count("x8")):
				result_poly.remove("x8")
				result_poly.append("x4")
				result_poly.append("x3")
				result_poly.append("x1")
				result_poly.append("x0")
		# print(polynomial1)
		# print(polynomial2)
		# print(result_poly,"\n")

	for i in range(8): # x count checking
		if(result_poly.count("x"+str(i))!= 0 and result_poly.count("x"+str(i))%2 != 0):
			final_result_poly.append("x"+str(i))
		# elif(result_poly.count("x"+str(i))!= 0 and result_poly.count("x"+str(i))%2 == 0):
		# 	print("x"+str(i)+" does not include")
		# else:
		# 	print("x"+str(i)+" does not include")
		if(final_result_poly.count("x"+str(i))==1):
			result.append("1")
		else:
			result.append("0")
	result.reverse() # get result
	# print(result)


	# if(result[0]=="1"):
	# 	final_result = bin(int("".join(result), 2)^int("100011011", 2))[2:].rjust(8, "0")
	# else:
	# 	result.pop(0)
	# 	final_result = "".join(result)
	final_result = "".join(result)
	polynomial1.clear()
	polynomial2.clear()
	result_poly.clear()
	final_result_poly.clear()
	result.clear()
	temp = 0
	temp2 = 0
	return final_result

def main():
	predefine_matrix = [["0e", "0b", "0d", "09"], ["09", "0e", "0b", "0d"], ["0d", "09", "0e", "0b"], ["0b", "0d", "09", "0e"]]
	define_matrix = []
	column_matrix = [[], [], [], []]
	result_matrix = []
	for ii in range(4):
		define_matrix.append(input("Enter Row "+str(ii+1)+" from shift row : ").split())

	for s in range(4):
		for c in range(4):
			column_matrix[s].append(define_matrix[c][s])

	for i in range(4):
		for j in range(4):
			result_matrix.append(hex(int(calculate(predefine_matrix[i], column_matrix[j]), 2))[2:])
	result = ""
	for i in range(len(result_matrix)):
		if((i+1)%4!=0):
			result += result_matrix[i].rjust(2, "0")+" "
		else:
			result += result_matrix[i].rjust(2, "0")+"\n"
	print("after inverse mix column"+result)

main()
