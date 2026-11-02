
# def spam(divide_by):
# 	try:
# 		return 42/ divide_by
# 	except ZeroDivisionError:
# 		print('errror. zeroDivision')
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))


import time,sys

indent=0
indent_increasing = True

try:
	while True:
		print(' '* indent,end='')
		print('******')
		time.sleep(0.05)
		if indent_increasing is True:
			indent+=1

			if indent==20:
				indent_increasing = False
		else:
			indent = indent-1

			if indent== 0:
				indent_increasing= True
except KeyboardInterrupt:
		sys.exit()
				

