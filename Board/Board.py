
# class to use all logic relate to game's board 
class Board():
    
    """input: int: row_size and int: column_size"""
    
    #---------------------------------------------------------------------------
    
    def __init__(self, row_size, column_size):
        self.row_size = row_size
        self.column_size = column_size
        self.matrix = None
        self.last_column = -1
        self.last_row = -1
        self.moves_count = 0

    #--------------------------------------------------------------------------

    def copy(self):
        """
            input : none
            function: Creates a copy of the actual board
            output: new board object 
        """        
        copy = Board( self.row_size,self.column_size)
        copy.matrix = [x[:] for x in self.matrix]
        copy.last_column = self.last_column
        copy.last_row = self.last_row
        copy.moves_count = self.moves_count
        return copy
    
    #--------------------------------------------------------------------------

    def create(self):
        """
            input : none
            function: create a this matrix a fill its rows
            output: none
        """
        
        self.matrix = list()
        for i in range(self.row_size):
            self.matrix.append([" "]*self.column_size)
    
    #--------------------------------------------------------------------------

    def  insert_value(self, column_number, value):
        """
            input : column_number: int value to insert, value: a char with player 
            character
            function: verify if column number is into the range 
            output: a boolean value, true is insert is ok and false if no     
        """
        if (column_number >= 1 and column_number <= self.column_size):
            return self.insert_aux(column_number-1, value)
        else:
            return False

    #--------------------------------------------------------------------------
     
    def insert_aux(self, column_number, value):
        """
            input : column_number: int value to insert, value: a char with player 
            character
            function: insert a new value in the board, and update 
            moves_count and last move
            output: a boolean value, true is insert is ok and false if no   
        """        
        row = self.row_size-1
        
        while(row >= 0 ):
            if self.matrix[row][column_number] == " ":
                self.setAt(row, column_number, str(value))
                self.last_column = column_number
                self.last_row = row
                self.moves_count += 1 
                return True
            row -= 1
        return False
    
    #--------------------------------------------------------------------------

    def is_column_full(self, column_number):
        """
            input :  column_number: int value to consult
            function: verify if the i column is full or not
            output: true if is full or false if it has at least a space
        """
        row = self.row_size-1
        
        while(row >= 0 ):
            if self.matrix[row][column_number] == " ":
                return False
            row -= 1
        return True    
    
    #--------------------------------------------------------------------------
  
    def have_legal_move(self):
        """
            input : none
            function: Checks if moves_count have reach the maximun number
            allow
            output: true if it has a space or false if it has not a space 
        """
        return self.moves_count < self.column_size * self.row_size

    # -------------------------------------------------------------------------
    
    def is_legal_area(self, area):
        """
        input: a list with specific index area
        function: review if an area is legal
        output: true or false
        """
        if area != []:
            for col in area:
                if not(self.is_column_full(col)):
                    return True
        return False
        
    #--------------------------------------------------------------------------

    def getAt(self, row, col):
        """
            input : row: int value, column: int value
            function: Returns the value in the row,col position
            output: specifict space in the board    
        """
        if row >= 0 and row < self.row_size and col >= 0 and  col < self.column_size:
            return self.matrix[row][col]
        
        return '-'

    #--------------------------------------------------------------------------

    def get_highest_disc(self, col, player_value):
        """
            input : col: int value, player_value: a char with the player's 
            charter
            function: returns the row value where it finds the first apereance
            of the player value
            output: int value, -1 if the column is empty or other if not
        """
        position = -1
        for i in range(self.row_size-1, -1, -1):
            if self.getAt(i, col) == player_value:
                position = i
            elif self.getAt(i, col) == " ":
                break
        return position
    
    #--------------------------------------------------------------------------

    def get_lowest_disc(self, col, player_value):
        """
            input : col: int value, player_value: a char with the player's 
            charter
            function: Return the row value where it finds the first apereance
            of the player value, from button to top, mainly used by transposed
            board
            output: int value, -1 if the column is empty or other if not
        """
        position = -1
        for i in range(self.row_size-1, -1, -1):
            if self.getAt(i, col) == player_value:
                position = i
                break
        return position
    
    #--------------------------------------------------------------------------

    def get_diagonal_border(self, row, col):
        """
            input : row: int value, column: int value
            function: Returns the fist diagonal position
            output: two int values    
        """
        while col != 0 and row != 0:
            col -=1
            row -=1
        return row, col
    
    #--------------------------------------------------------------------------

    def get_transposed(self):
        """
            input : none
            function: Creates a copy of the board and invertes it
            output:  a Board object 
        """
        transposed_matrix = Board(self.row_size, self.column_size)
        transposed_matrix.create()
        for i in range(self.row_size-1, -1, -1):
            del transposed_matrix.matrix[0]
            transposed_matrix.matrix.append(self.matrix[i])
        return transposed_matrix

    #--------------------------------------------------------------------------

    def setAt(self, row, col, value):
        """
            input : row: int value, column: int value and value: a  char with 
            the player's charter
            function: Sets the a value of the row and col given
            output: true if all is ok or false if it isn't
        """
        if (col >= 0 and col < self.column_size) and ( row >=0 and row < self.row_size):
            self.matrix[row][col] = value
            return True
        return False
    
    #--------------------------------------------------------------------------
    def get_column_with_space(self,area):
        """
        input: area with index to search
        funtion: search a column in the board with a space empty
        output: index column
        """
        for col in area:
            if not(self.is_column_full(col)) :
                return col
        return -2
    
    
    #--------------------------------------------------------------------------
    def get_set_space(self):
        """
        input: none
        funtion: get a set from 0 to column_size
        output: set object
        """
        return set(list(range(self.column_size)))
    
    #--------------------------------------------------------------------------
    def print_matrix(self):
        """
        input : none
        function: Prints the matrix to have a perspective of it's actual state
        output: None
        """
        m = ""
        for row in self.matrix:
            m += str(row)+"\n"
        print(m)
            
