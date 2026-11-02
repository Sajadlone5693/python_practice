def comma_code(items):
	number_items=len(items)
	if items==[]:
		return ''
	if number_items==1:
		return items[0]
	result=''

	for i in items[:-1]:
		result= result+i+', '
	result=result +'and '+ items[-1]
	return result

items=['apples', 'bananas', 'tofu', 'cats', 'hello']
print(comma_code(items))
