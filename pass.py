while True:
	print('who are you?')
	name = input('>')
	if name != 'joe':
		continue
	print('hello,JOE. what is the password')
	password = input ('>')
	if password == 'Fish':
		break
print ('access granted.')