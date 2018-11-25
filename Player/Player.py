
class Player():
    WINS = 0
    LOSSES = 1
    DRAWS = 2

    def __init__(self, character, name):
        """
            character is a char
            color is a string, see ConsoleControl class
        """
        self.character = character
        self.name = name
        self.my_pieces_positions = list()
        self.record = [0, 0, 0]
    
    def add_win(self):
        """
            Adds 1 to the WINS(0) in the vector record
        """
        self.record[self.WINS] += 1
    
    def add_lose(self):
        """
            Adds 1 to the LOSSES(0) in the vector record
        """
        self.record[self.LOSSES] += 1
    
    def add_draw(self):
        """
            Adds 1 to the DRWS(0) in the vector record
        """
        self.record[self.DRAWS] +=1

    def print_record(self):
        """
            Prints the Record of a Player
            e.g record=[2,1,0]
            Player Record: Wins: 2 | Losses: 1 | draws: 0
        """
        print("{} Record: Wins: {} | Losses: {} | draws: {}".format(self.name,
        self.record[self.WINS], self.record[self.LOSSES],
        self.record[self.DRAWS]))
        
    