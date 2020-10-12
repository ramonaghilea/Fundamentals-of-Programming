from StudentClass import Student
from DisciplineClass import Discipline
from GradeClass import Grade
from StudentRepoClass import StudentRepo
from DisciplineRepoClass import DisciplineRepo
from GradeRepoClass import GradeRepo
from StudentServiceClass import StudentService
from DisciplineServiceClass import DisciplineService
import  unittest

class TestsThirdFunctionality(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def testStudentRepo_search_student_id(self):
        self.studentRepo = StudentRepo()
        self._students = StudentService(self.studentRepo)
        self._students.add_student(56, "Hill Nina")
        self._students.add_student(90, "Hol Guara")
        self._students.add_student(120, "Alex Cerg")

        matches = []
        matches = self._students.search_student_id(56)
        matches2 = []
        matches2.append(Student(56, "Hill Nina"))

        self.assertEqual(matches[0].studentId, matches2[0].studentId)
        self.assertEqual(matches[0].studentName, matches2[0].studentName)

    def testStudentRepo_search_student_name(self):
        self.studentRepo = StudentRepo()
        self._students = StudentService(self.studentRepo)
        self._students.add_student(56, "Hill Nina")
        self._students.add_student(90, "Hol Guara")
        self._students.add_student(120, "Alex Cerg")

        matches = []
        matches = self._students.search_student_name("h")
        matches2 = []
        matches2.append(Student(56, "Hill Nina"))
        matches2.append((Student(90, "Hol Guara")))

        self.assertEqual(matches[0].studentId, matches2[0].studentId)
        self.assertEqual(matches[0].studentName, matches2[0].studentName)

        self.assertEqual(matches[1].studentId, matches2[1].studentId)
        self.assertEqual(matches[1].studentName, matches2[1].studentName)

    def testDisciplineRepo_search_discipline_id(self):
        self.disciplineRepo = DisciplineRepo()
        self._disciplines = DisciplineService(self.disciplineRepo)
        self._disciplines.add_discipline(90, "Maths")
        self._disciplines.add_discipline(83, "Mathematical Analasys")

        matches = []
        matches = self._disciplines.search_discipline_id(83)
        matches2 = []
        matches2.append(Discipline(83, "Mathematical Analasys"))

        self.assertEqual(matches[0].disciplineId, matches2[0].disciplineId)
        self.assertEqual(matches[0].disciplineName, matches2[0].disciplineName)

    def testDisciplineRepo_search_discipline_name(self):
        self.disciplineRepo = DisciplineRepo()
        self._disciplines = DisciplineService(self.disciplineRepo)
        self._disciplines.add_discipline(90, "Maths")
        self._disciplines.add_discipline(83, "Mathematical Analasys")

        matches = []
        matches = self._disciplines.search_discipline_name("math")
        matches2 = []
        matches2.append(Discipline(90, "Maths"))
        matches2.append(Discipline(83, "Mathematical Analasys"))

        self.assertEqual(matches[0].disciplineId, matches2[0].disciplineId)
        self.assertEqual(matches[0].disciplineName, matches2[0].disciplineName)

        self.assertEqual(matches[1].disciplineId, matches2[1].disciplineId)
        self.assertEqual(matches[1].disciplineName, matches2[1].disciplineName)

