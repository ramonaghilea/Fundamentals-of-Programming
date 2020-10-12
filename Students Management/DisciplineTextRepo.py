from DisciplineRepoClass import *

class DisciplineTextRepository(DisciplineRepo):
    def __init__(self, fileName):
        DisciplineRepo.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add_discipline(self, obj):
        self._disciplines = []
        self._loadFile()
        DisciplineRepo.add_discipline(self, obj)
        self._saveFile()
    def remove_discipline(self, dis_id):
        self._disciplines = []
        self._loadFile()
        removed_dis = DisciplineRepo.remove_discipline(self, dis_id)
        self._saveFile()
        return removed_dis
    def update_discipline(self, new_dis):
        self._disciplines = []
        self._loadFile()
        DisciplineRepo.update_discipline(self, new_dis)
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
        for dis in DisciplineRepo.getAll(self):
            line = ""
            line += str(dis.disciplineId) + "," + str(dis.disciplineName) + "," + str(dis.teacherName) + "\n"
            f.write(line)

        f.close()

    def _loadFile(self):
        
        filepath = self._fileName

        try:
            f = open(filepath, "r")
            line = f.readline().strip()
            while  len(line) > 0:
                line = line.split(",")
                DisciplineRepo.add_discipline(self,Discipline(int(line[0]), line[1], line[2]))
                line = f.readline().strip()
            f.close()
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers 
            """
            print("An error occured - " + str(e))
            raise e