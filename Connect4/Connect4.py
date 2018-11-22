from Board.Board import Board
from BoardPrinter.BoardPrinter import BoardPrinter
from Player.Player import Player
from Connect4View.Connect4View import Connect4View

class Connect4():
    
    def __init__(self,system):
        self.board =  Board(6,7)
        self.boar_printer = BoardPrinter(system,"bringht", "", "white")
        self.view = Connect4View(system)
        self.player1 = Player('1', "P1")
        self.player2 = Player('2', "P2")

    def default(self):
        self.board.create()
        self.boar_printer.load_boar(self.board.column_size)
        
    def new_game_menu(self):
        option = ""
        while option != "3":
            option = self.view.view_new_game_menu()
            if option == "1":
                self.type_game_menu()
            
            elif option == "2":
                self.play()
                
            elif option == "3":
                self.view.clear_console()
                
            else:
                self.view.invalid_option()
    
    def type_game_menu(self):
        option = ""
        while option != "4":
            option = self.view.view_type_game_menu()
            if option == "1":
                option = "4"
                print("escogió c vs c")
            
            elif option == "2":
                option = "4"
                print("escogió h vs h")
                
            elif option == "3":
                option = "4"
                print("escogió h vs c")                
                
            elif option == "4":
                self.view.clear_console()
                
            else:
                self.view.invalid_option()
    
    def how_to_play(self):
        self.view.view_how_to_play()
        self.view.clear_console()
    
    def main_menu(self):
        
        option = ""
        while option != "3":
            option = self.view.view_main_menu()
            if option == "1":
                self.new_game_menu()
            
            elif option == "2":
                self.how_to_play()
                
            elif option == "3":
                self.view.clear_console()
                
            else:
                self.view.invalid_option()   
                
    def play(self):
        self.default()
        _input = 4
        while( _input  != -1):
            
            self.view.view_title()
            
            if self.board.insert_value(_input, self.player1.character): 
                self.boar_printer.print_board(self.board)
            else:
                self.boar_printer.print_board(self.board)
                self.view.invalid_option()
            _input = int(self.view.column_option())            