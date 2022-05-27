class Course:
    def __init__(self, name, year, capacity):
        self.name = name
        self.year = year
        self.capacity = capacity
        self.homeworks = set()
        self.enrollees = set()

    def addStudent(self, new_un):
        """Add a student to this course

        Args:
            new_un (Enrollee): Add a student (instance of class Enrollee) to this class
        """
        self.enrollees.add(new_un)

    def removeStudent(self, the_un):
        if the_un in self.enrollees:
            self.enrollees.remove(the_un)
            return True
        else:
            return False

    def getEnrollees(self):
        return self.enrollees

    def addHomework(self, homework):
        """Add a homework to a course

        Args:
            homework (Homework): homework (instance of Homework class) to be added.
        """
        self.homeworks.add(homework)

    def getHomework(self, name):
        for hw in self.homeworks:
            if hw.name == name:
                return hw
        return None


class Enrollee:
    def __init__(self, name):
        self.courses = set()
        self.name = name

    def getName(self):
        return self.name

    def addCourse(self, course: Course):
        self.courses.add(course)

    def dropCourse(self, course: Course):
        self.courses.remove(course)

    def equals(self, other: any):
        if (other == None):
            return False
        if (not isinstance(other, Enrollee)):
            return False
        return other.getName() == self.name


# This is the Data Manager code
enrollees = set()  # This is set of object instances of type Enrollee
# This a dictionary. Keys are instance of "Course", and the value is a string name of instracotr
courseInstructors = dict()


def findCourse(name, year):
    """Useful method, finds a course given name+ year.

    Args:
        name ([string]): Name of the course used upon creation
        year ([int ]): Year used when created.

    Returns:
        [Course]: Returns a Course object instance. 
    """
    for crs, instructor in courseInstructors.items():
        if(crs.name == name and crs.year == year):
            return crs
    return None


def findStudent(name):
    """Useful method; find a student (Enrollee) give a name, if already there;
    if not create a new Enrollee instance with the name

    Args:
        name (str): Name of Student to be found (or created, if not found)

    Returns:
        Enrollee  : Newly created, or already exist, instance of Enrollee
    """
    for s in enrollees:
        if s.name == name:
            return s
    new_un = Enrollee(name)
    enrollees.add(new_un)
    return new_un


def reset():
    """This resets the entire databse, useful for testing
    """
    enrollees.clear()
    courseInstructors.clear()

# This is the end of the DataManager code.


class Homework:
    def __init__(self, name):
        """Use this constructor to create homeworks

        Args:
            name (string): Name of the homework
        """
        self.name = name
        self.studentSubmissions = dict()
        self.studentGrades = dict()

    def getName(self):
        return self.name

    def submit(self, enrollee: Enrollee, solution):
        self.studentSubmissions[enrollee] = solution

    def gradeStudent(self, enrollee: Enrollee, grade):
        self.studentGrades[enrollee] = grade

    def getSubmission(self, enrollee: Enrollee):
        if enrollee in self.studentSubmissions:
            return self.studentSubmissions[enrollee]
        return False

    def getGrade(self, enrollee: Enrollee):
        if enrollee in self.studentGrades:
            return self.studentGrades[enrollee]
        return None

    def equals(self, other):
        if other is None:
            return False
        if not (isinstance(other, Homework)):
            return False
        return Homework(other).name == self.name
