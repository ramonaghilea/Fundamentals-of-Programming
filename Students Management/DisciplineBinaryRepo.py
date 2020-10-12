from DisciplineRepoClass import *
from DisciplineClass import Discipline
import pickle
import os

class DisciplineBinaryRepository(DisciplineRepo):
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
        f = open(filepath, 'wb')

        
        for dis in DisciplineRepo.getAll(self):
            pickle.dump(dis,f)

        f.close()

    def _loadFile(self):
        
        filepath = self._fileName
        f = open(filepath, "rb")

        if os.path.getsize(filepath) > 0: 
            with open(filepath,"rb") as f:
                while True:
                    try:
                        obj = pickle.load(f)
                        DisciplineRepo.add_discipline(self,obj)
                    except EOFError:
                        break

        f.close()