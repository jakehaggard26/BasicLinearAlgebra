from DataStructures.Vector import Vector
import numpy as np

class Matrix:

    def __init__(self, rows=0, columns=0):

        self.__rows = rows
        self.__columns = columns

        self.__matrix = None

        if rows > 0 and columns > 0:
            self.__matrix = []

            for c in columns:
                self.__matrix.append(Vector())

        elif rows == 0 and columns > 0:
            raise Exception("Need at least 1 row.")
        
        elif rows > 0 and columns == 0:
            raise Exception("Need at least 1 column.")
        
        elif rows == 0 and columns == 0:
            self.__matrix = None
        
        else:
            # Not sure how this would happen
            raise RuntimeError("ERROR: Not sure how this branch was reached. Terminating program.\nControl Flow can be found in `__init__()` in Matrix.py")
            
        return   
    

    def __str__(self) -> str:

        string = 'Matrix Dimensions\n' \
        '--------------------------------------\n' \
        f'Rows: {self.rows} & Columns: {self.columns}\n' \
        'Matrix: \n'

        if self.rows >= 1:
            for i in range(self.rows):
                string += str(self.matrix[i]) + '\n'
        else:
            string = 'Matrix is empty'

        return string
    
    @property
    def matrix(self) -> list[np.array]:
        return self.__matrix
    
    @matrix.setter
    def matrix(self, value: list[np.array]):
        self.__matrix = value
        self.rows = len(value)
        self.columns = len(value[0])

    @property
    def rows(self):
        return self.__rows

    @rows.setter
    def rows(self, value):
        self.__rows = value

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        self.__columns = value
