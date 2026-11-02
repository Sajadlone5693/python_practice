#number Game 
import random
Secret_number = random.randint(1,6)
print('choose a number betwee 1 to 6.')

#guess 3 times

for guess_taken in range (1,3):
	print ('take a guess')
	guess= int(input('>'))

	if guess <Secret_number:
		print ("higher")

	elif guess>Secret_number:
		print("lower")

	else:
		break
if guess == Secret_number:
	print('your guess is correct')
	print ('you guessed the correct number in '+ str(guess_taken) +' tries' )
else :
	print('well tried '+  ' is the Secret number'+ str(Secret_number))