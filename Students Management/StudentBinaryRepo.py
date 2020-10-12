from StudentRepoClass import *
from StudentClass import Student
import pickle
import os

class StudentBinaryRepository(StudentRepo):
    def __init__(self, fileName):
        StudentRepo.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add_student(self, obj):
        self._students = []
        self._loadFile()
        StudentRepo.add_student(self, obj)
        self._saveFile()
    def remove_student(self, stud_id):
        self._students = []
        self._loadFile()
        removed_stud = StudentRepo.remove_student(self, stud_id)
        self._saveFile()
        return removed_stud
    def update_student(self, new_stud):
        self._students = []
        self._loadFile()
        StudentRepo.update_student(self, new_stud)
        self._saveFile()
        
    def _saveFile(self):
        '''
        1. Open text file for writing 'w'
        2. for each car in the repository:
            a. transform it into one-line string
            b. write it to the file
        3. close file
        '''
        filepath = self._fileName
        f = open(filepath, 'wb')

        objects = []
        for stud in StudentRepo.getAll(self):
            pickle.dump(stud,f)

        f.close()

    def _loadFile(self):
        
        filepath = self._fileName
        f = open(filepath, "rb")

        if os.path.getsize(filepath) > 0: 
            with open(filepath,"rb") as f:
                while True:
                    try:
                        obj = pickle.load(f)
                        StudentRepo.add_student(self,obj)
                        
                    except EOFError:
                        break

        f.close()