class Grade:
    '''
    A grade has an discipline ID (integer), different from the other discipline IDs, 
    student ID (integer), different from the other students IDs and a value (integer between 1 and 10).
    '''
    def __init__(self, gradeid, disid, studentid, gradevalue):
        self._gradeid = gradeid
        self._disid = disid
        self._studentid = studentid
        self._gradevalue = gradevalue

    @property
    def disciplineId(self):
        return self._disid

    @disciplineId.setter
    def disciplineId(self, value):
        self._disid = value

    @property
    def studentId(self):
        return self._studentid

    @studentId.setter
    def studentId(self, value):
        self._studentid = value

    @property
    def gradeValue(self):
        return self._gradevalue

    @gradeValue.setter
    def gradeValue(self, value):
        self._gradevalue = value

    @property
    def gradeId(self):
        return self._gradeid

    @gradeId.setter
    def gradeId(self, value):
        self._gradeid = value

    def __str__(self):
        return "GradeId: " + str(self._gradeid) + " DisciplineId: " + str(self._disid)+ " StudentId: " + str(self._studentid) + " GradeValue: " + str(self._gradevalue)