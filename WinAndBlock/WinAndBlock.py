
class Checker():

    def check(self, connect4, board, players, actual):
        """
            Checks if the actual player in the actual board can win
            and returns the respective column number 
        """
        board_temp = board.copy()
        for col in range(board_temp.column_size):

            player_char = self.set_player_value(players, actual)
            board_temp.insert_value(col+1, player_char)
            row = board_temp.get_highest_disc(col, player_char)
            if (self.check_win(board_temp, col, player_char)):
                board_temp.setAt(row, col, " ")
                return col+1
            board_temp.setAt(row, col, " ")
        return -1
    
    def set_player_value(self, players, actual):
        """
            it is used in the children functions to check if it is looking
            for actual player win or actual player lose
            Returns the payer value to look up
        """
        return "1"
    
    def check_win(self, board, col, player_value):
        """
            Main function to check if the player given can win in the 
            actual board
            Returns True or False
        """
        return self.check_verticals(board, col, player_value
                ) or self.check_horizontals(board, col, player_value
                ) or self.check_diagonals(board, col, player_value)

    def check_lines(self, board, player_value, next_discs):
        """
            Main check lines function which returns how many verticals, 
            horizontals and diagonals there are of the actual player 
            in the actual board, of an x number of discs limit,
            it recovers the entire board
        """
        lines_count = 0
        for row in range(board.row_size):
            for col in range(board.column_size):
                if board.getAt(row, col) == player_value:
                    lines_count += self.check_verticals_count(board, row,
                                            col, player_value, next_discs)
                    lines_count += self.check_horizontals_count(board, row, 
                                            col, player_value, next_discs)
                    lines_count += self.check_diagonals_count(board, row, 
                                            col, player_value, next_discs)
        return lines_count

    def check_verticals(self, board, col, player_value):
        """
            it returns True if there are 4 vertical discs in the given column
            False if not
        """
        four_in_a_row = False
        highest_disc_row = board.get_highest_disc(col, player_value)
        if (highest_disc_row <= 2):
            for i in range(highest_disc_row, highest_disc_row+4):
                if board.getAt(i, col) != player_value:
                    break
                elif i == highest_disc_row+3:
                    four_in_a_row = True
        return four_in_a_row
    
    def check_verticals_count(self, board, row, col, player_value, next_discs):
        """
            returns 1 if there are x or more discs in a vertical row 
            0 if not
        """
        discs = 0
        for i in range(row, row+next_discs):
            if i >= board.column_size-1 or board.getAt(i, col)!=player_value:
                break
            discs += 1
        return discs >= next_discs

    def check_horizontals(self, board, col, player_value):
        """
            it checks if there are 4 horizontals discs in a row
            returns True if so, else False
            it checks to right and left from the last disc inserted 
            in the board, variations of Breadth-first search
        """
        discs = 1 #Actual
        highest_disc_row = board.get_highest_disc(col, player_value)
        discs += self._check_horizontals(board, col+1, highest_disc_row, 
                                                        player_value, True)
        discs += self._check_horizontals(board, col-1, highest_disc_row, 
                                                        player_value, False)
        return discs >= 4
    
    def _check_horizontals(self, board, col, row, player_value, look_right):
        """
            Auxiliar recurcive function, returns the amount of horizontal
            discs in a row to left or right from the col and row 
            possition given
        """
        if col >= 0 and col <= board.column_size-1:
            if look_right:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_horizontals(board, col+1, row,
                                                player_value, look_right)
            else:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_horizontals(board, col-1, row, 
                                                player_value, look_right)
        return 0

    def check_horizontals_count(self,board,row,col,player_value,next_discs):
        """
            check if there are x discs count next to the row, col given
            Returns True of False, uses Breadth-first search
        """
        discs = 0
        if board.getAt(row, col) == player_value:
            discs += 1
        discs += self._check_horizontals_count(board, col+1, row, 
                                            player_value, True, next_discs)
        discs += self._check_horizontals_count(board, col-1, row, 
                                            player_value, False, next_discs)
        return discs >= next_discs

    def _check_horizontals_count(self,board,col,row,player_value,look_right,next_discs):
        """
            Auxiliar recursive function returns the amount of horizontal
            discs to left or right from the col,row  given even if there
            are empty squares in the way
        """
        if col >= 0 and col <= board.column_size-1 and next_discs > 0:
            if look_right:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_horizontals_count(board, col+1,
                                row, player_value, look_right, next_discs-1)
                elif board.getAt(row, col) == " ":
                    return self._check_horizontals_count(board, col+1, row, 
                                    player_value, look_right, next_discs-1)
            else:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_horizontals_count(board, col-1, 
                                row, player_value, look_right, next_discs-1)
                elif board.getAt(row, col) == " ":
                    return self._check_horizontals_count(board, col-1, row, 
                                    player_value, look_right, next_discs-1)
        return 0

    def check_diagonals(self, board, col, player_value):
        """
            it checks if there are 4 diagonals discs in a row
            returns True if so, else False
            it checks to up and down from the last disc inserted
            in the board, variation of Breadth-first search
            uses the transposed matrix to check 2 types of diagonals
        """
        discs = 1  #Actual
        discsT = 1 #Actual
        transposed = board.get_transposed()
        highest_disc_row = board.get_highest_disc(col, player_value)
        lowest_disc_row_t = transposed.get_lowest_disc(col, player_value)
        discs  += self._check_diagonals(board, col-1, highest_disc_row-1,
                                                        player_value, True)
        discs  += self._check_diagonals(board, col+1, highest_disc_row+1, 
                                                        player_value, False)
        discsT += self._check_diagonals(transposed, col-1,lowest_disc_row_t-1,
                                                        player_value, True)
        discsT += self._check_diagonals(transposed, col+1,lowest_disc_row_t+1, 
                                                        player_value, False)

        return discs >= 4 or discsT>=4   

    def _check_diagonals(self, board, col, row, player_value, look_up):
        """
            Auxiliar recurcive function, returns the amount of diagonals
            discs in a row to up or down from the col and row 
            possition given
        """
        if col>=0 and row>=0 and col<board.column_size and row<board.row_size:
            if look_up:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_diagonals(board, col-1, row-1, 
                                                        player_value, look_up)
            else:
                if board.getAt(row, col) == player_value:
                    return 1 + self._check_diagonals(board, col+1, row+1,
                                                        player_value, look_up)
        return 0
    
    def check_diagonals_count(self, board, row, col, player_value, next_discs):
        """
            check if there are x discs count in diagonal next to the row,col 
            given, returns 0,1 or 2, 2 if there are x discs in both diagonals
            uses Breadth-first search
        """
        total = 0
        discs = self._check_diagonals_count(board, row, col, player_value, 
                                                            next_discs, True)
        discsT = self._check_diagonals_count(board, row, col, player_value, 
                                                            next_discs, False)
        if discs >= next_discs:
            total+=1
        if discsT >= next_discs:
            total+=1
        return total

    def _check_diagonals_count(self,board,row,col,player_value,next_discs,identity):
        """
            returns the amount of discs next to the row,col given in diagonal
            uses Breadth-first search
        """
        discs = 0
        if board.getAt(row, col) == player_value:
            discs += 1
        if not(identity):
            matrix = board.get_transposed()
            row = (board.row_size-1)-row
        else:
            matrix = board
        discs += self.__check_diagonals_count(matrix, col-1, row-1,
                                                        player_value, True)
        discs += self.__check_diagonals_count(matrix, col+1, row+1, 
                                                        player_value, False)

        return discs

    def __check_diagonals_count(self, board, col, row, player_value, look_up):
        """
            Auxiliar recursive function returns the amount of diagonals
            discs to up or down from the col,row  given even if there
            are empty squares in the way
        """
        if col>=0 and row>=0 and col<board.column_size and row<board.row_size:
            if look_up:
                if board.getAt(row, col) == player_value:
                    return 1 + self.__check_diagonals_count(board, col-1, 
                                                row-1, player_value, look_up)
                elif board.getAt(row, col) == " ":
                    return self.__check_diagonals_count(board, col-1, row-1,
                                                        player_value, look_up)
            else:
                if board.getAt(row, col) == player_value:
                    return 1 + self.__check_diagonals_count(board, col+1, 
                                                row+1, player_value, look_up)
                elif board.getAt(row, col) == " ":
                    return self.__check_diagonals_count(board, col+1, row+1,
                                                        player_value, look_up)
        return 0

