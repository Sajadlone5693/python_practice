
import random
Streak_number=0
total_streaks=0



for experiment_number in range(10000): 

	flips=[]
	for i in range(100):

		flips.append(random.choice(['H','T']))


	streak_found=False

	for i in range(95):
		if flips[i:i + 6]==['H', 'H', 'H', 'H', 'H', 'H']or flips[i:i + 6]==['T', 'T', 'T', 'T', 'T', 'T']:
			total_streaks+=1
			streak_found=True
	if streak_found==True:
		Streak_number+=1

print(total_streaks)
print(Streak_number)
print(round(total_streaks/(95*10000)*100,3))
print('streak chance in 10000 flips is: '+str(Streak_number/100)+'%')



