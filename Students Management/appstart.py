from UndoControllerClass import UndoController
from StudentServiceClass import StudentService
from DisciplineServiceClass import DisciplineService
from GradeServiceClass import GradeService
from SuperService import SuperService
from StudentRepoClass import StudentRepo
from DisciplineRepoClass import DisciplineRepo
from GradeRepoClass import GradeRepo
from ExceptionsClass import *
from UI import UI


undoController = UndoController()

# loading settings.properties

filepath = "settingstext.properties"

try:
    f = open(filepath, "r")
    line = f.readline().strip() #reading line 1 repository = ...

    line = line.split(" ")
    if line[2] == "inmemory":  #using in-memory repositories
        studentRepo = StudentRepo()
        disciplineRepo = DisciplineRepo()
        gradeRepo = GradeRepo(studentRepo, disciplineRepo)

        studentRepo.init_students()
        disciplineRepo.init_disciplines()
        gradeRepo.init_grades()

    elif line[2] == "text":
        from StudentTextRepo import StudentTextRepository
        from DisciplineTextRepo import DisciplineTextRepository
        from GradeTextRepo import GradeTextRepository

        line = f.readline().strip() #reading line 2 students = ...
        line = line.split(" ")
        studentRepo = StudentTextRepository(line[2])
        
        line = f.readline().strip() #reading line 3 disciplines = ...
        line = line.split(" ")
        disciplineRepo = DisciplineTextRepository(line[2])

        line = f.readline().strip() #reading line 4 grades = ...
        line = line.split(" ")
        gradeRepo = GradeTextRepository(studentRepo, disciplineRepo, line[2])         

    elif line[2] == "binary":
        from StudentBinaryRepo import StudentBinaryRepository
        from DisciplineBinaryRepo import DisciplineBinaryRepository
        from GradesBinaryRepo import GradeBinaryRepository

        line = f.readline().strip() #reading line 2 students = ...
        line = line.split(" ")
        studentRepo = StudentBinaryRepository(line[2])
        studentRepo.init_students()

        line = f.readline().strip() #reading line 3 disciplines = ...
        line = line.split(" ")
        disciplineRepo = DisciplineBinaryRepository(line[2])
        disciplineRepo.init_disciplines()

        line = f.readline().strip() #reading line 4 grades = ...
        line = line.split(" ")
        gradeRepo = GradeBinaryRepository(studentRepo, disciplineRepo, line[2])
        gradeRepo.init_grades()

    f.close()

except IOError as e:
    print(str(e))


gradeService = GradeService(undoController, gradeRepo)

students = StudentService(undoController, studentRepo, gradeService)
disciplines = DisciplineService(undoController, disciplineRepo, gradeService)
grades = GradeService(undoController, gradeRepo)
superService = SuperService(studentRepo, disciplineRepo, gradeRepo)

ui = UI(undoController, students, disciplines, grades, superService)
ui.mainMenu()