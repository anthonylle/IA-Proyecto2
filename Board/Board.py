
# class to use all logic relate to game's board 
class Board():
    
    #---------------------------------------------------------------------------
    #input: int: row_size and int: column_size 
    def __init__(self, row_size, column_size):
        self.row_size = row_size
        self.column_size = column_size
        self.matrix = None
        self.last_column = -1
        self.last_row = -1
        self.moves_count = 0

    #--------------------------------------------------------------------------
    #input : none
    #function: create a copy of current board
    #output: new board object 
    def copy(self):
        copy = Board( self.row_size,self.column_size)
        copy.matrix = [x[:] for x in self.matrix]
        copy.last_column = self.last_column
        copy.last_row = self.last_row
        copy.moves_count = self.moves_count
        return copy
    
    #--------------------------------------------------------------------------
    #input : none
    #function: create a this matrix a fill its rows
    #output: none
    def create(self):
        self.matrix = list()
        for i in range(self.row_size):
            self.matrix.append([" "]*self.column_size)
        
        #no insertar crear de esta forma --> self.matrix = [[" "]*self.column_size]*self.row_size


    #--------------------------------------------------------------------------
    #input : column_number: int value to insert, value: a char with player character
    #function: verify if column number is into the range 
    #output: a boolean value, true is insert is ok and false if no 
    def  insert_value(self, column_number, value):

        if (column_number >= 1 and column_number <= self.column_size):
            return self.insert_aux(column_number-1, value)
        else:
            return False

    #--------------------------------------------------------------------------
    #input : column_number: int value to insert, value: a char with player character
    #function: insert a new value in the board, and update moves_count and last move
    #output: a boolean value, true is insert is ok and false if no        
    def insert_aux(self, column_number, value):
        
        row = self.row_size-1
        
        while(row >= 0 ):
            if self.matrix[row][column_number] == " ":
                self.matrix[row][column_number] = str(value)
                self.last_column = column_number
                self.last_row = row
                self.moves_count += 1 
                return True
            row -= 1
        return False

<<<<<<< HEAD
    #--------------------------------------------------------------------------
    #input :  column_number: int value to consult
    #function: verify if the i column is full or not
    #output: true if is full or false if it has at least a space 
=======
    def insert_value_IA(self, column_number, value):
        if (column_number >= 1 and column_number <= self.column_size):
            return self.insert_aux_IA(column_number-1, value)
        else:
            return False
        
    def insert_aux_IA(self, column_number, value):
        
        row = self.row_size-1
        
        while(row >= 0 ):
            if self.matrix[row][column_number] == " ":
                self.matrix[row][column_number] = str(value)
                self.last_column = column_number
                self.last_row = row
                return True
            row -= 1
        return False

>>>>>>> develop-Tenorio
    def is_column_full(self, column_number):
        
        row = self.row_size-1
        
        while(row >= 0 ):
            if self.matrix[row][column_number] == " ":
                return False
            row -= 1
        return True
    
    #--------------------------------------------------------------------------
    #input : none
    #function: verify if the board has at least a space
    #output: true if it has a space or false if it has not a space   
    def have_legal_move(self):
        print(self.moves_count)
        return self.moves_count < self.column_size * self.row_size
            
    #--------------------------------------------------------------------------
    #input : row: int value, column: int value
    #function: get a specifict space in the board
    #output: specifict space in the board
    def getAt(self, row, col):
        return self.matrix[row][col]

    #--------------------------------------------------------------------------
    #input : col: int value, player_value: a char with the player's charter
    #function: find the last space in the column
    #output: int value, -1 if the column is empty or other if no 
    def get_highest_disc(self, col, player_value):
        position = -1
        for i in range(self.row_size-1, -1, -1):
            if self.getAt(i, col) == player_value:
                position = i
            elif self.getAt(i, col) == " ":
                break
        return position
    
    #--------------------------------------------------------------------------
    #input : col: int value, player_value: a char with the player's charter
    #function: find the fisrt space in the column
    #output: int value, -1 if the column is empty or other if no 
    def get_lowest_disc(self, col, player_value):
        position = -1
        for i in range(self.row_size-1, -1, -1):
            if self.getAt(i, col) == player_value:
                position = i
                break
        return position
    
    #--------------------------------------------------------------------------
    #input : row: int value, column: int value
    #function: ?
    #output: two int values    
    def get_diagonal_border(self, row, col):
        while col != 0 and row != 0:
            col -=1
            row -=1
        return row, col
    
    #--------------------------------------------------------------------------
    #input : none
    #function: create a transposed boar with this board
    #output:  a Board object 
    def get_transposed(self):
        transposed_matrix = Board(self.row_size, self.column_size)
        transposed_matrix.create()
        for i in range(self.row_size-1, -1, -1):
            del transposed_matrix.matrix[0]
            transposed_matrix.matrix.append(self.matrix[i])
        return transposed_matrix

    #--------------------------------------------------------------------------
    #input : row: int value, column: int value and value: a  char with the player's charter
    #function: set specific spacein the board
    #output: true if all is ok or false if it isn't
    def setAt(self, row, col, value):
        if (col >= 0 and col < self.column_size):
            self.matrix[row][col] = value
            return True
        return False
    
    #--------------------------------------------------------------------------
    #input : none
    #function: print each row in the matrix
    #output: none
    def print_matrix(self):
        for row in self.matrix:
            print(row)
        print("________________________________")
            
