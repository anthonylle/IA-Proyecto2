import random

class Agent():
    
    def __init__(self, percent_first_move, percent_second_move, percent_third_move, percent_fourth_move):
        self.percent_first_move = percent_first_move
        self.percent_second_move = percent_second_move
        self.percent_third_move = percent_third_move
        self.percent_fourth_move =percent_fourth_move
        self.my_die = 0
        self.last_move = 0
        self.last_moves = list()
        
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

