class Student:
	def __init__(self,name):
		self.name=name
		self.marks=[]
	def add_mark(self,score):
		self.marks.append(score)

	def average(self):
		return sum(self.marks) /len(self.marks)

	def show(self):
		print(f'{self.name}: {self.marks} average:{self.average()}')

#Test Case
s1 = Student('Sajad')
s1.add_mark(80)
s1.add_mark(90)
s1.show()

s2 = Student('Aisha')
s2.add_mark(70)
s2.add_mark(100)
s2.show()
