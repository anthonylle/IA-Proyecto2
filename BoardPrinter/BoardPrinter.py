from ConsoleControl.ConsoleControl import ConsoleControl
from Board.Board import Board

class BoardPrinter(ConsoleControl):
    
    ##
    def __init__ (self, system, style, back, fore):
        
        ConsoleControl.__init__(self, system)
        self.header = str()
        self.divider = str()
        self.footer = str()
        self.style = style
        self.back = back
        self.fore = fore
        self.boardstyle = {185 :'╣', 186 : '║', 187 : '╗', 188 : '╝', 201 : '╔', 
                           202 : '╩', 200 : '╚', 204 : '╠',
                          205 : '═', 206 : '╬'}


    def creat_divider(self, column_size):
        self.divider = "  "+self.boardstyle[205]
        string = self.boardstyle[206] +self.boardstyle[205]*3
        self.divider += string*column_size + self.boardstyle[185]  +"\n"
        

    def create_footer(self, column_size):
        self.footer = "   "+ self.boardstyle[200]
        string = self.boardstyle[205]*3 + self.boardstyle[202]
        self.footer += string * (column_size-1) + self.boardstyle[205]*3 + self.boardstyle[188]  +"\n"
        
        

    def create_header(self,column_size):
        header = "    "
        string = self.boardstyle[206] +self.boardstyle[205]*3
        boundary = "  "+self.boardstyle[205] + string*column_size 
        boundary += self.boardstyle[187]
        for i in range (column_size):
            cell = " "+str(i+1)+"  "
            header += cell
        self.header +=  header +"\n"+ boundary +"\n"

    def load_boar(self,column_size):
        
        self.creat_divider(column_size)
        self.create_footer(column_size)
        self.create_header(column_size)
        

    def print_board(self, board):
        #self.font_selector(self.style, self.back, self.fore) 91r 93y 94b 96c
        matrix = '\033[94m'+ self.header
        for i in range (board.row_size):
            row = '\033[94m'+" "+str(i+1) +" "
            for j in range(board.column_size):
                #self.font_selector("bright","","yellow")
                row += self.boardstyle[186]
                if board.getAt(i,j) == '1':
                    row += '\033[91m' + " ⬤" #color red
                elif board.getAt(i,j) == '2':
                    row += '\033[93m' + " ⬤" #color yellow
                else:
                    row += "  "
                row += '\033[94m' + " "
            row += self.boardstyle[186] +"\n"
            if i < board.row_size-1:
                row += self.divider
            matrix += row
        matrix += self.footer
        self.font_selector(self.style,self.back, self.fore)
        print(matrix)
        self.reset_all()
       