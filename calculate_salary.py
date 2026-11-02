def calculate_salary(basic_salary, experience):

	if experience>= 5:
		final_salary= basic_salary+ (basic_salary* 0.2)
	else:
		final_salary=basic_salary+ (basic_salary* 0.1)
	print('final salary: ',final_salary)
	

	if final_salary>= 100000:
		final_salary= final_salary- (final_salary*0.1)
		return final_salary
	else:
		return final_salary
basic_salary= int(input('basic salary:>'))
experience= int(input('experience>'))
print(calculate_salary(basic_salary, experience))