class Win_Checker(Checker):
    def set_player_value(self, players, actual):
        """
            Overwrited funtion, to check the actual players win
        """
        return players[actual].character

class Block_Checker(Checker):
    def set_player_value(self, players, actual):
        """
            Overwrited funtion, to check the oponents win
        """
        return players[not(actual)].character

class Secuential_Count_Checker(Checker):
    def check_lines(self, board, player_value, next_discs):
        """
            Overwrited function, deffers from its father in calling 
            check_diagonals instead of check_diagonals_count
        """
        lines_count = 0
        for row in range(board.row_size):
            for col in range(board.column_size):
                if board.getAt(row, col) == player_value:
                    lines_count += self.check_verticals_count(board, row, col,
                                                    player_value, next_discs)
                    lines_count += self.check_horizontals_count(board, row, 
                                                col, player_value, next_discs)
                    lines_count += self.check_diagonals(board, row, col, 
                                                    player_value, next_discs)
        return lines_count

    def check_horizontals_count(self,board,row,col,player_value,next_discs):
        """
            Overwrited function it differs from it father when asign discs = 1
            insted of discs = 0
        """
        discs = 1 #Actual
        discs += self._check_horizontals_count(board, col+1, row, player_value, True, next_discs)
        discs += self._check_horizontals_count(board, col-1, row, player_value, False, next_discs)
        if discs >= next_discs:
            return 1
        return 0
    
    def check_diagonals(self, board, row, col, player_value, next_discs):
        """
            Overwrited function it differs from it father when asign discs = 1
            insted of discs = 0
        """
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
    
