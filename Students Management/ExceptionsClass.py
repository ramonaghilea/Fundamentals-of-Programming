class IntException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
class NoneException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
class DuplicateIdException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
class GradeException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
class NegativeException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
class NonexistentException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
class UndoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)