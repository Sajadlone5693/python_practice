def a():
	print('a() starts') #prints
	b() #calls b() prints b()
	d()# does not call immediatly because b()is called ,,,prints after 2nd return
	print('a() returns')#printd return 4th
	
def b():
	print('b() starts')# prints b() from previous a()
	c() #prints c() before d()
	print('c() returns')# return prints 2nd

def c():
	print('c() starts') #prints c() from b()
	print('c() returns')#return prints 1st

def d():
	print('d() starts')#prints after d() inside a()
	print('d() returns')#print return 3rd and returns back to a()

a()