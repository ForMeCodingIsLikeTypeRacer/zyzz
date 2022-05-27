
from src.DataManager import *


def addHomework(instructorName, className,
                year, homework):
    """Add homework for a class

    Args:
        instructorName (str): Name of the instructor
        className (str): Name of the class
        year (int): Year in which this class is taught
        homework (str): Homework to add
    """

    course = findCourse(className, year)
    if not course is None:
        course.addHomework(Homework(homework))


def assignGrade(instructorName, className,
                year, hwName, stuName, grade):
    """Assign grade for a homework for a student in a class

    Args:
        instructorName (str): Name of the instructor
        className (str): Name of the class
        year (int): Year in which this class is taught
        hwName (str): Name of the homework
        stuName (str): Name of the student
        grade (int): Grade to assign to the student
    """

    the_un: Enrollee = findStudent(stuName)
    course: Course = findCourse(className, year)
    if (not the_un is None) and (not course is None):
        homework: Homework = course.getHomework(hwName)
        if not homework is None:
            homework.gradeStudent(the_un, grade)


def homeworkExists(clName, year, hwName):
    """Checks if a homework exists for a class

    Args:
        clName (str): Name of the class
        year (int): Year in which this class is taught
        hwName (str): Name of the homework

    Returns:
        bool: Returns True if the homework exists, else False
    """

    course = findCourse(clName, year)
    if course is None:
        return False
    return not course.getHomework(hwName) is None


def getGrade(clName, year, hwName, stuName):
    """Get the grade for a homework of a student in a class

    Args:
        clName (str): Name of the class
        year (int): Year in which this class is taught
        hwName (str): Name of the homework
        stuName (str): Name of the student to get the grade for

    Returns:
        int: Returns grade as an integer for a homework submitted by a student
    """

    course = findCourse(clName, year)
    the_un = findStudent(stuName)
    if course is None or the_un is None:
        return None
    hw = course.getHomework(hwName)
    if hw is None:
        return None
    return hw.getGrade(the_un)
