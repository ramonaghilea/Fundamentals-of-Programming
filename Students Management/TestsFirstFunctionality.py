from StudentClass import Student
from DisciplineClass import Discipline
from GradeClass import Grade
from StudentRepoClass import StudentRepo
from DisciplineRepoClass import DisciplineRepo
from GradeRepoClass import GradeRepo
import  unittest

class TestsFirstFunctionality(unittest.TestCase):

    
    def testStudent_CreateStudent(self):
        stud_id = 56
        stud_name = "Will Smith"
        stud = Student(stud_id, stud_name)
        self.assertEqual(stud.studentId, 56)
        self.assertEqual(stud.studentName, "Will Smith")
    
    def testStudentRepo_addStudent(self):
        self._students = StudentRepo()
        self._students.add_student(56, "Hill Nina")
        stud = self._students.getStudentById(56)
        stud2 = Student(56, "Hill Nina")
        self.assertEqual(stud.studentId, stud2.studentId)
        self.assertEqual(stud.studentName, stud2.studentName)
        
    def testStudentRepo_removeStudent(self):
        self._students = StudentRepo()
        self._students.add_student(23, "Kinder Sah")
        self._students.remove_student(23)
        self.assertEqual(len(self._students.getAll()), 0)
        
    def testStudentRepo_updateStudent(self):
        self._students = StudentRepo()
        self._students.add_student(23, "Kinder Sah")
        self._students.update_student(23, "Joy")
        stud = Student(23, "Joy")
        stud2 = self._students.getStudentById(23)
        self.assertEqual(stud.studentId, stud2.studentId)
        self.assertEqual(stud.studentName, stud2.studentName)

    def testDiscipline_CreateDiscipline(self):
        dis_id = 100
        dis_name = "Organic Chemestry"
        dis = Discipline(dis_id, dis_name)
        self.assertEqual(dis.disciplineId, 100)
        self.assertEqual(dis.disciplineName, "Organic Chemestry")
    
    def testDisciplineRepo_addDiscipline(self):
        self._disciplines = DisciplineRepo()
        self._disciplines.add_discipline(100, "Chemestry")
        dis = self._disciplines.getDisciplineById(100)
        dis2 = Discipline(100, "Chemestry")
        self.assertEqual(dis.disciplineId, dis2.disciplineId)
        self.assertEqual(dis.disciplineName, dis2.disciplineName)
        
    def testDisciplineRepo_removeDiscipline(self):
        self._disciplines = DisciplineRepo()
        self._disciplines.add_discipline(94, "Maths")
        self._disciplines.remove_discipline(94)
        self.assertEqual(len(self._disciplines.getAll()), 0)
        
    def testDisciplineRepo_updateDiscipline(self):
        self._disciplines = DisciplineRepo()
        self._disciplines.add_discipline(23, "Computer Science")
        self._disciplines.update_discipline(23, "Latin")
        dis = Discipline(23, "Latin")
        dis2 = self._disciplines.getDisciplineById(23)
        self.assertEqual(dis.disciplineId, dis2.disciplineId)
        self.assertEqual(dis.disciplineName, dis2.disciplineName)

if __name__ == '__main__':
    unittest.main()
