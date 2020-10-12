from DisciplineRepoClass import DisciplineRepo
from DisciplineClass import Discipline
from ExceptionsClass import *
from UndoControllerClass import *

class DisciplineService:
    def __init__(self, undoController, disciplineRepo, gradesService):
        self._undoController = undoController
        self._disciplineRepo = disciplineRepo
        self._gradesService = gradesService
    
    def add_discipline(self, dis_id, dis_name, teacher_name):

        try:
            dis_id = int(dis_id)
        except IntException:"Id not integer"

        dis = Discipline(dis_id, dis_name, teacher_name)
        self._disciplineRepo.add_discipline(dis)

        redo = FunctionCall(self.add_discipline, dis_id, dis_name, teacher_name)
        undo = FunctionCall(self.remove_discipline, dis_id)

        op = Operation(undo, redo)
        self._undoController.recordOperation(op)

        return dis

    def remove_discipline(self, dis_id):
        dis = self._disciplineRepo.remove_discipline(dis_id)

        undo = FunctionCall(self.add_discipline, dis_id, dis.disciplineName, dis.teacherName)
        redo = FunctionCall(self.remove_discipline, dis_id)

        cop = CascadedOperation(Operation(undo, redo))

        if self._undoController.duringundo == False:
            grades = self._gradesService.filterGrades(None, dis_id)
            for gr in grades:
                op = self._gradesService.remove_grade(gr.gradeId, False)
                if self._undoController.duringundo == False:
                    cop.add(op)

        self._undoController.recordOperation(cop)

        return dis

    def update_discipline(self, dis_id, new_dis_name, new_teacher_name):
        try:
            dis_id = int(dis_id)
        except ValueError:"Not int"
        if dis_id == None:
            raise NoneException("Id is none")
        if dis_id < 0:
            raise NegativeException("Id is negative")
        ok = False
        for dis in self._disciplineRepo.getAll():
            if dis.disciplineId == dis_id:
                ok = True  
        if ok == False:
            raise NonexistentException("Nonexistent Id")         
        if new_dis_name == None:
            raise NoneException("Name is none")

        old_dis = self._disciplineRepo.getDisciplineById(dis_id)
        new_dis = Discipline(dis_id, new_dis_name, new_teacher_name)
        
        self._disciplineRepo.update_discipline(new_dis)

        redo = FunctionCall(self.update_discipline, dis_id, new_dis_name, new_teacher_name)
        undo = FunctionCall(self.update_discipline, dis_id, old_dis.disciplineName, old_dis.teacherName)

        op = Operation(undo, redo)
        self._undoController.recordOperation(op)

        return new_dis

    def getAll(self):
        return self._disciplineRepo.getAll()

    def getDisciplineById(self, dis_id):
        return self._disciplineRepo.getDisciplineById(dis_id)

    def search_discipline_id(self, dis_id):

        if dis_id == None:
            raise NoneException("Id is none")
        try:
            dis_id = int(dis_id)
        except IntException:"Id not integer"
        if dis_id < 0:
            raise NegativeException("Id is negative")

        matches = []
        for dis in self._disciplineRepo.getAll():
            match = False
            match = dis_id == dis.disciplineId
            if match == True:
                matches.append(dis)
                
        return matches

    def search_discipline_name(self, dis_name):

        if dis_name == None:
            raise NoneException("Name is none")

        matches = []
        for dis in self._disciplineRepo.getAll():
            match = False
            match = dis.disciplineName.lower().find(dis_name.lower()) != -1
            if match == True:
                matches.append(dis)

        return matches

    def __str__(self):
        return str(self._disciplineRepo)

    def init_disciplines(self):
        self._disciplineRepo.init_disciplines()

    
