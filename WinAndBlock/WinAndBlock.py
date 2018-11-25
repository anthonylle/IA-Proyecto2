
class Checker():

    def check(self, connect4, board, players, actual):
        for col in range(board.column_size):
            player_char = self.set_player_value(players, actual)
            board.insert_value(col+1, player_char)
            row = board.get_highest_disc(col, player_char)
            if (self.check_win(board, col, player_char)):
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
    
    def check_verticals_count(self, board, col, player_value, next_discs):
        discs = 0
        highest_disc_row = board.get_highest_disc(col, player_value)
        for i in range(highest_disc_row, highest_disc_row+next_discs):
            if i >= board.column_size-1 or board.getAt(i, col) != player_value:
                break
            discs += 1
        return discs

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

    def check_horizontals_count(self, board, col, player_value, next_discs):
        discs = 1 #Actual
        highest_disc_row = board.get_highest_disc(col, player_value)
        discs += self._check_horizontals_count(board, col+1, highest_disc_row, player_value, True, next_discs)
        discs += self._check_horizontals_count(board, col-1, highest_disc_row, player_value, False, next_discs)
        return discs

    def _check_horizontals_count(self, board, col, row, player_value, look_right, next_discs):
        if col >= 0 and col <= board.column_size-1 and next_discs > 0:
            if look_right:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_horizontals_count(board, col+1, row, player_value, look_right, next_discs-1)
                elif board.getAt(row, col) == " ":
                    return self._check_horizontals_count(board, col+1, row, player_value, look_right, next_discs-1)
            else:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_horizontals_count(board, col-1, row, player_value, look_right, next_discs-1)
                elif board.getAt(row, col) == " ":
                    return self._check_horizontals_count(board, col-1, row, player_value, look_right, next_discs-1)
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
    
    def check_diagonals_count(self, board, col, player_value, next_discs, identity):
        discs = 1 #Actual
        if not(identity):
            matrix = board.get_transposed()
            disc_row = matrix.get_lowest_disc(col, player_value)
        else:
            matrix = board
            disc_row = matrix.get_highest_disc(col, player_value)
        discs += self._check_diagonals_count(matrix, col-1, disc_row-1, player_value, True, next_discs)
        discs  += self._check_diagonals_count(matrix, col+1, disc_row+1, player_value, False, next_discs)

        return discs

    def _check_diagonals_count(self, board, col, row, player_value, look_up, next_discs):
        if col >= 0 and row >=0 and col < board.column_size and row < board.row_size and next_discs > 0:
            if look_up:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_diagonals_count(board, col-1, row-1, player_value, look_up, next_discs-1)
                elif board.getAt(row, col) == " ":
                    return self._check_diagonals_count(board, col-1, row-1, player_value, look_up, next_discs-1)
            else:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_diagonals_count(board, col+1, row+1, player_value, look_up, next_discs-1)
                elif board.getAt(row, col) == " ":
                    return self._check_diagonals_count(board, col+1, row+1, player_value, look_up, next_discs-1)
        return 0

class Win_Checker(Checker):
    def set_player_value(self, players, actual):
        return players[actual].character

class Block_Checker(Checker):
    def set_player_value(self, players, actual):
        return players[not(actual)].character

class Secuential_Count_Checker(Checker):

    def check_verticals_count(self, board, row, col, player_value, next_discs):
        discs = 0
        for i in range(row, row+next_discs):
            if i >= board.column_size-1 or board.getAt(i, col) != player_value:
                break
            discs += 1
        if discs >= next_discs:
            return 1
        return 0
    
    def check_horizontals_count(self, board, row, col, player_value, next_discs):
        discs = 1 #Actual
        discs += self._check_horizontals_count(board, col+1, row, player_value, True, next_discs)
        discs += self._check_horizontals_count(board, col-1, row, player_value, False, next_discs)
        if discs >= next_discs:
            return 1
        return 0
    
    def check_diagonals(self, board, row, col, player_value, next_discs):
        discs = 1  #Actual
        discsT = 1 #Actual
        total = 0
        transposed = board.get_transposed()
        rowT = (board.row_size-1)-row
        discs  += self._check_diagonals(board, col-1, row-1, player_value, True)
        discs  += self._check_diagonals(board, col+1, row+1, player_value, False)
        discsT += self._check_diagonals(transposed, col-1, rowT-1, player_value, True)
        discsT += self._check_diagonals(transposed, col+1, rowT+1, player_value, False)

        total+=1 if discs >= next_discs else total
        total+=1 if discsT >= next_discs else total
        return total