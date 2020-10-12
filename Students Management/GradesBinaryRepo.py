from GradeRepoClass import *
from GradeClass import Grade
import pickle
import os

class GradeBinaryRepository(GradeRepo):
    def __init__(self, studentRepo, disciplineRepo, fileName):
        GradeRepo.__init__(self, studentRepo, disciplineRepo)
        self._fileName = fileName
        self._loadFile()

    def add_grade(self, obj):
        self._grades = []
        self._loadFile()
        GradeRepo.add_grade(self, obj)
        self._saveFile()
    def remove_grade(self, grade_id):
        self._grades = []
        self._loadFile()
        removed_grade = GradeRepo.remove_grade(self, grade_id)
        self._saveFile()
        return removed_grade
        
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

        for grade in GradeRepo.getAll(self):
            pickle.dump(grade,f)

        f.close()

    def _loadFile(self):
        
        filepath = self._fileName
        f = open(filepath, "rb")

        if os.path.getsize(filepath) > 0: 
            with open(filepath,"rb") as f:
                while True:
                    try:
                        obj = pickle.load(f)
                        GradeRepo.add_grade(self,obj)
                    except EOFError:
                        break

        f.close()