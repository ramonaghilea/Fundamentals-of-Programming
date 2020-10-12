from copy import deepcopy
from ExceptionsClass import UndoException

class UndoController:
    def __init__(self):
        # History of the program's undoable operations
        self._history = []
        # Keep the position in the undo/redo list
        self._index = 0
        # true if we are during an undo/redo operation
        self._duringUndo = False
        self._lastOpUndo = True

    @property
    def duringundo(self):
        return self._duringUndo

    @property
    def lastopundo(self):
        return self._lastOpUndo
        
    def recordOperation(self, operation):
        '''
        Record an operation in the history for undo/redo
        params:
             operation - the operation that was carried out
        '''
        if self._duringUndo == True:
            return

        self._history.append(operation)
        self._index += 1

        self._lastOpUndo = False #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    '''
    UndoController.undo() calls CascadedOperation.undo() which calls Operation.undo() for each
    Operation which calls undoFunction.call() which calls:
        - clientController.delete
        - carController.create
        ...
    '''

    def undo(self):
        if self._index == 0:
            raise ValueError("No more undos!")

        self._duringUndo = True
        self._index -= 1
        self._history[self._index].undo()
        self._duringUndo = False
        self._lastOpUndo = True   #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def redo(self):

        if self._lastOpUndo == False:
            raise UndoException("Cannot perform a redo without a previous undo")

        if self._index == len(self._history):
            raise ValueError("No more redos!")
        self._duringUndo = True
        self._history[self._index].redo()
        self._index += 1
        self._duringUndo = False

    def history_list(self):
        return deepcopy(self._history)

# 1. Keep e reference to a function and its params
# we use the command design pattern
# either undo or redo (a simple one, not cascaded)

class FunctionCall:
    def __init__(self, function, *parameters):
        # use * because we don not know how many params we will have, it memorizes one ore more params
        # parameters = tuple
        self._function = function
        self._params = parameters

    def __call__(self):
        self.call()

    def call(self):
        self._function(*self._params)

class Operation:
    '''
    Store the function reference and params for both undo and redo
    '''
    def __init__(self, undoFunction, redoFunction):
        self._undo = undoFunction
        self._redo = redoFunction

    def undo(self):
        self._undo() # self._undo.call()

    def redo(self):
        self._redo()


class CascadedOperation:
    def __init__(self, *operations):
        self._oper = operations
        self._oper = list(self._oper) #!!!!!!!!!!!!!!!!

    def undo(self):
        for o in self._oper:
            o.undo()

    def redo(self):
        for o in self._oper:
            o.redo()

    def add(self, o):
        self._oper.append(o) #!!!!!!!!!!!!!!!!!!!!!!!