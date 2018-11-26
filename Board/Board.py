
class Board():
    def __init__(self, row_size, column_size):
        self.row_size = row_size
        self.column_size = column_size
        self.matrix = None
        self.last_column = -1
        self.last_row = -1
        self.moves_count = 0
      
    def copy(self):
        """
            Creates a copy of the actual board
        """
        copy = Board( self.row_size,self.column_size)
        copy.matrix = [x[:] for x in self.matrix]
        copy.last_column = self.last_column
        copy.last_row = self.last_row
        copy.moves_count = self.moves_count
        return copy
        
    def create(self):
        """
            Creates the board from the column size and row size provided
        """
        self.matrix = list()
        for i in range(self.row_size):
            self.matrix.append([" "]*self.column_size)

    def insert_value(self, column_number, value):
        """
            insets the provided value in the column number provided
            it pusts the value in the las empty space avaiable in the col
        """
        if (column_number >= 1 and column_number <= self.column_size):
            return self.insert_aux(column_number-1, value)
        else:
            return False
        
    def insert_aux(self, column_number, value):
        """
            Auxiliar function to insert it looks the column row until it finds 
            the last one empty
        """
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

    def is_column_full(self, column_number):
        """
            Returns true if the column's first row is empty 
        """
        row = self.row_size-1
        
        while(row >= 0 ):
            if self.matrix[row][column_number] == " ":
                return False
            row -= 1
        return True
    
    def have_legal_move(self):
        """
            Checks if moves_count have reach the maximun number allow
        """
        return self.moves_count < self.column_size * self.row_size
            
    def getAt(self, row, col):
        """
            Returns the value in the row,col position
        """
        return self.matrix[row][col]

    def get_highest_disc(self, col, player_value):
        """
            returns the row value where it finds the first apereance of the 
            player value
        """
        position = -1
        for i in range(self.row_size-1, -1, -1):
            if self.getAt(i, col) == player_value:
                position = i
            elif self.getAt(i, col) == " ":
                break
        return position
    
    def get_lowest_disc(self, col, player_value):
        """
            return the row value where it finds the first apereance of the 
            player value, from button to top, mainly used by transposed board
        """
        position = -1
        for i in range(self.row_size-1, -1, -1):
            if self.getAt(i, col) == player_value:
                position = i
                break
        return position
    
    def get_diagonal_border(self, row, col):
        """
            Returns the fist diagonal position
        """
        while col != 0 and row != 0:
            col -=1
            row -=1
        return row, col
    
    def get_transposed(self):
        """
        returns a copy of the board inverted
        """
        transposed_matrix = Board(self.row_size, self.column_size)
        transposed_matrix.create()
        for i in range(self.row_size-1, -1, -1):
            del transposed_matrix.matrix[0]
            transposed_matrix.matrix.append(self.matrix[i])
        return transposed_matrix

    def setAt(self, row, col, value):
        """
            Sets the a value of the row and col given
        """
        if (col >= 0 and col < self.column_size):
            self.matrix[row][col] = value
            return True
        return False
    
    def print_matrix(self):
        """
            Prints the matrix to have a perspective of it's actual state
        """
        for row in self.matrix:
            print(row)
        print("________________________________")
            
