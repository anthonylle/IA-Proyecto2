from Board.Board import Board
from WinAndBlock.WinAndBlock import *
import sys

class MiniMax():

    def __init__(self, depth_max, current_player, oponent):
        self.MAX = sys.maxsize
        self.MIN = - sys.maxsize -1
        self.depth_max = depth_max
        self.current_player = current_player
        self.oponent = oponent
        
    #--------------------------------------------------------------------------   
    # state_board is object of Board class
    # player_piece is char value   
    # board_area is a list with the columns number to apply this
    #function: search the best move for an agent
    #output: an int with best 
    def search_best_move(self, state_board, board_area):
        """
            function: Looks for the best move to take, it calls min_value
            with all the columns then decides the best move amongst then
            output: an int with best 
        """
        best_move = -2
        current_max = self.MIN
        best_max = self.MIN
        
        for col in board_area :
            
            if not(state_board.is_column_full(col)):
                child = state_board.copy()
                child.insert_value(col+1, self.current_player)
                current_max = self.min_value(0, child, self.MIN, self.MAX)
                #print("curent_max", current_max, col)
                if( current_max > best_max):
                    best_move = col
                    best_max = current_max
        # +1 because the insert method only admit number bigger than 0           
        return best_move+1
    
    #--------------------------------------------------------------------------
    #input : board is a board class 's object, depth a int value and player is a 
    #        char with the player character
    #function: check if there a win, or the game is depth is the max
    #output: boolean value
    def check_state(self, board, depth, player):
        """
            function checks if there's a win, no more legal moves or the depth
            has come to 0
            output: boolean
        """
        checker = Checker()
        win = checker.check_win(board, board.last_column, player)
        legal_moves = not(board.have_legal_move())
        over = depth > self.depth_max
        return  win or legal_moves or over
            
    #--------------------------------------------------------------------------
    #input : 
    #function: 
    #output:
    def heuristic(self, state_board):
        """
            function: Fathers Model funtion
            output: 0
        """
        return 0
    
    #--------------------------------------------------------------------------
    #input : depth: int value, state_board: Board object, alfa: int value and beta: int value 
    #function: search the best value for the human(oponent) the worse for the computer
    #output: int value, the least between alfa and beta 
    def min_value(self, depth, state_board, alfa, beta):
        """
            function: search the best value for the human(oponent) the worse 
            for the computer
            output: int value, the least between alfa and beta 
        """
        if self.check_state(state_board, depth, self.current_player):
            return self.heuristic(state_board)
            
        else:
            for col in range(state_board.column_size):
                
                if not(state_board.is_column_full(col)):
                    child = state_board.copy()
                    child.insert_value(col+1, self.oponent) 
                    temp_alfa = self.max_value(depth+1, child, alfa, beta)
                    beta = min(beta, temp_alfa)
                    if alfa >= beta:
                        return alfa
            return beta
        
    #--------------------------------------------------------------------------
    #input : depth: int value, state_board: Board object, alfa: int value and beta: int value 
    #function: search the best value for the computer and the worse for the human (oponent)
    #output: int value, the higher bwtween alpha and beta   
    def max_value(self, depth, state_board, alfa, beta):
        """
            function: search the best value for the computer and the worse for
            the human (oponent)
            output: int value, the higher bwtween alpha and beta   
        """

        if self.check_state(state_board, depth, self.oponent):
            return self.heuristic(state_board)
            
        else: 
            for col in range(state_board.column_size):
                
                if not(state_board.is_column_full(col)):
                    
                    child = state_board.copy()
                    child.insert_value(col+1, self.current_player)
                    temp_beta = self.min_value(depth+1, child, alfa, beta)
                    alfa = max(alfa, temp_beta)
                    if alfa >= beta:
                        return beta
            
            return alfa
    
    #--------------------------------------------------------------------------
    #input : depth: an int value, and a Board object 
    #function: print the board state with its depth
    #output: none
    def print_state(self, depth, board):
        """
            function: Prints the actual depth and matrix
            output: None
        """
        print ("Depth: ", depth)
        board.print_matrix()
    
class Secuential(MiniMax):
    def heuristic(self, state_board):
        """
        fucntion: Overwrites heuristic function, it gives a 100000 weight to 4 in line
        discs, 100 to 3 in line discs and 1 to the 2 in line discs, then
        returns the sum of them all, if the oponent haves 4 in line returns
        -100000
        output: weight calculated
        """
        checker = Secuential_Count_Checker()
        discs_4 = checker.check_lines(state_board, self.current_player, 4)
        discs_3 = checker.check_lines(state_board, self.current_player, 3)
        discs_2 = checker.check_lines(state_board, self.current_player, 2)
        oponent_discs_4 = checker.check_lines(state_board, self.oponent, 4)
        if oponent_discs_4 > 0:
            return -100000
        return discs_4*100000 + discs_3*100 + discs_2

class Spaces(MiniMax):
    def heuristic(self, state_board):
        """
        function: Overwrites heuristic function, it gives a 100000 weight to 4 in line
        discs, 100 to 3 in line with spaces discs and 1 to the 2 in line with 
        spaces discs, then returns the sum of them all, if the oponent haves 
        4 in line returns -100000 
        output: weight calculated
        """
        checker = Checker()
        discs_4 = checker.check_lines(state_board, self.current_player, 4)
        discs_3 = checker.check_lines(state_board, self.current_player, 3)
        discs_2 = checker.check_lines(state_board, self.current_player, 2)
        oponent_discs_4 = checker.check_lines(state_board, self.oponent, 4)
        if oponent_discs_4 > 0:
            return -100000
        return discs_4*100000 + discs_3*100 + discs_2

class Block_3_In_Line(MiniMax):
    def heuristic(self, state_board):
        """
        function: Overwrites heuristic function, it gives a 1000 weight to 3 in line
        discs blocked, 100 to 2 in line with discs blocked and 150 to the 4 
        in line with discs blocked, then returns the sum of them all, if the 
        oponent haves 4 in line returns -100000 
        output: weight calculated
        """
        blocker = Block_3_In_Line_Checker()
        checker = Checker()
        oponent_discs_4 = checker.check_lines(state_board, self.oponent, 4)

        oponent_block_discs_3 = blocker.check_lines(state_board, self.oponent, 3)
        oponent_block_discs_2 = blocker.check_lines(state_board, self.oponent, 2)
        oponent_block_discs_4 = blocker.check_lines(state_board, self.oponent, 4)
        if oponent_discs_4 > 0:
            return -100000
        return oponent_block_discs_3*1000+oponent_block_discs_2*100+oponent_block_discs_4*150
           
class Play_3_In_Line(MiniMax):
    def heuristic(self, state_board):
        """
        function: Overwrites heuristic function, it gives a 1000 weight to 3 in line
        discs blocked, 100 to 2 in line with discs blocked and 150 to the 4 
        in line with discs blocked, then returns the sum of them all, if the 
        oponent haves 4 in line returns -100000 
        output: weight calculated
        """
        checker = Checker()
        discs_4 = checker.check_lines(state_board, self.current_player, 4)
        discs_3 = checker.check_lines(state_board, self.current_player, 3)
        discs_2 = checker.check_lines(state_board, self.current_player, 2)

        oponent_discs_4 = checker.check_lines(state_board, self.oponent, 4)
        if oponent_discs_4 > 0:
            return -100000
        return discs_3*1000 + discs_2*100 + discs_4*150
