import random,sys,time


try:
	width= 70
	columns = [0]*width
	while True:
		for i in range(len(columns)):
			if random.random()<0.03:
				columns[i]=random.randint(4,14)
			if columns[i]==0:
				print(' ',end='')
			else:
				print(random.choice([0,1]),end='')
				columns[i]-=1
		print ( )
		time.sleep(0.1)

except KeyboardInterrupt:
	sys.exit()