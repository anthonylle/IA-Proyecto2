from BoardPrinter.BoardPrinter import BoardPrinter
from Connect4View.Connect4View import Connect4View
from WinAndBlock.WinAndBlock import Checker
from Player.Player import Player
from Board.Board import Board
from MiniMax.MiniMax import MiniMax

class Connect4():
    
    def __init__(self,system):
        self.board =  None
        self.system = system
        self.board_printer = None
        self.view = Connect4View(system)
        self.checker = Checker()

    def default(self):
        self.board =  Board(6,7)
        self.board.create()
        self.board_printer = BoardPrinter(self.system,"bringht", "", "white")
        self.board_printer.load_boar(self.board.column_size)        
        
    def new_game_menu(self):
        option = ""
        while option != "3":
            option = self.view.view_new_game_menu()
            if option == "1":
                self.type_game_menu()
            
            elif option == "2":
                self.start_game()
                
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
                
           
    def start_game(self):
        players = []
        play_again = "y"
        self.view.clear_console()
        P1name = self.view.input_option("Enter Player1's name: ")
        players.append(Player('1', P1name))
        P2name = self.view.input_option("Enter Player2's name: ")
        players.append(Player('2', P2name))
        
        while play_again != "n":
            
            self.default()
            self.play(players)
            play_again =  self.view.input_option(">>>> Do you want to play again?[y/n]: ")
        
    
    def play(self, players):
        actual = 0
        self.view.view_title()
        self.board_printer.print_board(self.board)
        
        _input = self.request_column(players, actual)
        while( _input  != -1):
            self.view.view_title()

            if self.board.insert_value(_input, players[Actual].character):
                self.boar_printer.print_board(self.board)
                if self.checker.check_win(self.board, _input-1, players[Actual].character):
                    if Actual:
                       self.view.player2_wins("bright", "", "cyan")
                    else:
                        self.view.player1_wins("bright", "", "cyan")
                    print("{} is the winner".format(players[Actual].name))
                    break
                Actual = self.change_turn(Actual)
                if Actual == 1:
                    mm = MiniMax(1,'2','1')
                    mm.minimax_search(self.board, [0,1,2,3,4,5,6])

            else:
                self.board_printer.print_board(self.board)
                self.view.alert("invalid move ! D:")
            _input = self.request_column(players, actual)

    def show_winner(self, players, actual):
        if actual:
            self.view.player2_wins("bright", "", "cyan")
        else:
            self.view.player1_wins("bright", "", "cyan")
        players[actual].add_win()
        players[not actual].add_lose()
        print("{} is the winner".format(players[actual].name))
        players[actual].print_record()
        players[not actual].print_record()

    def request_column(self, players, actual):
        _input = -2
        try:
            _input = int(self.view.input_option(">>>> {} select a column's number: ".format(players[actual].name)))
        except ValueError:
            _input = -2
            self.view.alert("invalid move ! D:")
        return _input

    def change_turn(self, Actual):
        return not(Actual)
            
           