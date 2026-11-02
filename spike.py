# spike.py

import time,sys
try:
	while True:
		for i in range(1,8):
			print('_'* i**2)
			time.sleep(.2)
		for i in range(6,2,-1):
			print('_'* i**2)
			time.sleep(.2)


except KeyboardInterrupt:
	sys.exit()