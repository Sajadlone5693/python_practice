import random

# for i in range(100):
# 	if random.randint(0,1)==0:
# 		print('H', end=' ')
# 	else:
# 		print('T', end=' ')
# print()
i =0
while i<100:
	if random.randint(0,1) ==0:
		print('H', end=' ')
		# break
	else:
		print('T', end=' ')
		# break
	i+=1