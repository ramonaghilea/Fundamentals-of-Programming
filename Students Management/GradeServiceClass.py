from GradeRepoClass import GradeRepo
from GradeClass import Grade
from UndoControllerClass import *

class GradeService:
    def __init__(self, undoController, gradeRepo):
        
        self._undoController = undoController
        self._gradeRepo = gradeRepo

    def add_grade(self, grade_id, dis_id, stud_id, grade_value, recordUndo = True):
        try:
            grade_id = int(grade_id)
            dis_id = int(dis_id)
            stud_id = int(stud_id)
            grade_value = int(grade_value)
        except ValueError:"Not int"

        grade = Grade(grade_id, dis_id, stud_id, grade_value)
        self._gradeRepo.add_grade(grade)

        if recordUndo == True:
            undo = FunctionCall(self.remove_grade, grade_id) 
            redo = FunctionCall(self.add_grade, grade_id, grade.disciplineId, grade.studentId, grade.gradeValue)
            op = Operation(undo, redo)
            self._undoController.recordOperation(op)
        elif self._undoController.duringundo == False:
            undo = FunctionCall(self.remove_grade, grade_id)
            redo = FunctionCall(self.add_grade, grade_id, grade.disciplineId, grade.studentId, grade.gradeValue)
            op = Operation(undo, redo)
            return op

        return grade
    

    def filterGrades(self, stud_id, dis_id):
        """
        Return a list of rentals performed by the provided client for the provided car
        client - The client performing the rental. None means all clients
        cars - The rented car. None means all cars 
        """
        result = []
        for grade in self._gradeRepo.getAll():
            if stud_id != None and grade.studentId != stud_id:
                continue
            if dis_id != None and grade.disciplineId != dis_id:
                continue
            result.append(grade)
        return result

    def remove_grade(self, grade_id, recordUndo=True):
        grade = self._gradeRepo.remove_grade(grade_id)

        '''
        If the operation did not raise an Exception, then we record it for Undo/Redo
        '''
        if recordUndo == True:
            redo = FunctionCall(self.remove_grade, grade_id) 
            undo = FunctionCall(self.add_grade, grade_id, grade.disciplineId, grade.studentId, grade.gradeValue)
            op = Operation(undo, redo)
            self._undoController.recordOperation(op)
        elif self._undoController.duringundo == False:
            redo = FunctionCall(self.remove_grade, grade_id) 
            undo = FunctionCall(self.add_grade, grade_id, grade.disciplineId, grade.studentId, grade.gradeValue)
            op = Operation(undo, redo)
            return op
            
        return grade


    def remove_grades_by_stud_id(self, stud_id):
        self._gradeRepo.remove_grades_by_stud_id(stud_id)

    def remove_grades_by_dis_id(self, dis_id):
        self._gradeRepo.remove_grades_by_dis_id(dis_id)

    def getAll(self):
        return self._gradeRepo.getAll()

    def __str__(self):
        return str(self._gradeRepo)

    def init_grades(self):
        self._gradeRepo.init_grades()
    