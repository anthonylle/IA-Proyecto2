from MessagePrinter.MessagesPrinter import MessagePrinter
from Board.Board import Board
from BoardPrinter.BoardPrinter import BoardPrinter
from Player.Player import Player

class GamePlay():

    #def __init__(self):


    def start_game(self):
        players = []
        messages = MessagePrinter('clear')
        messages.welcome_message("bright", "", "green")
        messages.input_option(">>>> Do you want star the game?[s/n]: ")
        
        board = Board(6,7)
        board.create()
        bp = BoardPrinter('clear',"bringht", "", "blue")
        bp.load_boar(board.column_size)

        P1name = messages.input_option("Enter Player1's name: ")
        players.append(Player('1', P1name))
        P2name = messages.input_option("Enter Player2's name: ")
        players.append(Player('2', P2name))

        self.play(players, bp, messages, board)
    
    def play(self, players, bp, messages, board):
        Actual = 0
        bp.print_board(board)
        _input = int(messages.input_option(">>>> {} select a column's number: ".format(players[Actual].name)))
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
            _input = int(messages.input_option(">>>> {} select a column's number: ".format(players[Actual].name)))

    def check_win(self, board, col, player_value):
        if self.check_verticals(board, col, player_value):
            return True
        if self.check_horizontals(board, col, player_value):
            return True
        if self.check_diagonals(board, col, player_value):
            return True
        return False

    def check_verticals(self, board, col, player_value):
        four_in_a_row = True
        highest_disc_row = board.get_highest_disc(col, player_value)
        if (highest_disc_row <= 2):
            for i in range(highest_disc_row, highest_disc_row+4):
                if board.getAt(i, col) != player_value:
                    four_in_a_row = False
                    break
        else:
            four_in_a_row = False
        return four_in_a_row
    
    def check_horizontals(self, board, col, player_value):
        four_in_a_row = False
        discs = 0
        highest_disc_row = board.get_highest_disc(col, player_value)
        for j in range(board.column_size):
            if board.getAt(highest_disc_row, j) == player_value:
                discs += 1
                if discs == 4:
                    four_in_a_row = True
                    break
            else:
                discs = 0
        return four_in_a_row

    def check_diagonals(self, board, col, player_value):
        four_in_a_row = False
        discs = 0
        transposed = board.get_transposed()
        highest_disc_row = board.get_highest_disc(col, player_value)
        lowest_disc_row_t = transposed.get_lowest_disc(col, player_value)
        return self._check_diagonals(board, col, player_value, 
                        four_in_a_row, discs, highest_disc_row) or self._check_diagonals(transposed, col,
                        player_value, four_in_a_row, discs, lowest_disc_row_t)
    
    def _check_diagonals(self, board, col, player_value, win, discs, row):
        row, col = board.get_diagonal_border(row, col)
        while row != board.row_size and col != board.column_size:
            if board.getAt(row, col) == player_value:
                discs += 1
                if discs == 4:
                    win = True
                    break
            else:
                discs = 0
            col += 1
            row += 1
        return win

