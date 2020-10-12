from DisciplineClass import Discipline
from copy import deepcopy
from ExceptionsClass import *
import random

class DisciplineRepo:
    '''
    Manage the list of disciplines in the program
    Holds a private list of Discipline obj
    Functions to manage the list:
        - add a new Discipline (raise exception if duplicate ID)
        - delete a discipline
        - update a discipline
        - get discipline by id
        - return the list of disciplines
    '''
    def __init__(self):
        self._disciplines = []

    def add_discipline(self, dis):
        '''
        It ads a new Discipline to the list of disciplines.
        It validates the params:
        - checks if dis_id is None, negative or duplicate
        - checks if dis_id is None
        - raises Errors if these happen

        Otherwise, it creates a new Discipline object and adds it to the list.
        '''

        for discipline in self._disciplines:
            if discipline.disciplineId == dis.disciplineId:
                raise DuplicateIdException("Duplicate Id")

        self._disciplines.append(dis)
    
    def remove_discipline(self, DisciplineId):
        '''
        It removes a Discipline from the list of disciplines.
        It validates the params:
        - checks if DisciplineId is None, negative or nonexistent in the list
        - raises Errors if these happen

        Otherwise, it creates a new list, appends all the disciplines, except for the one meant to be removed.
        '''
        new_list = []
        try:
            DisciplineId = int(DisciplineId)
        except ValueError:"Not int"
        if DisciplineId == None:
            raise NoneException("Id is none")
        if DisciplineId < 0:
            raise NegativeException("Id is negative")
        ok = False
        for dis in self._disciplines:
            if dis.disciplineId == DisciplineId:
                ok = True  
        if ok == False:
            raise NonexistentException("Nonexistent Id")

        dis = self.getDisciplineById(DisciplineId)
        self._disciplines.remove(dis)

        return dis
    
    def update_discipline(self, new_dis):
        '''
        It updates a Discipline in the list of disciplines.
        It validates the params:
        - checks if DisciplineId is None, negative or nonexistent in the list
        - checks if newDisciplineId is duplicate
        - checks if newDisciplineName is None
        - raises Errors if these happen

        Otherwise, it updates a Discipline object.
        '''

        dis = self.getDisciplineById(new_dis.disciplineId)
        if dis == None:
            raise NoneException("Element not found!")
        idx = self._disciplines.index(dis)
        self._disciplines.remove(dis)
        self._disciplines.insert(idx, new_dis)

    def getDisciplineById(self, DisciplineId): #returns a Discipline object by its Id
        for dis in self._disciplines:
            if dis.disciplineId == int(DisciplineId):
                return dis

    def getAll(self): #returns a copy of the list of disciplines
        return deepcopy(self._disciplines)

    def __len__(self):
        return len(self._disciplines)

    def __str__(self):
        r = ""
        for e in self._disciplines:
            r += str(e)
            r += "\n"
        return r

    def init_disciplines(self):
        list_of_disciplines = ["Computer Science", "Chemestry", "Biology", "Physics", "Astronomy", 
        "English", "German", "French", "Art", "Sport", "Logic Design", "ASC", "Algebra", "Geometry", "Analysis", 
        "Geography", "History", "Spanish", "Latin", "Debate", "Journalism", "Music", "Political Sciences", 
        "Social Sciences", "Philosophy", "Psychology", "Critical Thinking", "Culinary Arts"]

        list_of_teachers = ["Anemona Frich", "Alexandra Holland", "Camelia Shepherd", "Matilda Fin", "Corina Uhl", 
        "George Mal", "Mariana Hill"]

        dis_id_already_in_list = []
        dis_name_already_in_list = []
        
        for i in range(10):
            dis_id = random.randint(1,200)
            while dis_id in dis_id_already_in_list:
                dis_id = random.randint(1,200)
            dis_name = random.choice(list_of_disciplines)
            while dis_name in dis_name_already_in_list:
                dis_name = random.choice(list_of_disciplines)

            teacher_name = random.choice(list_of_teachers)

            self.add_discipline(Discipline(dis_id, dis_name, teacher_name))

            dis_id_already_in_list.append(dis_id)
            dis_name_already_in_list.append(dis_name)
