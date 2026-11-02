import random,sys
print('Rock,Paper,Scissors'.upper())

wins= 0
losses=0
ties=0

while True:
	print(f"{wins} wins, {losses} losses, {ties} ties".upper())
	while True:
		player_input=input('>')
		
		if player_input == 'q':
			print('game over'.upper())
			sys.exit()

		else: 
			player_input == 'r' or player_input=='p' or player_input=='s'
			break
	if player_input=="r":
		print('Rock vs '.upper() ,end='')
	elif player_input=='p':
		print('Paper vs '.upper(),end='')
	elif player_input=='s':
		print('Scissor vs '.upper(),end='')
	#computer move
	move_number=random.randint(1,3)
	# print(move_number)
	if move_number==1:
		computer_move= 'r'
		print('Rocks'.upper())
	elif move_number==2:
		computer_move='p'
		print('Paper'.upper())
	elif move_number==3:
		computer_move='s'
		print('Scissor'.upper())

	#check

	if player_input==computer_move:
		print('it is a tie'.upper())
		ties +=1
	elif player_input=='r' and computer_move=='s'or\
	player_input=='p' and computer_move=='r'or\
	player_input=='s' and computer_move=='p':
		print('You win'.upper())
		wins+=1

	if player_input=='s' and computer_move=='r'or\
	player_input=='r' and computer_move=='p'or\
	player_input=='p' and computer_move=='s':
		print('You loose'.upper())
		losses+=1




