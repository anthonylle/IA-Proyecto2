from ConsoleControl.ConsoleControl import ConsoleControl
from Board.Board import Board


class BoardPrinter(ConsoleControl):
    
    #--------------------------------------------------------------------------
    #input : system: a string with the the clear type(cls or clear)
    #        - style: string with the style 
    #        - style: string with the back color
    #        - style: string with the fore color
    #        see the ConsoleControl class
    #function: constructor
    def __init__ (self, system, style, back, fore):
        ConsoleControl.__init__(self, system)
        self.header = str()
        self.divider = str()
        self.footer = str()
        self.style = style
        self.back = back
        self.fore = fore
        self.boardstyle = {185 :'╣', 186 : '║', 187 : '╗', 188 : '╝', 
                           201 :'╔', 202 : '╩', 200 : '╚', 204 : '╠',
                           205 : '═', 206 : '╬'}

    #--------------------------------------------------------------------------
    #input : column_size int value
    #function: create the divider between rows
    #output: none
    def creat_divider(self, column_size):
        """
            function: Creates the divisions (═ + ╬  + ═)*columns+ ╣ = ═╬═╬═╬═╣
            output: None
        """
        self.divider = "  "+self.boardstyle[205]
        string = self.boardstyle[206] +self.boardstyle[205]*3
        self.divider += string*column_size + self.boardstyle[185]  +"\n"
        
    #--------------------------------------------------------------------------
    #input : column_size: int value
    #function: create the footer to the board
    #output: none
    def create_footer(self, column_size):
        """
            function: Creates the footer
            ╚ + (═*3 + ╩)*columns-1 + ═*3 + ╝ = ╚═══╩═══╩═══╩═══╝ 
            output: None 
        """
        self.footer = "   "+ self.boardstyle[200]
        string = self.boardstyle[205]*3 + self.boardstyle[202]
        self.footer += string * (column_size-1) + self.boardstyle[205]*3 + self.boardstyle[188]  +"\n"
     
    def create_header(self,column_size):
        """
            function: Creates the header 
            "  " ═ + (╬ + ═*3)*columns + ╗  =         1   2   3
                                                "  ═╬═══╬═══╬═══╗"
            output: None
        """
        header = "  "
        string = self.boardstyle[206] +self.boardstyle[205]*3
        boundary = "  "+self.boardstyle[205] + string*column_size 
        boundary += self.boardstyle[187]
        for i in range (column_size):
            cell = " "+str(i+1)+"  "
            header += cell
        self.header +=  header +"\n"+ boundary +"\n"

    #--------------------------------------------------------------------------
    #input : column_size: int value
    #function: create all the dividers to use in the board, used the charaters
    #          in boardstyle variable
    #output: none
    def load_boar(self,column_size):
        """
            function: It prepares the divider, footer and headers class to 
            print the board
            output: None
        """
        self.creat_divider(column_size)
        self.create_footer(column_size)
        self.create_header(column_size)

    #--------------------------------------------------------------------------
    #input : board: a Board object 
    #function: read the board and create the board view
    #output: a string with the board view
    def generate_board_string(self, board):
        """
            function: read the board and create the board view
            output: A String with the board view
        """
        #self.font_selector(self.style, self.back, self.fore) 91r 93y 94b 96c
        matrix = '\033[94m'+ self.header
        for i in range (board.row_size):
            row = '\033[94m'+"   "
            for j in range(board.column_size):
                #self.font_selector("bright","","yellow")
                row += self.boardstyle[186]
                if board.getAt(i,j) == '1':
                    row += '\033[91m' + " ●" #color red●
                elif board.getAt(i,j) == '2':
                    row += '\033[93m' + " ●" #color yellow
                else:
                    row += "  "
                row += '\033[94m' + " "
            row += self.boardstyle[186] +"\n"
            if i < board.row_size-1:
                row += self.divider
            matrix += row
        matrix += self.footer
        return matrix    
    
    #--------------------------------------------------------------------------
    #input : board: a Board object 
    #function: print the board view
    #output: none
    def print_board(self, board):
        """
            function: Prints the board view
            output: None
        """
        self.font_selector(self.style,self.back, self.fore)
        print(self.generate_board_string(board))
        self.reset_all()
       