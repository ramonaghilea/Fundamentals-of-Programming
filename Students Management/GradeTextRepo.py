from GradeClass import Grade
from GradeRepoClass import GradeRepo

class GradeTextRepository(GradeRepo):
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
        f = open(filepath, 'w')

        line = ""
        for grade in GradeRepo.getAll(self):
            line = ""
            line += str(grade.gradeId) + "," + str(grade.disciplineId) + "," + str(grade.studentId) + "," + str(grade.gradeValue) + "\n"
            f.write(line)

        f.close()

    def _loadFile(self):
        
        filepath = self._fileName

        try:
            f = open(filepath, "r")
            line = f.readline().strip()
            while  len(line) > 0:
                line = line.split(",")
                GradeRepo.add_grade(self,Grade(int(line[0]), int(line[1]), int(line[2]), int(line[3])))
                line = f.readline().strip()
            f.close()
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers 
            """
            print("An error occured - " + str(e))
            raise e