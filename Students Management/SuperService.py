from StudentServiceClass import StudentService
from DisciplineServiceClass import DisciplineService
from GradeServiceClass import GradeService
from GradeClass import Grade
from StudentClass import Student

class SuperService:
    def __init__(self, studentService, disciplineService, gradeService):
        self._studentService = studentService
        self._disciplineService = disciplineService
        self._gradeService = gradeService

    def students_failing(self):
        result = []

        for stud in self._studentService.getAll():
            studDict = {}
            for dis in self._disciplineService.getAll():
                studDict[dis.disciplineId] = 0

            for grade in self._gradeService.getAll():
                if grade.studentId == stud.studentId:
                    if not(studDict[grade.disciplineId] == 0):
                        studDict[grade.disciplineId] = (studDict[grade.disciplineId] + grade.gradeValue)/2
                    else:
                        studDict[grade.disciplineId] = grade.gradeValue
            fail = False
            #for clientId, daysRented in statsDict.items():
            #result.append(ClientStatistics(clientId, daysRented))
            for j in studDict.keys():
                if studDict[j] < 5 and not (studDict[j] == 0):
                    fail = True

            if fail == True:
                result.append(Student(stud.studentId, stud.studentName))
            
        return result

    def students_best_situation(self):
        result = []

        for stud in self._studentService.getAll():
            studDict = {}
            for dis in self._disciplineService.getAll():
                studDict[dis.disciplineId] = 0

            for grade in self._gradeService.getAll():
                if grade.studentId == stud.studentId:
                    if not(studDict[grade.disciplineId] == 0):
                        studDict[grade.disciplineId] = (studDict[grade.disciplineId] + grade.gradeValue)/2
                    else:
                        studDict[grade.disciplineId] = grade.gradeValue

            total_average = 0
            for dis in studDict.keys():
                if not (studDict[dis] == 0):
                    if total_average == 0:
                        total_average = studDict[dis]
                    else:
                        total_average = (total_average + studDict[dis])/2

            result.append([stud.studentId, total_average])

        def sortSecond(val): 
            return val[1]

        result.sort(key = sortSecond, reverse = True)

        result2 = []
        for res in range(len(result)):
            result2.append(self._studentService.getStudentById(result[res][0]))
        
        return result2

    def disciplines_with_grades(self):
        result = []
        for dis in self._disciplineService.getAll():
            
            dis_average = 0
            for grade in self._gradeService.getAll():
                if grade.disciplineId == dis.disciplineId:
                    if not(dis_average == 0):
                        dis_average = (dis_average + grade.gradeValue)/2
                    else:
                        dis_average = grade.gradeValue

            result.append([dis.disciplineId, dis_average])

        def sortSecond(val): 
            return val[1]

        result.sort(key = sortSecond, reverse = True)

        result2 = []
        for res in range(len(result)):
            result2.append(self._disciplineService.getDisciplineById(result[res][0]))

        return result2

    def teachers_by_average_of_grades(self):
        result = {}
        for dis in self._disciplineService.getAll():
            result[dis.teacherName] = 0
            
        for grade in self._gradeService.getAll():
            discipline = self._disciplineService.getDisciplineById(grade.disciplineId)
            if result[discipline.teacherName] == 0:
                result[discipline.teacherName] = grade.gradeValue
            else:
                result[discipline.teacherName] = (result[discipline.teacherName] + grade.gradeValue)/2
        
        result2 = []
        for k in result.keys():
            result2.append([k, result[k]])

        def sortSecond(val): 
                return val[1]

        result2.sort(key = sortSecond, reverse = True)

        return result2






