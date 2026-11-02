# def flatten(messy):

# 	new_list=[]
# 	for item in messy:
# 		if type(item) != list:
# 			new_list.append(item)
# 			# print(new_list)	
# 		else:
# 			new_list.extend(flatten(item))
# 			# print(new_list)
# 	return new_list	
# messy=[1, 2, [3, 4], 5, [[6, [7, 8], 9],10],11]
# print(flatten(messy))




def remove_duplicates(given_list):
	new_list=[]

	for items in given_list:
		if items not in new_list:
			new_list.append(items)
	# return new_list
given_list=[1, 3, 3, 5, 5, 5, 7, 1, 9]
print(remove_duplicates(given_list))