import codecs

# 8CEF67B467F480D9CD4B768662ACE0BC39B5C06AFB1F0295621EDC7584397650
# jO9ntGf0gNnNS3aGYqzgvDm1wGr7HwKVYh7cdYQ5dlA=
# d4 01 4b e0
# a5 37 7c 79
# 14 2b de bf
# b2 e3 5e b6

# d4a514b201372be34b7cde5ee079bfb6
# 2a69736d79646174617365637572653f

he_input = ""
b_input = "jO9ntGf0gNnNS3aGYqzgvDm1wGr7HwKVYh7cdYQ5dlA="

# flag = True
# while flag:
# 	test = input("Again(y/n) ?")
# 	if(test=="y"):
# 		flag = True
# 	else:
# 		flag = False


he = "d4a514b201372be34b7cde5ee079bfb6"
b = codecs.encode(codecs.decode(he, 'hex'), 'base64').decode()

# r = codecs.encode(codecs.decode(b_input, 'base64'), 'hex').decode()

print(b)

