import random
from WinAndBlock.WinAndBlock import Win_Checker, Block_Checker

class Agent():
    
    def __init__(self, percent_first_move, percent_second_move, percent_third_move, percent_fourth_move):
        self.percent_first_move = percent_first_move
        self.percent_second_move = percent_second_move
        self.percent_third_move = percent_third_move
        self.percent_fourth_move =percent_fourth_move
        self.my_die = 0
        self.last_move = 0
        self.last_moves = list()
        self.win_checker = Win_Checker()
        self.block_checker = Block_Checker()
        
    def throw_die(self):
        self.my_die = random.uniform(0, 1)
    
    def select_move(self):
        print("mi dado: ", self.my_die)
        if self.my_die <= self.percent_first_move:
            print("escojo el primer movimiento")
        
        elif self.my_die <= self.percent_second_move:
            print("escojo el segundo movimiento")
            
        elif self.my_die <= self.percent_third_move:
            print("escojo el tercer movimiento")
            
        else:
            print("escojo el cuarto movimiento")

    def next_move(self, board, players, actual):
        col_move = 0
        win = self.win_checker.check(self, board, players, actual)
        block = self.block_checker.check(self, board, players, actual)
        if win != -1:
            col_move = win
        elif block != -1:
            col_move = block
        #else:
            #Llamar función electora de estrategia
        return col_move
