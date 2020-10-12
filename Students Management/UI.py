
from UndoControllerClass import UndoController
from StudentClass import Student
from DisciplineClass import Discipline
from GradeClass import Grade
from StudentRepoClass import StudentRepo
from DisciplineRepoClass import DisciplineRepo
from GradeRepoClass import GradeRepo
from StudentServiceClass import StudentService
from DisciplineServiceClass import DisciplineService
from GradeServiceClass import GradeService
from SuperService import SuperService
from ExceptionsClass import *
from printMessages import printReposWithMessage


class UI:
    def __init__(self, undoController, students, disciplines, grades, superService):
        self._undoController = undoController
        self._students = students
        self._disciplines = disciplines
        self._grades = grades
        self._superService = superService
    
    def init_all(self):
        self._students.init_students()
        self._disciplines.init_disciplines()
        self._grades.init_grades()

    def MainMenu(self):
        s = "Available commands:\n"

        s += "0. Exit\n"
        s += "1. Manage the list of students and available disciplines\n"
        s += "2. Grade student\n"
        s += "3. Search for disciplines/students based on ID or name/title\n"
        s += "4. Create statistics\n"
        s += "5. Undo/Redo\n"

        print(s)
        s=""

    def Menu1(self):
        s = "Available commands:\n"

        s += "0. Exit\n"
        s += "1. Add student/discipline\n"
        s += "2. Remove student/discipline\n"
        s += "3. Update student/discipline\n"
        s += "4. List students/disciplines\n"

        print(s)
        s=""

    def Menu2(self):
        s = "Available commands:\n"
        s += "0. Exit\n"
        s += "1. Grade student\n"

        print(s)
        s=""

    def Menu3(self):
        s = "Available commands:\n"

        s += "0. Exit\n"
        s += "1. Search for disciplines based on ID\n"
        s += "2. Search for disciplines based on name\n"
        s += "3. Search for students based on ID\n"
        s += "4. Search for students based on name\n"

        print(s)
        s=""

    def Menu4(self):
        s = "Available commands:\n"

        s += "0. Exit\n"
        s += "1. All students failing at one or more disciplines (students having an average <5 for a discipline are considered to be failing)\n"
        s += "2. Students with the best school situation, sorted in descending order of their aggregated average (the average between their average grades per discipline)\n"
        s += "3. All disciplines at which there is at least one grade, sorted in descending order of the average grade received by all students enrolled at that discipline\n"
        s += "4. Teachers ordered by the means of grades\n"

        print(s)
        s=""

    def Menu5(self):
        s = "Available commands:\n"

        s += "0. Exit\n"
        s += "1. Undo\n"
        s += "2. Redo\n"

        print(s)
        s = ""

    def subMenu1(self):
        s = "Available commands for add:\n"

        s += "1. Add student\n"
        s += "2. Add discipline\n"
        print(s)
    def subMenu2(self):
        s = "Available commands for remove:\n"

        s += "1. Remove student\n"
        s += "2. Remove discipline\n"
        print(s)
    def subMenu3(self):
        s = "Available commands for update:\n"

        s += "1. update student\n"
        s += "2. Update discipline\n"
        print(s)
    def subMenu4(self):
        s = "Available commands for list:\n"

        s += "1. List students\n"
        s += "2. List disciplines\n"
        print(s)

    def add_student_ui(self):
        stud_id = input("Student ID: ")
        stud_name = input("Student Name: ")

        self._students.add_student(stud_id, stud_name)

    def add_discipline_ui(self):
        dis_id = input("Discipline ID: ")
        dis_name = input("Discipline Name: ")
        teacher_name = input("Teacher: ")

        self._disciplines.add_discipline(dis_id, dis_name, teacher_name)

    def remove_student_ui(self):
        stud_id = int(input("Student ID: "))

        self._students.remove_student(stud_id)

    def remove_discipline_ui(self):
        dis_id = int(input("Discipline ID: "))

        self._disciplines.remove_discipline(dis_id)
        
    def update_student_ui(self):
        stud_id = input("Student ID: ")
        new_stud_name = input("New Student Name: ")

        self._students.update_student(stud_id, new_stud_name)

    def update_discipline_ui(self):
        dis_id = input("Discipline ID: ")
        new_dis_name = input("New Discipline Name: ")
        new_teacher_name = input("New teacher Name: ")
        self._disciplines.update_discipline(dis_id, new_dis_name, new_teacher_name)

    def list_students_ui(self):
        print("Students:\n" + str(self._students))
        print("Grades:\n" + str(self._grades))

    def list_disciplines_ui(self):
        print("Disciplines:\n" + str(self._disciplines))
        print("Grades:\n" + str(self._grades))

    def add_ui(self):
        self.subMenu1()
        commands_add = {"1": self.add_student_ui, "2": self.add_discipline_ui}

        cmd_add = input("Enter command: ")

        if cmd_add not in commands_add:
            print("Bad command")
        else:
            commands_add[cmd_add]()
            
    def remove_ui(self):
        self.subMenu2()
        commands_remove = {"1": self.remove_student_ui, "2": self.remove_discipline_ui}

        cmd_remove = input("Enter command: ")

        if cmd_remove not in commands_remove:
            print("Bad command")
        else:
            try:
                commands_remove[cmd_remove]()
            except Exception as ex:
                print(str(ex))

    def update_ui(self):
        self.subMenu3()
        commands = {"1": self.update_student_ui, "2": self.update_discipline_ui}

        cmd = input("Enter command: ")

        if cmd not in commands:
            print("Bad command")
        else:
            try:
                commands[cmd]()
            except Exception as ex:
                print(str(ex))

    def list_ui(self):
        self.subMenu4()
        commands_list = {"1": self.list_students_ui, "2": self.list_disciplines_ui}

        cmd_list = input("Enter command: ")

        if cmd_list not in commands_list:
            print("Bad command")
        else:
            #try:
            commands_list[cmd_list]()
            #except Exception as ex:
            #    print(str(ex))

    def add_grade_ui(self):
        grade_id = input("Grade ID: ")
        dis_id = input("Discipline ID: ")
        stud_id = input("Student ID: ")
        grade_value = input("Grade Value: ")
        self._grades.add_grade(grade_id, dis_id, stud_id, grade_value)

    def search_disciplines_id_ui(self):
        dis_id = input("Discipline ID: ")
        matches = []
        matches = self._disciplines.search_discipline_id(dis_id)
        if len(matches) == 0:
            print("No matches")
        else:
            for m in matches:
                print(m)

    def search_disciplines_name_ui(self):
        dis_name = input("Discipline Name: ")
        matches = []
        matches = self._disciplines.search_discipline_name(dis_name)
        if len(matches) == 0:
            print("No matches")
        else:
            for m in matches:
                print(m)

    def search_students_id_ui(self):
        stud_id = input("Student ID: ")
        matches = []
        matches = self._students.search_student_id(stud_id)
        if len(matches) == 0:
            print("No matches")
        else:
            for m in matches:
                print(m)

    def search_students_name_ui(self):
        stud_name = input("Student Name: ")
        matches = []
        matches = self._students.search_student_name(stud_name)
        if len(matches) == 0:
            print("No matches")
        else:
            for m in matches:
                print(m)

    def students_failing_ui(self):
        result = self._superService.students_failing()

        for res in result:
            print(res)

    def students_best_situation_ui(self):
        result = self._superService.students_best_situation()

        for res in result:
            print(res)

    def disciplines_with_grades_ui(self):
        result = self._superService.disciplines_with_grades()

        for res in result:
            print(res)

    def teachers_by_average_of_grades_ui(self):
        result = self._superService.teachers_by_average_of_grades()

        for res in result:
            print(res)

    def undo_ui(self):
        self._undoController.undo()
        printReposWithMessage("After Undo: ", self._students, self._disciplines, self._grades)

    def redo_ui(self):
        self._undoController.redo()
        printReposWithMessage("After Redo: ", self._students, self._disciplines, self._grades)

    def functionality1(self):

        commands1 = {"1": self.add_ui, "2": self.remove_ui, "3": self.update_ui, "4": self.list_ui}

        while True:
            self.Menu1()

            cmd = input("Enter command:")

            if cmd == "0":
                return
            if cmd not in commands1:
                print("Bad command")
            else:
                #try:
                commands1[cmd]()
                #except Exception as ex:
                #    print(str(ex))

    def functionality2(self):

        commands2 = {"1": self.add_grade_ui}

        while True:
            self.Menu2()

            cmd = input("Enter command:")

            if cmd == "0":
                return
            if cmd not in commands2:
                print("Bad command")
            else:
                #try:
                commands2[cmd]()
                #except Exception as ex:
                #    print(str(ex)

    def functionality3(self):

        commands3 = {"1": self.search_disciplines_id_ui, "2": self.search_disciplines_name_ui,
        "3": self.search_students_id_ui, "4": self.search_students_name_ui}

        while True:
            self.Menu3()

            cmd = input("Enter command:")

            if cmd == "0":
                return
            if cmd not in commands3:
                print("Bad command")
            else:
                #try:
                commands3[cmd]()
                #except Exception as ex:
                #    print(str(ex)

    def functionality4(self):

        commands4 = {"1": self.students_failing_ui, "2": self.students_best_situation_ui, 
        "3": self.disciplines_with_grades_ui, "4": self.teachers_by_average_of_grades_ui}

        while True:
            self.Menu4()

            cmd = input("Enter command:")

            if cmd == "0":
                return
            if cmd not in commands4:
                print("Bad command")
            else:
                #try:
                commands4[cmd]()
                #except Exception as ex:
                #    print(str(ex)

    def functionality5(self):

        commands5 = {"1": self.undo_ui, "2": self.redo_ui}

        while True:
            self.Menu5()

            cmd = input("Enter command:")

            if cmd == "0":
                return
            if cmd not in commands5:
                print("Bad command")
            else:
                #try:
                commands5[cmd]()
                #except Exception as ex:
                #    print(str(ex)


    def mainMenu(self):

        commands = {"1": self.functionality1, "2": self.functionality2, "3": self.functionality3, 
        "4": self.functionality4, "5": self.functionality5}


        print("-" * 15 + "The initial objects" + "-" * 15)
        print("Students:\n" + str(self._students))
        print("Disciplines\n" + str(self._disciplines))
        print("Grades:\n" + str(self._grades))
        
        while True:
            self.MainMenu()

            cmd = input("Enter command:")

            if cmd == "0":
                return
            if cmd not in commands:
                print("Bad command")
            else:
                try:
                    commands[cmd]()
                except Exception as ex:
                
                    print(str(ex))
