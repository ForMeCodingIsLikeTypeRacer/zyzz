from src import DataManager
from src.DataManager import *


# def resetAll():
#   """ Resets all the data
#   Good for test.
#   """
##  courseInstructors = dict()


def createClass(className, year, instructorName, capacity):
    """Creates a new class

    Args:
        className (str): Name of the class/course
        year (int): year Calendar year in which the course is to be taught
        instructorName (str): instructorName Name of instructor to be assigned,
        capacity (int): capacity Maximum capacity of this class 
    """

    course = Course(className, year, capacity)
    courseInstructors[course] = instructorName


def changeCapacity(className, year, capacity):
    """Changes capacity of the class

    Args:
        className (str): Name of the class for which capacity should be changed
        year (int): Year in which this class is taught
        capacity (int): New capacity of this class, must be at least equal to the number of students enrolled
    """

    course = findCourse(className, year)
    if not course is None:
        course.capacity = capacity


def classExists(className, year):
    """Check if the class exists
    Args:
        className (str): Name of the class 
        year (int): Year in which this class is taught

    Returns:
        bool: Returns true if the class exists
    """

    return findCourse(className, year) != None


def getClassInstructor(className, year):
    """Get the instructor of the class
    Args:
        className (str): Name of the class
        year (int): Year in which this class is taught

    Returns:
        str: Returns name of the instructor if the class exists
    """

    course = findCourse(className, year)
    if course is None:
        return None
    else:
        return courseInstructors[course]


def getClassCapacity(className, year):
    """Get the capacity of the class
    Args:
        className (str): Name of the class
        year (int): Year in which this class is taught

    Returns:
        int: Returns the capacity of the class as integer
    """

    course = findCourse(className, year)
    if course is None:
        return -1
    else:
        return course.capacity
