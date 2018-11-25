from Board.Board import Board
from WinAndBlock.WinAndBlock import Checker
import sys

class MiniMax():

    def __init__(self, depth_max, current_player, oponent):
        self.MAX = sys.maxsize
        self.MIN = - sys.maxsize -1
        self.depth_max = depth_max
        self.current_player = current_player
        self.oponent = oponent
        
    # state_board is object of Board class
    # player_piece is char value   
    # board_area is a list with the columns number to apply this
    def search_best_move(self, state_board, board_area):
        best_move = -2
        current_max = self.MIN
        best_max = self.MIN
        
        for col in board_area :
            
            if not(state_board.is_column_full(col)):
                #print("---------------------------------------",col,"---------------------------------------")
                child = state_board.copy()
                child.insert_value(col+1, self.current_player)
                child.print_matrix()
                current_max = self.min_value(0, child, self.MIN, self.MAX)
                
                if( current_max > best_max):
                    best_move = col
                    best_max = current_max
                    
        return best_move
    
    # board is a board class 's object 
    def check_state(self, board, depth, player):
        checker = Checker()
        win = checker.check_win(board, board.last_column, player)
        legal_moves = not(board.have_legal_move())
        over = depth > self.depth_max
        #print("win: ", win, "legal moves: ", legal_moves, "over: ", over)
        return  win or legal_moves or over
            
    
    def heuristic(self):
        return 0
    
    def min_value(self, depth, state_board, alfa, beta):
        
        if self.check_state(state_board, depth, self.current_player):
            return self.heuristic()
            
        else:
            #print("----------- for del min ----------")
            for col in range(state_board.column_size):
                
                if not(state_board.is_column_full(col)):
                    child = state_board.copy()
                    child.insert_value(col+1, self.oponent) 
                    #print("-----------jagada valida ----------")
                    #self.print_state(depth, child)
                    temp_alfa = self.max_value(depth+1, child, alfa, beta)
                    beta = min(beta, temp_alfa)
                    if alfa >= beta:
                        return alfa
            
            return beta
    
    def max_value(self, depth, state_board, alfa, beta):

        if self.check_state(state_board, depth, self.oponent):
            return self.heuristic()
            
        else: 
            #print("----------- for del min ----------")
            for col in range(state_board.column_size):
                
                if not(state_board.is_column_full(col)):
                    
                    child = state_board.copy()
                    child.insert_value(col+1, self.current_player)
              #      print("-----------jagada valida ----------")
              #      self.print_state(depth, child)
                    temp_beta = self.min_value(depth+1, child, alfa, beta)
                    alfa = max(alfa, temp_beta)
                    if alfa >= beta:
                        return beta
            
            return alfa
    
    def print_state(self, depth, board):
        print ("Depth: ", depth)
        board.print_matrix()
           
    
    

