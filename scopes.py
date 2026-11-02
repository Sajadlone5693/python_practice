

def calculate_result(marks1,marks2,marks3):
	average = (marks1+marks2+marks3 )/3
	print('Average: ' + str(average))
	if marks1<40 or marks2<40 or marks3<40:
		return ('fail')
	if average>=80:
		return('A grade')
	elif average>=60:
		return('B grade')
	elif average>= 40:
		return('C grade')
marks1= int(input('subject 1: >'))
marks2= int(input('subject 2: >'))
marks3= int(input('subject 3: >'))
print (calculate_result(marks1,marks2,marks3))




