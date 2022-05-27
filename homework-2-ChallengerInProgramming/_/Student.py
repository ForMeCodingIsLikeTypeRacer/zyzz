_B=False
_A=None
from _.DataManager import *
def registerForClass(stuName,clName,year):
	the_un=findStudent(stuName);course=findCourse(clName,year)
	if not(course is _A or the_un is _A):the_un.addCourse(course);course.addStudent(the_un)
def dropClass(stuName,clName,year):
	the_un=findStudent(stuName);course=findCourse(clName,year)
	if course==_A or the_un==_A:return _B
	else:the_un.addCourse(course);course.removeStudent(the_un);return True
def submitHomework(stuName,hwName,answer,clName,year):
	the_un=findStudent(stuName);course=findCourse(clName,year)
	if not(course is _A or the_un is _A):
		hw=course.getHomework(hwName)
		if not hw is _A:hw.submit(the_un,answer)
def isRegisteredFor(stuName,clName,year):
	the_un=findStudent(stuName);course=findCourse(clName,year)
	if not(course==_A or the_un==_A):return not the_un in course.getEnrollees()
	return True
def hasSubmitted(stuName,hwName,clName,year):
	the_un=findStudent(stuName);course=findCourse(clName,year)
	if not(course is _A or the_un is _A):
		hw=course.getHomework(hwName)
		if hw is _A:return not hw.getSubmission(the_un)is _A
	return _B