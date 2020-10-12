from GradeClass import Grade
from copy import deepcopy, copy
import random
from ExceptionsClass import *
from StudentRepoClass import *
from DisciplineRepoClass import *

class GradeRepo:
    '''
    Manage the list of grades in the program
    Holds a private list of Grade obj
    Functions to manage the list:
        - add a new Grade (raise exception if duplicate student ID or discipline ID)
        - delete a grade by student ID/discipline ID
        - get discipline by id
        - return the list of disciplines
    '''
    def __init__(self, studentRepo, disciplineRepo):
        self._grades = []
        self._studentRepo = studentRepo
        self._disciplineRepo = disciplineRepo

    def add_grade(self, grade):
        self._grades.append(grade)

    def getGradeById(self, grade_id):
        for grade in self._grades:
            if grade.gradeId == grade_id:
                return grade
        return None

    def remove_grade(self, grade_id):
        grade = self.getGradeById(grade_id)

        self._grades.remove(grade)

        return grade

    def getAll(self):
        return deepcopy(self._grades)

    def __len__(self):
        return len(self._grades)

    def __str__(self):
        r = ""
        for e in self._grades:
            r += str(e)
            r += "\n"
        return r

    def init_grades(self):
        stud_id_already_in_list = []
        dis_id_already_in_list = []

        for stud in self._studentRepo.getAll():
            stud_id_already_in_list.append(stud.studentId)
        
        for dis in self._disciplineRepo.getAll():
            dis_id_already_in_list.append(dis.disciplineId)

        for i in range(10):
            self.add_grade(Grade(random.randint(1, 200), random.choice(dis_id_already_in_list), 
            random.choice(stud_id_already_in_list), random.randint(1,10)))
