import os
class Board():
    def __init__(self, row_size, column_size):
        self.row_size = row_size
        self.column_size = column_size
        self.matrix = list()
        
        
    def create(self):
        for i in range(self.row_size):
            self.matrix.append([" "]*self.column_size)
        
        #no insertar crear de esta forma --> self.matrix = [[" "]*self.column_size]*self.row_size

    def  insert_value(self, column_number, value):
        if (column_number >= 1 and column_number <= self.column_size):
            return self.insert_aux(column_number-1, value)
        else:
            return False
        
    def insert_aux(self, column_number, value):
        
        row = self.row_size-1
        
        while(row >= 0 ):
            if self.matrix[row][column_number] == " ":
                self.matrix[row][column_number] = str(value)
                return True
            row -= 1
            
        return False
    
    def print_matrix(self): 
        for i in range(self.row_size):
            print(self.matrix[i])
            
    def getAt(self, i, j):
        return self.matrix[i][j]
        