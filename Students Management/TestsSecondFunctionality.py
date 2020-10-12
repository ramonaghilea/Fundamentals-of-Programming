from StudentClass import Student
from DisciplineClass import Discipline
from GradeClass import Grade
from StudentRepoClass import StudentRepo
from DisciplineRepoClass import DisciplineRepo
from GradeRepoClass import GradeRepo
import  unittest

class TestsSecondFunctionality(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def testGradeRepo_addGrade(self):
        self._students = StudentRepo()
        self._disciplines = DisciplineRepo()
        self._grades = GradeRepo()
        self._students.add_student(56, "Hill Nina")
        self._students.add_student(30, "Christina Shepherd")
        self._disciplines.add_discipline(78, "Maths")
        self._disciplines.add_discipline(120, "Physics")

        self._grades.add_grade(78, 30, 7)
        self.assertEqual(len(self._grades.getAll()), 1)

        self._grades.add_grade(120, 56, 10)
        self.assertEqual(len(self._grades.getAll()), 2)