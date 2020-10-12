class Discipline:
    '''
    A dicipline has an ID (integer), different from the other discipline IDs and a name.
    '''
    def __init__(self, disid, disname, teachername):
        self._disid = disid
        self._disname = disname
        self._teachername = teachername

    @property
    def disciplineName(self):
        return self._disname

    @disciplineName.setter
    def disciplineName(self, value):
        self._disname = value

    @property
    def disciplineId(self):
        return self._disid

    @disciplineId.setter
    def disciplineId(self, value):
        self._disid = value

    @property
    def teacherName(self):
        return self._teachername

    @teacherName.setter
    def teacherName(self, value):
        self._teachername = value

    def __str__(self):
        return "Id: " + str(self._disid)+ " Name: " + str(self._disname) + " TeacherName: " + str(self._teachername)