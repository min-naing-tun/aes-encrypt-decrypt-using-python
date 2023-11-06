row = []
after_row = []
result = ""

for i in range(4):
	row.append(input("Enter ROW "+str(i+1)+" value (0 0 0 0) : ").split())

result += (row[0][0])+" "
result += (row[0][1])+" "
result += (row[0][2])+" "
result += (row[0][3])+"\n"

result += (row[1][1])+" "
result += (row[1][2])+" "
result += (row[1][3])+" "
result += (row[1][0])+"\n"



result += (row[2][2])+" "
result += (row[2][3])+" "
result += (row[2][0])+" "
result += (row[2][1])+"\n"


result += (row[3][3])+" "
result += (row[3][0])+" "
result += (row[3][1])+" "
result += (row[3][2])





# for i in range(16):
# 	if((i+1)%4==0):
# 		result += after_row[i]+"\n"
# 	else:
# 		result += after_row[i]+" "

print("after shift row\n"+result) # for result

# l = result.split(" ")
# print(l)

# result = ""
# result += "[\""+(row[0][0])+"\", "
# result += "\""+(row[1][1])+"\", "
# result += "\""+(row[2][2])+"\", "
# result += "\""+(row[3][3])+"\"]\n"

# result += "[\""+(row[0][1])+"\", "
# result += "\""+(row[1][2])+"\", "
# result += "\""+(row[2][3])+"\", "
# result += "\""+(row[3][0])+"\"]\n"



# result += "[\""+(row[0][2])+"\", "
# result += "\""+(row[1][3])+"\", "
# result += "\""+(row[2][0])+"\", "
# result += "\""+(row[3][1])+"\"]\n"


# result += "[\""+(row[0][3])+"\", "
# result += "\""+(row[1][0])+"\", "
# result += "\""+(row[2][1])+"\", "
# result += "\""+(row[3][2])+"\"]"



# print("\nlist for insert\n"+result) # for result
