from StudentRepoClass import *
from StudentClass import Student
from ExceptionsClass import *

class StudentTextFileModificationsRepository(StudentRepo):
    def __init__(self, fileName, auxiliaryFileName):
        StudentRepo.__init__(self)
        self._fileName = fileName
        self._auxiliaryFileName = auxiliaryFileName

    def copy_file(self):
        filepath2 = self._fileName
        filepath = self._auxiliaryFileName
        f = open(filepath, "r")
        f2 = open(filepath2, "w")

        line = f.readline().strip()
        while  len(line) > 0:
            f2.write(line)
            line = f.readline().strip()
        f.close()
        f2.close()

    def add_student(self, obj):
        filepath = self._fileName
        filepath2 = self._auxiliaryFileName
        f = open(filepath, "r")
        f2 = open(filepath2, "w")

        line = f.readline().strip()
        while  len(line) > 0:
            line = line.split(",")
            if int(line[0]) == obj.studentId:
                raise DuplicateIdException("Duplicate Id")
            line = ""
            line += str(line[0]) + "," + str(line[1]) + "\n"
            f2.write(line)
            line = f.readline().strip()

        line = ""
        line += str(obj.studentId) + "," + str(obj.studentName) + "\n"
        f2.write(line)

        f.close()
        f2.close()

        #copy the auxiliary file to the main file
        self.copy_file()

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