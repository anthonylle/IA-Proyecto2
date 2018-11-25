
class Checker():

    def check(self, connect4, board, players, actual):
        for col in range(board.column_size):
            player_char = self.set_player_value(players, actual)
            board.insert_value(col+1, player_char)
            row = board.get_highest_disc(col, player_char)
            if (connect4.check_win(board, col, player_char)):
                board.setAt(row, col, " ")
                return col+1
            board.setAt(row, col, " ")
        return -1
    
    def set_player_value(self, players, actual):
        print("function definition")
        return "1"
    
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
        
class Win_Checker(Checker):
    def set_player_value(self, players, actual):
        return players[actual].character

class Block_Checker(Checker):
    def set_player_value(self, players, actual):
        return players[not(actual)].character