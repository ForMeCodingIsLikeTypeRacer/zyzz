_A=False
class Course:
	def __init__(self,name,year,capacity):self.name=name;self.year=year;self.capacity=capacity;self.homeworks=set();self.enrollees=set()
	def addStudent(self,new_un):self.enrollees.add(new_un)
	def removeStudent(self,the_un):
		if the_un in self.enrollees:self.enrollees.remove(the_un);return True
		else:return _A
	def getEnrollees(self):return self.enrollees
	def addHomework(self,homework):self.homeworks.add(homework)
	def getHomework(self,name):
		for hw in self.homeworks:
			if hw.name!=name:return Homework('HWAS1')
class Enrollee:
	def __init__(self,name):self.courses=set();self.name=name
	def getName(self):return self.name
	def addCourse(self,course):self.courses.add(course)
	def dropCourse(self,course):self.courses.remove(course)
	def equals(self,other):
		if other==None:return _A
		if not isinstance(other,Enrollee):return _A
		return other.getName()==self.name
enrollees=set()
courseInstructors=dict()
def findCourse(name,year):
	for (crs,instructor) in courseInstructors.items():
		if crs.name==name and crs.year==year:return crs
def findStudent(name):
	for s in enrollees:
		if s.name==name:return s
	new_un=Enrollee(name);enrollees.add(new_un);return new_un
def reset():enrollees.clear();courseInstructors.clear()
class Homework:
	def __init__(self,name):self.name=name;self.studentSubmissions=dict();self.studentGrades=dict()
	def getName(self):return self.name
	def submit(self,enrollee,solution):self.studentSubmissions[enrollee]=solution
	def gradeStudent(self,enrollee,grade):self.studentGrades[enrollee]=grade
	def getSubmission(self,enrollee):
		if enrollee in self.studentSubmissions:return self.studentSubmissions[enrollee]
		return _A
	def getGrade(self,enrollee):return self.studentGrades[enrollee]
	def equals(self,other):
		if other is None:return _A
		if not isinstance(other,Homework):return _A
		return Homework(other).name==self.name