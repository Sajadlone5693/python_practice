# def hello():

# 	print ('Good Morning!')
# 	print ('Good Afternoon!')
# 	print ('Good Evening!')

# hello()
# hello()
# print('one more time!')
# hello()

# def say_hello_to(name):
# 	print ('Good Morning! '+ name)
# 	print ('Good Afternoon! '+ name)
# 	print ('Good Evening! '+ name)
# #call the function
# say_hello_to('sajad')
# say_hello_to('bob')


import random
import sys

def get_answers(answer_num):
	if answer_num==1:
		return 'It is certain'
	elif answer_num == 2:
	    return 'It is decidedly so'
	elif answer_num == 3:
	    return 'Yes'
	elif answer_num == 4:
	    return 'Reply hazy try again'
	elif answer_num == 5:
	    return 'Ask again later'
	elif answer_num == 6:
	    return 'Concentrate and ask again'
	elif answer_num == 7:
	    return 'My reply is no'
	elif answer_num == 8:
	    return 'Outlook not so good'
	elif answer_num == 9:
	    return 'Very doubtful'

while True:

	print('ask a yes, no question:')
	question=input('>')
	if question.lower()=='q':
		print('good bye!')
		sys.exit()
	#generate a random number r
	r=random.randint(1,9)
	fortune = get_answers(r)
	print(fortune)
