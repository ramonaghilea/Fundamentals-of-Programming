from StudentRepoClass import *
from StudentClass import Student

class StudentTextRepository(StudentRepo):
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
        f = open(filepath, 'w')

        line = ""
        for stud in StudentRepo.getAll(self):
            line = ""
            line += str(stud.studentId) + "," + str(stud.studentName) + "\n"
            f.write(line)

        f.close()

    def _loadFile(self):
        
        filepath = self._fileName

        try:
            f = open(filepath, "r")
            line = f.readline().strip()
            while  len(line) > 0:
                line = line.split(",")
                StudentRepo.add_student(self,Student(int(line[0]), line[1]))
                line = f.readline().strip()
            f.close()
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers 
            """
            print("An error occured - " + str(e))
            raise e