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

for quiz_num in range(35):
	quiz_filenames= f"capitalsquiz{quiz_num+1}.txt"
	answer_filenames=f"capitalanswers{quiz_num+1}.txt"

	quiz_file=open(quiz_filenames,'w')
	answer_file= open(answer_filenames,'w')

	quiz_file.write(f"name:\n\ndate:\n\nperiod:\n\n\n {' '*15}State Capitals Quiz(Form{quiz_num+1})\n\n")

	states= list(capitals.keys())
	random.shuffle(states)

	for num in range(50):
		# print(states[num])
		correct_answer=capitals[states[num]]
		wrong_answers= list(capitals.values())
		del wrong_answers[wrong_answers.index(correct_answer)]
		wrong_answers= random.sample(wrong_answers,3)
		answerpool= [correct_answer]+wrong_answers
		random.shuffle(answerpool)
		quiz_file.write(f"{num+1}. what is the capital of {states[num]}:\n")
		for i in range (4):
			quiz_file.write(f'{' '*4}{'ABCD'[i]}. {answerpool[i]}.\n')
		answer_file.write(f"{num+1}. {'ABCD'[answerpool.index(correct_answer)]},{correct_answer}\n")
	answer_file.close()
	quiz_file.close()

# for p in Path.cwd().glob('*.txt'):
# 	# print(p)

print(Path('capitalanswers1.txt').read_text()[:400])
# print(states[num])	
# print(answerpool)
# print(correct_answer)
