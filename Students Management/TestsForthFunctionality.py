from StudentClass import Student
from DisciplineClass import Discipline
from GradeClass import Grade
from StudentRepoClass import StudentRepo
from DisciplineRepoClass import DisciplineRepo
from GradeRepoClass import GradeRepo
from StudentServiceClass import StudentService
from DisciplineServiceClass import DisciplineService
from SuperService import SuperService
import  unittest

class TestsForthFunctionality(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def testStudentRepo_statistics_students_failing(self):
        self._students = StudentRepo()
        self._disciplines = DisciplineRepo()
        self._grades = GradeRepo()


        self.__superService = SuperService(self._students, self._disciplines, self._grades)

        self._students.add_student(56, "Hill Nina")
        self._students.add_student(90, "Hol Guara")
        self._students.add_student(120, "Alex Cerg")

        self._disciplines.add_discipline(87, "Maths")
        self._disciplines.add_discipline(234, "Logic")
        self._disciplines.add_discipline(99, "Art")

        self._grades.add_grade(87, 56, 10)
        self._grades.add_grade(87, 56, 3)
        self._grades.add_grade(99, 120, 4) #student 120 should be in the result
        self._grades.add_grade(234, 120, 10)

        result = []
        result = self.__superService.students_failing()
        result2 = []
        result2.append(Student(120, "Alex Cerg"))

        self.assertEqual(result[0].studentId, result2[0].studentId)
        self.assertEqual(result[0].studentName, result2[0].studentName)

    def testStudentRepo_statistics_students_best_situation(self):
        self._students = StudentRepo()
        self._disciplines = DisciplineRepo()
        self._grades = GradeRepo()


        self.__superService = SuperService(self._students, self._disciplines, self._grades)

        self._students.add_student(56, "Hill Nina")
        self._students.add_student(90, "Hol Guara")
        self._students.add_student(120, "Alex Cerg")

        self._disciplines.add_discipline(87, "Maths")
        self._disciplines.add_discipline(234, "Logic")
        self._disciplines.add_discipline(99, "Art")

        self._grades.add_grade(87, 56, 10) #2
        self._grades.add_grade(87, 56, 3)
        self._grades.add_grade(99, 120, 4) #1
        self._grades.add_grade(234, 120, 10)

        result = []
        result = self.__superService.students_best_situation()
        result2 = []
        result2.append(Student(120, "Alex Cerg"))
        result2.append(Student(56, "Hill Nina"))

        self.assertEqual(result[0].studentId, result2[0].studentId)
        self.assertEqual(result[0].studentName, result2[0].studentName)

        self.assertEqual(result[1].studentId, result2[1].studentId)
        self.assertEqual(result[1].studentName, result2[1].studentName)

    def testDisciplineRepo_disciplines_with_grades(self):
        self._students = StudentRepo()
        self._disciplines = DisciplineRepo()
        self._grades = GradeRepo()


        self.__superService = SuperService(self._students, self._disciplines, self._grades)

        self._students.add_student(56, "Hill Nina")
        self._students.add_student(90, "Hol Guara")
        self._students.add_student(120, "Alex Cerg")

        self._disciplines.add_discipline(87, "Maths")
        self._disciplines.add_discipline(234, "Logic")
        self._disciplines.add_discipline(99, "Art")
        self._disciplines.add_discipline(178, "Chemestry")

        self._grades.add_grade(87, 56, 10)
        self._grades.add_grade(87, 56, 3)
        self._grades.add_grade(99, 120, 4)
        self._grades.add_grade(234, 120, 10)

        result = []
        result = self.__superService.disciplines_with_grades()
        result2 = []
        result2.append(Discipline(234, "Logic"))
        result2.append(Discipline(87, "Maths"))
        result2.append(Discipline(99, "Art"))

        self.assertEqual(result[0].disciplineId, result2[0].disciplineId)
        self.assertEqual(result[0].disciplineName, result2[0].disciplineName)

        self.assertEqual(result[1].disciplineId, result2[1].disciplineId)
        self.assertEqual(result[1].disciplineName, result2[1].disciplineName)