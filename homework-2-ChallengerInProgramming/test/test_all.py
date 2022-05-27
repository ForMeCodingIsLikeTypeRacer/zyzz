import src.Admin as Admin
import src.DataManager as DataManager
import src.Instructor as Instructor
import src.Student as Student
import unittest

class TestAdmin(unittest.TestCase):

    def setUp(self):
        '''
        This method automatically gets called before every test.
        '''
        DataManager.reset()

    def test_nocourse(self):
        '''
        EXAMPLE TEST
        This method checks that a random course doesn't exist before cretion
        '''
        self.assertIsNone(DataManager.findCourse("ecs999", 2022))

    def test_class_does_not_exist(self):
        '''
        EXAMPLE TEST
        This method checks that a random course doesn't exist before cretion
        '''
        self.assertTrue(Admin.classExists("ecs161", 2022) == False)

    def test_class_exists(self):
        """
        EXAMPLE TEST
        This test creates a course, and checks that we
        can find the course.
        """
        Admin.createClass("ecs161", 2022, "Prem Devanbu", 101)
        self.assertTrue(Admin.classExists("ecs161", 2022))

    def test_newcourse(self):
        """
        EXAMPLE TEST
        This test creates a course with a name, for a year, and checks that
        a) The course with this name, and year is created correctly, and exists. 
        b) The course instructor is set correctly.
        """
        Admin.createClass("ecs161", 2022, "Prem Devanbu", 101)
        course = DataManager.findCourse("ecs161", 2022)
        self.assertIsNotNone(course)
        self.assertEqual(
            DataManager.courseInstructors[course],  "Prem Devanbu")

    def test_newEnrollee(self):
        """YOU MUST WRITE THIS TEST
        This test creates a course, and an enrolls a student,
        and then checks that the student is indeed in the class. Use
        functions in Admin.py and Student.py
        """
        className = "ecs161"
        year = 2022
        instructorName = "Prem Devanbu"
        capacity = 101
        Admin.createClass(className,year,instructorName,capacity)
        
        stuName = "Tom"
        clName = "ecs161"
        Student.registerForClass(stuName,clName,year)
        self.assertTrue(Student.hasSubmitted("Tom Kwon","homework1","ecs161",2022) == False)
        self.assertTrue(Admin.getClassInstructor("ecs161",2022) == "Prem Devanbu")
        self.assertTrue(Student.isRegisteredFor(stuName,clName,year))


    def test_change_capacity(self):
        """YOU MUST WRITE THIS TEST
        This test creates a course, changes the capacity
        and then ensures that the capacity has indeed changed
        to the new value 
        """
        className = "ecs161"
        year = 2022
        instructorName = "Prem Devanbu"
        capacity = 101
        Admin.createClass(className,year,instructorName,capacity)
        
        newCapacity = Admin.getClassCapacity(className,year) + 10
        Admin.changeCapacity(className,year,newCapacity)
        self.assertTrue(Instructor.getGrade(className,2022,"homework1","Tom Kwon") == None)
        self.assertEqual(Admin.getClassCapacity(className,year), newCapacity)





class TestHomework(unittest.TestCase):

    def setUp(self) -> None:
        """This gets run before every test. 
        """
        DataManager.reset()

    def test_new_homework(self):
        """This test creates a course, and a homework for that course, and ensures that it exists. 
        YOU MUST WRITE. Use functions in DataManager Some of them will be
        top level functions, others will be methods in specific classes (e.g., Course)
        """
        
        className = "ecs161"
        year = 2022
        instructorName = "Prem Devanbu"
        capacity = 101
        Admin.createClass(className,year,instructorName,capacity)

        homework = "homework1"
        Instructor.addHomework(instructorName,className,year,homework)
        self.assertTrue(Instructor.homeworkExists(className,year,homework))   

    def test_newhomework_grade(self):
        """This test creates a course, registers a student in a course,
        adds a homework to the course, assigns a grade for the student,
        and checks that the grade the student actually has for that homework, for that course,
        is the grade that was assigned. 
        YOU MUST WRITE. 
        Use functions in DataManager, Student, Instructor, Admin, etc, as needed
        """
        className = "ecs161"
        year = 2022
        instructorName = "Prem Devanbu"
        capacity = 101
        Admin.createClass(className,year,instructorName,capacity)
        
        studentName = "Tom Kwon"        
        Student.registerForClass(studentName,className,year)

        homework = "homework1"
        grade = 100
        Instructor.addHomework(instructorName,className,year,homework)
        Instructor.assignGrade(instructorName,className,year,homework,studentName,grade)
        self.assertEqual(grade, Instructor.getGrade(className,year,homework,studentName))