class Block_3_In_Line_Checker(Checker):
    def check_verticals_count(self,board,row,col,player_value,next_discs):
        """
            returns 1 if there are x or more discs in a vertical row 
            with a block at the begining
        """
        discs = 0

        if board.getAt(row, col) == player_value:
            discs += 1
            for i in range(row+1, row+next_discs):
                if i >= board.column_size-1 or board.getAt(i, col)==player_value:
                    break
                discs += 1
        return discs >= next_discs

    def check_horizontals_count(self,board,row,col,player_value,next_discs):
        """
            checks if there are x discs count next to the row, with at least
            one actual player disc in the row, to seach blocks
        """
        player_discs = 0
        discs = 0
        if board.getAt(row, col) == player_value:
            player_discs += 1
        if board.getAt(row, col)!=player_value and board.getAt(row, col)!=" ":
            discs += 1
        discs += self._check_horizontals_count(board, col+1, row, 
                                            player_value, True, 2, True)
        discs += self._check_horizontals_count(board, col-1, row, 
                                            player_value, False, 2, True)
        player_discs += self._check_horizontals_count(board, col+1, row, 
                                            player_value, True, 2, False)
        player_discs += self._check_horizontals_count(board, col-1, row, 
                                            player_value, False, 2, False)
        
        return player_discs >=1 and discs >= next_discs-1


    def _check_horizontals_count(self,board,col,row,player_value,look_right,next_discs,oponent):
        """
            Auxiliar recursive function returns the amount of horizontal
            discs to left or right from the col,row  given even if there
            are empty squares in the way, it have the oponent option to 
            look for oponent or actual player discs 
        """
        if col >= 0 and col <= board.column_size-1 and next_discs > 0:
            if look_right:
                if oponent:
                    if board.getAt(row, col)!=player_value and board.getAt(row, col)!=" ":
                        return 1 + self._check_horizontals_count(board, col+1,
                                row, player_value, look_right, next_discs-1, oponent)
                    else:
                        return self._check_horizontals_count(board, col+1, row, 
                                        player_value, look_right, next_discs-1, oponent)
                else:
                    if board.getAt(row, col) == player_value:
                        return 1 + self._check_horizontals_count(board, col+1,
                                    row, player_value, look_right, next_discs-1, oponent)
                    else:
                        return self._check_horizontals_count(board, col+1, row, 
                                        player_value, look_right, next_discs-1, oponent)
            else:
                if oponent:
                    if board.getAt(row, col)!=player_value and board.getAt(row, col)!=" ":
                        return 1 + self._check_horizontals_count(board, col-1,
                                row, player_value, look_right, next_discs-1, oponent)
                    else:
                        return self._check_horizontals_count(board, col-1, row, 
                                        player_value, look_right, next_discs-1, oponent)
                else:
                    if board.getAt(row, col) == player_value:
                        return 1 + self._check_horizontals_count(board, col-1,
                                    row, player_value, look_right, next_discs-1, oponent)
                    else:
                        return self._check_horizontals_count(board, col-1, row, 
                                        player_value, look_right, next_discs-1, oponent)
        return 0

    def check_diagonals_count(self, board, row, col, player_value, next_discs):
        """
            check if there are x discs count in diagonal next to the row,col 
            given, returns 0,1 or 2, 2 if there are x discs in both diagonals
            with at least one actual player discs in the middle
        """
        total = 0
        discs = self._check_diagonals_count(board, row, col, player_value, 
                                                            next_discs, True)
        discsT = self._check_diagonals_count(board, row, col, player_value, 
                                                            next_discs, False)
        total = discs + discsT
        return total
    
    def _check_diagonals_count(self,board,row,col,player_value,next_discs,identity):
        """
            returns the amount of discs next to the row,col given in diagonal
            looks for oponent discs and players discs
        """
        player_discs = 0
        discs = 0
        if board.getAt(row, col) == player_value:
            player_discs += 1
        if board.getAt(row, col)!=player_value and board.getAt(row, col)!=" ":
            discs += 1
        if not(identity):
            matrix = board.get_transposed()
            row = (board.row_size-1)-row
        else:
            matrix = board
        discs += self.__check_diagonals_count(matrix, col-1, row-1,
                                                        player_value,2, True, True)
        discs += self.__check_diagonals_count(matrix, col+1, row+1, 
                                                        player_value,2, False, True)
        player_discs += self.__check_diagonals_count(matrix, col-1, row-1,
                                                        player_value,2, True, False)
        player_discs += self.__check_diagonals_count(matrix, col+1, row+1, 
                                                        player_value,2, False, False)
        return player_discs >= 1 and discs >= next_discs-1
    
    def __check_diagonals_count(self, board, col, row, player_value, next_discs, look_up, oponent):
        """
            Auxiliar recursive function returns the amount of diagonals
            discs to up or down from the col,row  given even if there
            are empty squares in the way, also looks for oponent discs or 
            players discs
        """
        if col>=0 and row>=0 and col<board.column_size and row<board.row_size and next_discs >0:
            if look_up:
                if oponent:
                    if board.getAt(row, col)!=player_value and board.getAt(row, col)!=" ":
                        return 1 + self.__check_diagonals_count(board, col-1, 
                                                    row-1, player_value,next_discs-1, look_up, oponent)
                    else:
                        return self.__check_diagonals_count(board, col-1, row-1,
                                                            player_value,next_discs-1, look_up, oponent)
                else:
                    if board.getAt(row, col)==player_value:
                        return 1 + self.__check_diagonals_count(board, col-1, 
                                                    row-1, player_value,next_discs-1, look_up, oponent)
                    else:
                        return self.__check_diagonals_count(board, col-1, row-1,
                                                            player_value,next_discs-1, look_up, oponent)   
            else:
                if oponent:
                    if board.getAt(row, col)!=player_value and board.getAt(row, col)!=" ":
                        return 1 + self.__check_diagonals_count(board, col+1, 
                                                    row+1, player_value,next_discs-1, look_up, oponent)
                    else:
                        return self.__check_diagonals_count(board, col+1, row+1,
                                                            player_value,next_discs-1, look_up, oponent)
                else:
                    if board.getAt(row, col)==player_value:
                        return 1 + self.__check_diagonals_count(board, col+1, 
                                                    row+1, player_value,next_discs-1, look_up, oponent)
                    else:
                        return self.__check_diagonals_count(board, col+1, row+1,
                                                            player_value,next_discs-1, look_up, oponent)
        return 0