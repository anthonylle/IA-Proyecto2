
class Player():
    WINS = 0
    LOSSES = 1
    DRAWS = 2

    # character is a char
    # color is a string, see ConsoleControl class
    def __init__(self, character, name):
        self.character = character
        self.name = name
        self.my_pieces_positions = list()
        self.record = [0, 0, 0]
    
    def add_win(self):
        self.record[self.WINS] += 1
    
    def add_lose(self):
        self.record[self.LOSSES] += 1
    
    def add_draw(self):
        self.record[self.DRAWS] +=1

    def print_record(self):
        print("{} Record: Wins: {} | Losses: {} | draws: {}".format(self.name,
        self.record[self.WINS], self.record[self.LOSSES],
        self.record[self.DRAWS]))
        
    