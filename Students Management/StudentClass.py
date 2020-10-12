class Student:
    '''
    A student has an ID (integer), different from the other student IDs and a name.
    '''
    def __init__(self, studentid, studentname):
        self._studentid = studentid
        self._studentname = studentname

    @property
    def studentName(self):
        return self._studentname

    @studentName.setter
    def studentName(self, value):
        self._studentname = value

    @property
    def studentId(self):
        return self._studentid

    @studentId.setter
    def studentId(self, value):
        self._studentid = value

    def __str__(self):
        return ("Id: " + str(self._studentid)+ " Name: " + str(self._studentname))