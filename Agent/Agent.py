from WinAndBlock.WinAndBlock import Win_Checker, Block_Checker
from MiniMax.MiniMax import *
from Player.Player import Player
from operator import itemgetter
from collections import OrderedDict
import random

class Agent(Player):
    
    def __init__(self,character, name ,percent_first_move, 
                 percent_second_move, percent_third_move, percent_fourth_move):
        Player.__init__(self, character, name)
        self.percent_first_move = percent_first_move
        self.percent_second_move = percent_second_move
        self.percent_third_move = percent_third_move
        self.percent_fourth_move =percent_fourth_move
        self.last_move = 0
        self.last_moves = list()
        self.win_checker = Win_Checker()
        self.block_checker = Block_Checker()
        self.ranges = {}
        self.create_ranges(percent_first_move, percent_second_move, 
                           percent_third_move, percent_fourth_move)

    #--------------------------------------------------------------------------
    def throw_die(self, from_, to_):
        """input : from min value value to max value
        function: throw_die for a new percent
        output: none
        """        
        my_die = random.uniform(from_, to_)
        return  round(my_die,2)
        
    #--------------------------------------------------------------------------
    def select_move(self, board_state,depth_max, oponent):
        """
        input: a Board object, max depth to search, oponent character(human)
        function: select the best move using minimax
        output: int with column number > 0     
        """
        
        die = self.throw_die(0, self.percent_fourth_move)
        print("mi dado: ", die)
        
        if self.is_in_range(0,die):
            print("escojo el de secuencia vs espacio")
            return self.sequence_vs_space(board_state,depth_max, oponent)
        elif self.is_in_range(1,die):
            print("escojo centro vs centros")
            return self.center_vs_extremes(board_state,depth_max, oponent)

        elif self.is_in_range(2,die):
            print("escojo el tercer movimiento")
            
        elif self.is_in_range(3,die):
            print("escojo el cuarto movimiento")

    #--------------------------------------------------------------------------
    def sequence_vs_space(self,board_state,depth_max, oponent):
        """
        input: a Board object, max depth to search, oponent character(human)
        funtion: select the sequence or space
        output: none
        """
        die = self.throw_die(0, self.percent_fourth_move)
        if die <= 0.60: # sequence
            minimax = Secuential(depth_max, self.character, depth_max)
            return minimax.search_best_move(board_state, [0,1,2,3,4,5,6])
        else:
            minimax = Spaces(depth_max, self.character, depth_max)
            return minimax.search_best_move(board_state, [0,1,2,3,4,5,6])
            pass

    #--------------------------------------------------------------------------
    def center_vs_extremes(self,board_state,depth_max, oponent):
        """
        input: a Board object, max depth to search, oponent character(human)
        funtion: select center or extreme
        output: none
        """
        
        if board_state.is_legal_area([2,3,4]):
            return board_state.get_column_with_space([3,2,4])
        elif board_state.is_legal_area([0,1,5,6]):
            return board_state.get_column_with_space([1,5,0,6])
        else:
            return -2     
        
     #--------------------------------------------------------------------------       
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
            minimax = Spaces(3, self.character, '1')
            col_move = minimax.search_best_move(board, [0,1,2,3,4,5,6])
            #col_move = random.randint(0, 6)+1
        return col_move

    #--------------------------------------------------------------------------
    def create_ranges(self,percent_first_move,percent_second_move, 
                      percent_third_move, percent_fourth_move):
        """
        input: 4 floats with the percents
        funtion: create the ranges for the agent
        output: none        
        """
        the_ranges = {}
        ranges = {0:percent_first_move, 1:percent_second_move, 
                  2:percent_third_move, 3:percent_fourth_move}
        sorted_r = OrderedDict(sorted(ranges.items(), key=itemgetter(1)))
        ranges = dict(sorted_r)
        keys = list(ranges)
        
        the_ranges[keys[0]] = [0,ranges[keys[0]] ]
        the_ranges[keys[1]] = [ranges[keys[0]]+0.01, ranges[keys[1]] ]
        the_ranges[keys[2]] = [ranges[keys[1]]+0.01, ranges[keys[2]] ]
        the_ranges[keys[3]] = [ranges[keys[2]]+0.01, ranges[keys[3]] ]
        
        return the_ranges
        
    #--------------------------------------------------------------------------
    def is_in_range(self, key, value):
        """
            input: key in ranges, value between range
            function: to verify if value is between key range
            output: boolean value
        """
        return self.ranges[key][0] <= value and self.ranges[key][1] >= value