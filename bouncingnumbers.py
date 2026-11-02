#bouncingnumbers.py

import time, sys

var =1
numbers_increasing=True

try:
	while True:
		print('    '*(var-1),end='')
		print(var)
		time.sleep(0.1)
		if numbers_increasing:
			var+=1
			if var==10:
				numbers_increasing=False
		else:
			var-=1
			if var==1:
				numbers_increasing=True
except KeyboardInterrupt:
	sys.exit()


