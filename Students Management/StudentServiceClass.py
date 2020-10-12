from StudentRepoClass import StudentRepo
from StudentClass import Student
from copy import deepcopy
from ExceptionsClass import *
from UndoControllerClass import *
from GradeServiceClass import GradeService

class StudentService:
    def __init__(self, undoController, studentRepo, gradesService):
        self._undoController = undoController
        self._studentRepo = studentRepo
        self._gradesService = gradesService

    def getAll(self):
        return self._studentRepo.getAll()

    def add_student(self, stud_id, stud_name):

        try:
            stud_id = int(stud_id)
        except IntException:"Id not integer"

        stud = Student(stud_id, stud_name)
        self._studentRepo.add_student(stud)

        redo = FunctionCall(self.add_student, stud_id, stud_name)
        undo = FunctionCall(self.remove_student, stud_id)

        op = Operation(undo, redo)
        self._undoController.recordOperation(op)

        return stud

    def remove_student(self, stud_id):
        stud = self._studentRepo.remove_student(stud_id)

        undo = FunctionCall(self.add_student, stud_id, stud.studentName)
        redo = FunctionCall(self.remove_student, stud_id)

        cop = CascadedOperation(Operation(undo, redo))

        if self._undoController.duringundo == False:
            grades = self._gradesService.filterGrades(stud_id, None)
            for gr in grades:
                op = self._gradesService.remove_grade(gr.gradeId, False)
                if self._undoController.duringundo == False:
                    cop.add(op)

        self._undoController.recordOperation(cop)

        return stud

    def update_student(self, stud_id, new_stud_name):

        try:
            stud_id = int(stud_id)
        except ValueError:"Not int"

        if stud_id == None:
            raise NoneException("Id is none")
        if stud_id < 0:
            raise NegativeException("Id is negative")
        ok = False
        for stud in self._studentRepo.getAll():
            if stud.studentId == stud_id:
                ok = True  
        if ok == False:
            raise NonexistentException("Nonexistent Id")
        if new_stud_name == None:
            raise NoneException("Name is none")

        old_stud = self._studentRepo.getStudentById(stud_id)
        new_stud = Student(stud_id, new_stud_name)
        
        self._studentRepo.update_student(new_stud)

        redo = FunctionCall(self.update_student, stud_id, new_stud_name)
        undo = FunctionCall(self.update_student, stud_id, old_stud.studentName)

        op = Operation(undo, redo)
        self._undoController.recordOperation(op)

        return new_stud
    
    def getStudentById(self, stud_id):
        return self._studentRepo.getStudentById(stud_id)
    
    def search_student_id(self, stud_id):

        if stud_id == None:
            raise NoneException("Id is none")
        try:
            stud_id = int(stud_id)
        except IntException:"Id not integer"
        if stud_id < 0:
            raise NegativeException("Id is negative")

        matches = []
        for stud in self._studentRepo.getAll():
            match = False
            match = stud_id == stud.studentId
            if match == True:
                matches.append(stud)
                
        return matches

    def search_student_name(self, stud_name):

        if stud_name == None:
            raise NoneException("Name is none")

        matches = []
        for stud in self._studentRepo.getAll():
            match = False
            match = stud.studentName.lower().find(stud_name.lower()) != -1
            if match == True:
                matches.append(stud)

        return matches
    
    def __str__(self):
        return str(self._studentRepo)

    def init_students(self):
        self._studentRepo.init_students()