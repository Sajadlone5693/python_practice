# import sys
# def collatz(number):

# 	if number%2==0:
# 		print (number//2,end=' ')
# 		return number//2
# 	else:
# 		print(3* number+1, end=' ')
# 		return 3*number+1
# try:
# 	number=int(input('>'))
# 	if number==0:
# 		print('enter a positive integer')
# 		sys.exit()
# 	while number!=1:
# 		number= collatz(number)
# except ValueError:
# 	print('enter an integer values')
import random, sys, time

WIDTH = 70

try:
    columns = [0] * WIDTH
    while True:
        for i in range(len(columns)):
            if random.random() < 0.02:
                columns[i] = random.randint(4, 14)
            if columns[i] == 0:
                print(' ', end='')
            else:
                print(random.choice([0, 1]), end='')
                columns[i] -= 1
        print()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()