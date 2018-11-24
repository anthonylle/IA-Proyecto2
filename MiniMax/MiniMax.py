from Board.Board import Board
import sys

class MiniMax():

    def __init__(self):
        self.MAX = sys.maxsize
        self.MIN = -sys.maxsize -1
        
    # state_board is object of Board class
    # player_piece is char value   
    # sector is a list with the columns number to apply this
    def minimax_search(self, state_board, depth, player_piece, sector):
        best_move = -1
        temp_max = self.MIN
        best_max = temp_max
        
        for i in sector :
            pass
        
        return best_move
        
    
    
                
    
    

