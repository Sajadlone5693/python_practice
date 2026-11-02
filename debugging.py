def box_print(symbol,width,height):
	if len(symbol) !=1:
		raise Exception('symbol must me 1 character string')
	if width<=2:
		raise Exception('width must me greater than 2')
	if height<=2:
		raise Exception('height must me greater than 2')

	print(symbol*width)

	for i in range (height-2):
		print(symbol+(' '*(width-2))+symbol)
	print(symbol*width )
try:
	box_print('*',10,9)
	box_print('0',20,5)
	box_print('x',1,3)
	box_print('zz',3,3)
except Exception as err:
	print('A Exception happned: '+ str(err))
try:
	box_print('zz',3,3)
except Exception as err:
	print('A Exception happned: '+ str(err))
