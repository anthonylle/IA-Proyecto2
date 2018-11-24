
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
        
class Win_Checker(Checker):
    def set_player_value(self, players, actual):
        return players[actual].character

class Block_Checker(Checker):
    def set_player_value(self, players, actual):
        return players[not(actual)].character