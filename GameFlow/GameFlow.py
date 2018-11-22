from MessagePrinter.MessagesPrinter import MessagePrinter
from Board.Board import Board
from BoardPrinter.BoardPrinter import BoardPrinter
from Player.Player import Player

class GamePlay():

    #def __init__(self):


    def start_game(self):
        players = []
        play_again = "y"
        messages = MessagePrinter('clear')
        messages.welcome_message("bright", "", "green")
        play = messages.input_option(">>>> Do you want to star the game?[y/n]: ")
        
        if (play != "n"):
            P1name = messages.input_option("Enter Player1's name: ")
            players.append(Player('1', P1name))
            P2name = messages.input_option("Enter Player2's name: ")
            players.append(Player('2', P2name))
            
            while play_again != "n":
                board = Board(6,7)
                board.create()
                bp = BoardPrinter('clear',"bringht", "", "blue")
                bp.load_boar(board.column_size)

                self.play(players, bp, messages, board)
                play_again = messages.input_option(">>>> Do you want to play again?[y/n]: ")
        
    
    def play(self, players, bp, messages, board):
        Actual = 0
        bp.print_board(board)
        try:
            _input = int(messages.input_option(">>>> {} select a column's number: ".format(players[Actual].name)))
        except ValueError:
            _input = -2
            messages.alert("invalid move ! D:")
        while( _input  != -1):
            bp.clear_console()
            messages.title("bright","","cyan")
            
            if board.insert_value(_input, players[Actual].character):
                bp.print_board(board)
                if self.check_win(board, _input-1, players[Actual].character):
                    if Actual:
                        messages.player2_wins("bright", "", "cyan")
                    else:
                        messages.player1_wins("bright", "", "cyan")
                    print("{} is the winner".format(players[Actual].name))
                    break
                Actual = not(Actual)
            else:
                bp.print_board(board)
                messages.alert("invalid move ! D:")
            try:
                _input = int(messages.input_option(">>>> {} select a column's number: ".format(players[Actual].name)))
            except ValueError:
                _input = -2
                messages.alert("invalid move ! D:")

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

