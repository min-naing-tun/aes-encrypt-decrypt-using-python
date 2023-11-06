

def calculate(l1, l2):
	polynomial1 = []
	polynomial2 = []
	result_poly = []
	final_result_poly = []
	result = []
	final_result = ""
	temp = 0
	temp2 = 0
	ll1 = l1
	ll2 = l2
	for i in range(4): # convert hex to binary
		ll1[i] = bin(int(l1[i], 16))[2:].rjust(8, "0")
		ll2[i] = bin(int(l2[i], 16))[2:].rjust(8, "0")
	
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
				result_poly.append("x"+str(int(j[1])+int(s[1])))
		# print(polynomial1)
		# print(polynomial2)
		# print(result_poly)

	for i in range(9): # x count checking
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


	if(result[0]=="1"):
		final_result = bin(int("".join(result), 2)^int("100011011", 2))[2:].rjust(8, "0")
	else:
		result.pop(0)
		final_result = "".join(result)
	polynomial1.clear()
	polynomial2.clear()
	result_poly.clear()
	final_result_poly.clear()
	result.clear()
	temp = 0
	temp2 = 0
	return final_result