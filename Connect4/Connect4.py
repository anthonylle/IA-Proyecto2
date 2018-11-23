from BoardPrinter.BoardPrinter import BoardPrinter
from Connect4View.Connect4View import Connect4View
from Player.Player import Player
from Board.Board import Board
from WinAndBlock.WinAndBlock import Win_Checker, Block_Checker

class Connect4():
    
    def __init__(self,system):
        self.board =  None
        self.system = system
        self.boar_printer = None
        self.view = Connect4View(system)
        

    def default(self):
        self.board =  Board(6,7)
        self.board.create()
        self.boar_printer = BoardPrinter(self.system,"bringht", "", "white")
        self.boar_printer.load_boar(self.board.column_size)        
        
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
        Actual = 0
        self.view.view_title()
        self.boar_printer.print_board(self.board)
        win_checker = Win_Checker()
        block_checker = Block_Checker()
        try:
            _input = int(self.view.input_option(">>>> {} select a column's number: ".format(players[Actual].name)))
        except ValueError:
            _input = -2
            self.view.alert("invalid move ! D:")
        while( _input  != -1):
            self.view.view_title()
            

            if self.board.insert_value(_input, players[Actual].character):
                self.boar_printer.print_board(self.board)
                if self.check_win(self.board, _input-1, players[Actual].character):
                    if Actual:
                       self.view.player2_wins("bright", "", "cyan")
                    else:
                        self.view.player1_wins("bright", "", "cyan")
                    print("{} is the winner".format(players[Actual].name))
                    break
                Actual = self.change_turn(Actual)
                win = win_checker.check(self, self.board, players, Actual)
                block = block_checker.check(self, self.board, players, Actual)
                if win != -1:
                    _input = win
                    continue
                elif block != -1:
                    _input = block
                    continue
            else:
                self.boar_printer.print_board(self.board)
                self.view.alert("invalid move ! D:")
            try:
                _input = int(self.view.input_option(">>>> {} select a column's number: ".format(players[Actual].name)))
            except ValueError:
                _input = -2
                self.view.alert("invalid move ! D:")

    def change_turn(self, Actual):
        return not(Actual)
            
    def check_win(self, board, col, player_value):
        return self.check_verticals(board, col, player_value
                ) or self.check_horizontals(board, col, player_value
                ) or self.check_diagonals(board, col, player_value)

    def check_verticals(self, board, col, player_value):
        four_in_a_row = False
        highest_disc_row = board.get_highest_disc(col, player_value)
        if (highest_disc_row <= 2):
            for i in range(highest_disc_row, highest_disc_row+4):
                if board.getAt(i, col) != player_value:
                    break
                elif i == highest_disc_row+3:
                    four_in_a_row = True
        return four_in_a_row
    
    def check_horizontals(self, board, col, player_value):
        discs = 1 #Actual
        highest_disc_row = board.get_highest_disc(col, player_value)
        discs += self._check_horizontals(board, col+1, highest_disc_row, player_value, True)
        discs += self._check_horizontals(board, col-1, highest_disc_row, player_value, False)
        return discs >= 4
    
    def _check_horizontals(self, board, col, row, player_value, look_right):
        if col >= 0 and col <= board.column_size-1:
            if look_right:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_horizontals(board, col+1, row, player_value, look_right)
            else:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_horizontals(board, col-1, row, player_value, look_right)
        return 0

    def check_diagonals(self, board, col, player_value):
        discs = 1  #Actual
        discsT = 1 #Actual
        transposed = board.get_transposed()
        highest_disc_row = board.get_highest_disc(col, player_value)
        lowest_disc_row_t = transposed.get_lowest_disc(col, player_value)
        discs  += self._check_diagonals(board, col-1, highest_disc_row-1, player_value, True)
        discs  += self._check_diagonals(board, col+1, highest_disc_row+1, player_value, False)
        discsT += self._check_diagonals(transposed, col-1, lowest_disc_row_t-1, player_value, True)
        discsT += self._check_diagonals(transposed, col+1, lowest_disc_row_t+1, player_value, False)

        return discs >= 4 or discsT>=4

    def _check_diagonals(self, board, col, row, player_value, look_up):
        if col >= 0 and row >=0 and col < board.column_size and row < board.row_size:
            if look_up:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_diagonals(board, col-1, row-1, player_value, look_up)
            else:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_diagonals(board, col+1, row+1, player_value, look_up)
        return 0            