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
        
    def search_best_move(self, state_board, board_area):
        """
            Looks for the best move to take, it calls min_value
            with all the columns then decides the best move amongst then
        """
        best_move = -2
        current_max = self.MIN
        best_max = self.MIN
        
        for col in board_area :
            
            if not(state_board.is_column_full(col)):
                child = state_board.copy()
                child.insert_value_IA(col+1, self.current_player)
                current_max = self.min_value(0, child, self.MIN, self.MAX)
                
                if( current_max > best_max):
                    best_move = col
                    best_max = current_max
                    
        return best_move
    
    def check_state(self, board, depth, player):
        """
            Returns True if theres a win, no more legal moves or the depth
            has come to 0
        """
        checker = Checker()
        win = checker.check_win(board, board.last_column, player)
        legal_moves = not(board.have_legal_move())
        over = depth > self.depth_max
        return  win or legal_moves or over
            
    
    def heuristic(self, state_board):
        """
            Fathers Model funtion
        """
        return 0
    
    def min_value(self, depth, state_board, alfa, beta):
        """

        """
        
        if self.check_state(state_board, depth, self.current_player):
            return self.heuristic(state_board)
            
        else:
            for col in range(state_board.column_size):
                
                if not(state_board.is_column_full(col)):
                    child = state_board.copy()
                    child.insert_value_IA(col+1, self.oponent) 
                    temp_alfa = self.max_value(depth+1, child, alfa, beta)
                    beta = min(beta, temp_alfa)
                    if alfa >= beta:
                        return alfa
            
            return beta
    
    def max_value(self, depth, state_board, alfa, beta):
        """

        """

        if self.check_state(state_board, depth, self.oponent):
            return self.heuristic(state_board)
            
        else: 
            for col in range(state_board.column_size):
                
                if not(state_board.is_column_full(col)):
                    
                    child = state_board.copy()
                    child.insert_value_IA(col+1, self.current_player)
                    temp_beta = self.min_value(depth+1, child, alfa, beta)
                    alfa = max(alfa, temp_beta)
                    if alfa >= beta:
                        return beta
            
            return alfa
    
    def print_state(self, depth, board):
        """
            Prints the actual depth and matrix
        """
        print ("Depth: ", depth)
        board.print_matrix()
    
class Secuential(MiniMax):
    def heuristic(self, state_board):
        """
        Overwrites heuristic function, it gives a 100000 weight to 4 in line
        discs, 100 to 3 in line discs and 1 to the 2 in line discs, then
        returns the sum of them all, if the oponent haves 4 in line returns
        -100000 
        """
        checker = Secuential_Count_Checker()
        discs_4 = checker.check_lines(state_board, self.current_player, 4)
        discs_3 = checker.check_lines(state_board, self.current_player, 3)
        discs_2 = checker.check_lines(state_board, self.current_player, 2)
        oponent_discs_4 = checker.check_lines(state_board, self.oponent, 4)
        if oponent_discs_4 > 0:
            return -100000
        return discs_4*100000 + discs_3*100 + discs_2

class Espaces(MiniMax):
    def heuristic(self, state_board):
        """
        Overwrites heuristic function, it gives a 100000 weight to 4 in line
        discs, 100 to 3 in line with spaces discs and 1 to the 2 in line with 
        spaces discs, then returns the sum of them all, if the oponent haves 
        4 in line returns -100000 
        """
        checker = Checker()
        discs_4 = checker.check_lines(state_board, self.current_player, 4)
        discs_3 = checker.check_lines(state_board, self.current_player, 3)
        discs_2 = checker.check_lines(state_board, self.current_player, 2)
        oponent_discs_4 = checker.check_lines(state_board, self.oponent, 4)
        if oponent_discs_4 > 0:
            return -100000
        return discs_4*100000 + discs_3*100 + discs_2
           
    
    

