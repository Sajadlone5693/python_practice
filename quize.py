import random
from pathlib import Path



capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':
'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':
'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'West Virginia':'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# print(len(list(capitals.keys())))
# print(Path.cwd())
for quiz_num in range(35):

	quiz_filename=f'capitalsquiz{quiz_num+1}.txt'
	answer_filename=f'capitalsanswers{quiz_num+1}.txt'
	quiz_file= open(quiz_filename, 'w')
	answer_file= open(answer_filename, 'w')
	quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quiz_file.write((' '*20)+f'state capitals quiz(Form {quiz_num+1})' +'\n\n')

	states=list(capitals.keys())
	random.shuffle(states)
	for num in range(50):
		correct_answer=capitals[states[num]]
		wrong_answers=list(capitals.values())
		del wrong_answers[wrong_answers.index(correct_answer)]
		wrong_answers=random.sample(wrong_answers,3)
		answer_options= wrong_answers + [correct_answer]
		random.shuffle(answer_options)
		questions=quiz_file.write(f'{num+1} What is the capital of {states[num]}:\n')
		for i in range(4):
			quiz_file.write(f'    {'ABCD'[i]}. {answer_options[i]}\n')
		quiz_file.write('\n')
		answer_file.write(f'{num+1}.{'ABCD'[answer_options.index(correct_answer)]} {correct_answer}\n')
	quiz_file.close()
	answer_file.close()

# file_number=0
# for f in Path.cwd().glob('cat*'):
# 	print(f'{file_number+1}: {f}')
# 	file_number+=1

	# print(Path('capitalsquiz1.txt').read_text())