class TestInstructor(unittest.TestCase):

    def setUp(self) -> None:
        DataManager.reset()

    def test_add_homework(self):
        """EXAMPLE TEST
        Create a course, make sure it exists;
        then add a homework, and check that the homework exists
        """
        Admin.createClass("ecs161", 2022, "Prem Devanbu", 101)
        course = DataManager.findCourse("ecs161", 2022)
        self.assertIsNotNone(course)
        Instructor.addHomework("Prem Devanbu", "ecs161", 2022, "HW1")
        self.assertTrue(Instructor.homeworkExists("ecs161", 2022, "HW1"))

    def test_get_grade_with_no_course(self):
        """YOU MUST WRITE THIS TEST
        If you try to get the grade for a student, for a course that does not exist,
        you will get 'None'
        """
        self.assertTrue(Student.dropClass("Tom Kwon","ecs161",2022) == False)
        self.assertTrue(Admin.getClassInstructor("ecs161",2022) == None)
        self.assertTrue(Admin.getClassCapacity("ecs161",2022) == -1)
        self.assertTrue(Instructor.homeworkExists("ecs161",2022,"homework1") == False)
        self.assertTrue(Instructor.getGrade("ecs161",2022,"homework1","Tom Kwon") == None)
        

    def test_get_grade_with_no_grading(self):
        """YOU MUST WRITE THIS TEST
        FOr this test, you will create a class, create a homework in that class,
        add a student to that class, but NOT assign a grade for that student (see Instructor.py, for
        the relevant function, but don't call it) and then ensure that the grade for that student is NOne.
        """
        Admin.createClass("ecs161", 2022, "Prem Devanbu", 101)
        Instructor.addHomework("Prem Devanbu","ecs161",2022,"homework1")
        Student.registerForClass("Tom Kwon","ecs161",2022)
        self.assertTrue(Instructor.getGrade("ecs161",2022,"homework1","Tom Kwon") == None)


    def test_get_the_grade(self):
        """YOU MUST WRITE THIS TEST
        FOr this test, you will create a class, create a homework in that class,
        add a student to that class, then assign a grade for that student (see Instructor.py, for
        the relevant function) and then ensure that the grade for that student is correct (any
        integer value can be a grade)
        """
        Admin.createClass("ecs161", 2022, "Prem Devanbu", 101)
        Instructor.addHomework("Prem Devanbu","ecs161",2022,"homework1")
        Student.registerForClass("Tom Kwon","ecs161",2022)
        Instructor.assignGrade("Prem Devanbu","ecs161",2022,"homework1","Tom Kwon",100)
        self.assertTrue(Instructor.getGrade("ecs161",2022,"homework1","Tom Kwon") == 100)



class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        DataManager.reset()

    def test_register_for_class_for_no_course(self):
        """YOU MUST WRITE THIS TEST
        If you add a student for a course that does not exist, 
        then the student is not registered for the course. 
        """
        
        Student.registerForClass("Tom Kwon","DAWG TOWN", 2022)
        course = DataManager.findCourse("DAWG TOWN", 2022)
        self.assertTrue(Student.isRegisteredFor("Tom Kwon","DAWG TOWN",2022) == False)

    def test_drop_class(self):
        """YOU MUST WRITE THIS TEST
        This test will a) Create a class, b) register a student for the class, 
        c) drop teh student, and, then after this d) ensure that the student is NOT REGISTERED
        for the class.
        """
        Admin.createClass("ecs161", 2022, "Prem Devanbu", 101)
        Student.registerForClass("Tom Kwon","ecs161",2022)
        Student.dropClass("Tom Kwon","ecs161",2022)
        self.assertTrue(Student.isRegisteredFor("Tom Kwon","ecs161",2022) == False)

    def test_submit_homework(self):
        """YOU MUST WRITE THIS TEST
        For this test, a) Create a class, b) add a homework, c) add a student
        d) student submits the homework e) now check that teh student has indeed
        submitted the homework. 
        """
        Admin.createClass("ecs161", 2022, "Prem Devanbu", 101)
        Instructor.addHomework("Prem Devanbu","ecs161",2022,"homework1")
        Student.registerForClass("Tom Kwon","ecs161",2022)
        Student.submitHomework("Tom Kwon","homework1","Hi","ecs161",2022)
        self.assertTrue(Student.hasSubmitted("Tom Kwon","homework1","ecs161",2022) == True)



if __name__ == "__main__":
    unittest.main()