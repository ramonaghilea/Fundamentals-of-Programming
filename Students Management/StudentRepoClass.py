from StudentClass import Student
from copy import deepcopy, copy
from ExceptionsClass import *
import random

class StudentRepo:
    '''
    Manage the list of students in the program
    Holds a private list of Student obj
    Functions to manage the list:
        - add a new Student (raise exception if duplicate ID)
        - delete a student
        - update a student
        - get student by id
        - return the list of students
    '''
    def __init__(self):
        self._students = []

    def getAll(self):
        return deepcopy(self._students) #returns a copy of the list of students

    def getStudentById(self, StudentId): #returns a Student object by its Id
        StudentId = int(StudentId)
        for stud in self._students:
            if stud.studentId == StudentId:
                return stud
        return None

    def add_student(self, stud):
        '''
        It ads a new Student to the list of students.
        It validates the params:
        - checks if stud_id is None, negative or duplicate
        - checks if stud_name is None
        - raises Errors if these happen

        Otherwise, it creates a new Student object and adds it to the list.
        '''

        #for student in self._students:
        #    if student.studentId == stud.studentId:
        #        raise DuplicateIdException("Duplicate Id")

        self._students.append(stud)
    
    def remove_student(self, StudentId):
        '''
        It removes a Student from the list of students.
        It validates the params:
        - checks if StudentId is None, negative or nonexistent in the list
        - raises Errors if these happen

        Otherwise, it creates a new list, appends all the students, except for the one meant to be removed.
        '''
        try:
            StudentId = int(StudentId)
        except ValueError:"Not int"
        if StudentId == None:
            raise NoneException("Id is none")
        if StudentId < 0:
            raise NegativeException("Id is negative")
        ok = False
        for stud in self._students:
            if stud.studentId == StudentId:
                ok = True  
        if ok == False:
            raise NonexistentException("Nonexistent Id")

        stud = self.getStudentById(StudentId)
        self._students.remove(stud)

        return stud
    
    def update_student(self, new_stud):
        '''
        It updates a Student in the list of students.
        It validates the params:
        - checks if StudentId is None, negative or nonexistent in the list
        - checks if newStudentName is None
        - raises Errors if these happen

        Otherwise, it updates a Student object.
        '''
        stud = self.getStudentById(new_stud.studentId)
        if stud == None:
            raise NoneException("Element not found!")
        idx = self._students.index(stud)
        self._students.remove(stud)
        self._students.insert(idx, new_stud)

    def __len__(self):
        return len(self._students)

    def __str__(self):
        r = ""
        for e in self._students:
            r += str(e)
            r += "\n"
        return r

    def init_students(self):
        list_of_students = ["Sara Ohn", "Helen Mill", "Rebeka Schmidt", "Tim More", "Cassie Rolling", "Orlando Beck",
        "Alexandra Dimisov", "Sandra Key", "Meredith Grey", "Dereck Shepherd", "Amelia Shepherd", "Cristina Yang",
        "Alex Karev", "Jackson Avery", "Callie Torres", "Izzie Stevens", "Mark Sloan", "April Kepner", "Andrew DeLuca",
        "Owen Hunt", "Lexie Grey", "Arizona Robbins", "Miranda Bailey", "Jo Wilson", "Maggie Pierce", "Catherine Avery",
        "George O'Malley"]

        stud_id_already_in_list = []
        stud_name_already_in_list = []

        for i in range(10):
            stud_id = random.randint(1,200)
            while stud_id in stud_id_already_in_list:
                stud_id = random.randint(1,200)

            stud_name = random.choice(list_of_students)
            while stud_name in stud_name_already_in_list:
                stud_name = random.choice(list_of_students)

            self.add_student(Student(stud_id, stud_name))

            stud_id_already_in_list.append(stud_id)
            stud_name_already_in_list.append(stud_name)
