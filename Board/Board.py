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
            
    def getAt(self, row, col):
        return self.matrix[row][col]

    def get_highest_disc(self, col, player_value):
        position = -1
        for i in range(self.row_size-1, -1, -1):
            if self.getAt(i, col) == player_value:
                position = i
            elif self.getAt(i, col) == " ":
                break
        return position
    
    def get_lowest_disc(self, col, player_value):
        position = -1
        for i in range(self.row_size-1, -1, -1):
            if self.getAt(i, col) == player_value:
                position = i
                break
        return position
    
    def get_diagonal_border(self, row, col):
        while col != 0 and row != 0:
            col -=1
            row -=1
        return row, col
    
    def get_transposed(self):
        transposed_matrix = Board(self.row_size, self.column_size)
        transposed_matrix.create()
        for i in range(self.row_size-1, -1, -1):
            del transposed_matrix.matrix[0]
            transposed_matrix.matrix.append(self.matrix[i])
        return transposed_matrix

    def setAt(self, row, col, value):
        if (col >= 0 and col < self.column_size):
            self.matrix[row][col] = value
            return True
        return False
