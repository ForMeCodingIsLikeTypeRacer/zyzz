
from src.DataManager import *


def registerForClass(stuName, clName, year):
    """Register for a class

    Args:
        stuName (str): Name of the student
        clName (str): Name of the class to enroll into
        year (int): Year in which this class is taught 
    """
    the_un = findStudent(stuName)
    course = findCourse(clName, year)
    if not (course is None or the_un is None):
        the_un.addCourse(course)
        course.addStudent(the_un)


def dropClass(stuName, clName, year):
    """Drop a class

    Args:
        stuName (str): Name of the student
        clName (str): Name of the class to drop
        year (int): Year in which this class is taught 
    """
    the_un = findStudent(stuName)
    course = findCourse(clName, year)
    if course == None or the_un == None:
        return False
    else:
        the_un.addCourse(course)
        course.removeStudent(the_un)
        return True

def submitHomework(stuName, hwName, answer,
                   clName, year):
    """Submit homework for a class

    Args:
        stuName (str): Name of the student
        hwName (str): Name of the homework to submit
        answer (str): Answer of the homework
        clName (str): Name of the class to submit homework for
        year (int): Year in which this class is taught 
    """
    the_un = findStudent(stuName)
    course = findCourse(clName, year)
    if not (course is None or the_un is None):
        hw = course.getHomework(hwName)
        if not hw is None:
            hw.submit(the_un, answer)


def isRegisteredFor(stuName, clName, year):
    """Check if a student has registered for a class

    Args:
        stuName (str): Name of the student to check registration for
        clName (str): Name of the class 
        year (int): Year in which this class is taught
    
    Returns:
        bool: True if the student has registered for the class, else False
    """
    the_un = findStudent(stuName)
    course = findCourse(clName, year)    
    if not (course == None or the_un == None):
        return the_un in course.getEnrollees()
    return False


def hasSubmitted(stuName, hwName, clName, year):
    """Check if the student has submitted homework for the class

    Args:
        stuName (str): Name of the student to check the submission 
        hwName (str): Name of the homework 
        clName (str): Name of the class to check the submission for
        year (int): Year in which this class is taught
    
    Returns:
        bool: True if the student has submitted the homework for the class, else False 
    """
    the_un = findStudent(stuName)
    course = findCourse(clName, year)
    if not (course is None or the_un is None):
        hw = course.getHomework(hwName)
        if not hw is None:
            return not hw.getSubmission(the_un) is None
    return False
