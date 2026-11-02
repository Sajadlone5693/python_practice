import random ,sys

messages=['it is certain',
'it is decidely so',
'yes definitely',
'reply hazy try again',
'ask again later',
'concentrate and ask again',
'my reply is no',
'outlook not so good',
'very doubtful']

while True:
	answer=input('Ask a yes or no question:')
	if answer.lower() =='q':
		print ('gameover')
		sys.exit()
	# print(messages[random.randint(0,(len(messages)-1))])
	print(random.choice(messages))
