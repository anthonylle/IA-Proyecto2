from WinAndBlock.WinAndBlock import Win_Checker, Block_Checker
from MiniMax.MiniMax import *
from Player.Player import Player
import random

class Agent(Player):
    
    def __init__(self,character, name ,percent_first_move, 
                 percent_second_move, percent_third_move, percent_fourth_move):
        Player.__init__(self, character, name)
        self.percent_first_move = percent_first_move
        self.percent_second_move = percent_second_move
        self.percent_third_move = percent_third_move
        self.percent_fourth_move =percent_fourth_move
        self.my_die = 0
        self.last_move = 0
        self.last_moves = list()
        self.win_checker = Win_Checker()
        self.block_checker = Block_Checker()

    #--------------------------------------------------------------------------
    def throw_die(self):
        """input : none
        
        function: throw_die for a new percent
        
        output: none
        
        """        
        self.my_die = random.uniform(0, 1)

    #--------------------------------------------------------------------------
    def select_move(self, board_state,depth_max, oponent):
        """
        input: a Board object, max depth to search, oponent character(human)
        function: select the best move using minimax
        output: int with column number > 0     
        """
        #minimax = MiniMax(depth_max, self.character, oponent)
        print("mi dado: ", self.my_die)
        
        if self.my_die <= self.percent_first_move:
            print("escojo el de secuencia vs espacio")
            minimax = Secuential(depth_max, self.character, oponent)
            return minimax.search_best_move(board_state, [0,1,2,3,4,5,6])
        elif self.my_die <= self.percent_second_move:
            print("escojo centro vs centros")
            #return minimax.search_best_move(board_state, [2,3,4])
            #return minimax.search_best_move(board_state, [0,1,5,6])
        elif self.my_die <= self.percent_third_move:
            print("escojo el tercer movimiento")
            
        else:
            print("escojo el cuarto movimiento")

    def next_move(self, board, players, actual):
        """
            Checks if it can win el if it can block else make a move from
            the strategies
        """
        col_move = 0
        win = self.win_checker.check(self, board, players, actual)
        block = self.block_checker.check(self, board, players, actual)
        if win != -1:
            col_move = win
        elif block != -1:
            col_move = block
        else:
            #Llamar función electora de estrategia
            #minimax = Secuential(3, self.character, '1')
            minimax = Espaces(3, self.character, '1')
            col_move = minimax.search_best_move(board, [0,1,2,3,4,5,6])+1
            #col_move = random.randint(0, 6)+1
        return col_move
