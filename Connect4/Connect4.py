from BoardPrinter.BoardPrinter import BoardPrinter
from Connect4View.Connect4View import Connect4View
from WinAndBlock.WinAndBlock import Checker
from Agent.Agent import Agent
from Player.Player import Player
from Board.Board import Board

# class to control all game's logic
class Connect4():
    
    #--------------------------------------------------------------------------
    #input : a string, 'cls' i for windows and 'clear' for ubunrun or other
    #function: constructor
    def __init__(self,system):
        self.board =  None
        self.system = system
        self.board_printer = None
        self.view = Connect4View(system)
        self.checker = Checker()
        self.game_modes = ["c_vs_c", "h_vs_h", "h_vs_c"]
        self.game_mode = self.game_modes[1]
        self.level = 1
        
    #--------------------------------------------------------------------------
    #input : none
    #function: create a game environment for default
    #output:    none
    def default(self):
        self.board =  Board(6,7)
        self.board.create()
        self.board_printer = BoardPrinter(self.system,"bringht", "", "white")
        self.board_printer.load_boar(self.board.column_size)        
    
    #--------------------------------------------------------------------------
    #input : none
    #function: controll for the new game option
    #output:none
    def new_game_menu(self):
        option = ""
        while option != "4":
            option = self.view.view_new_game_menu()
            if option == "1":
                self.type_game_menu()
            
            elif option == "2":
                self.level = self.select_level()
            elif option == "3":
                self.start_game()
                
            elif option == "4":
                self.view.clear_console()
                
            else:
                self.view.invalid_option()
    
    #--------------------------------------------------------------------------
    #input : none
    #function: controll for the level game option
    #output:none
    def select_level(self):
        self.view.view_title()
        level = self.view.select_level()
        if level >= 1 and level <= 4:
            return level
        else:
            self.view.invalid_option()
            return self.select_level()    
        
    #--------------------------------------------------------------------------
    #input : mode: an int value, index of game_moves variable
    #output:none
    def set_game_mode(self,mode):
        self.game_mode = self.game_modes[mode]
     
    #--------------------------------------------------------------------------
    #input : none
    #function: controll for type game option
    #output:none 
    def type_game_menu(self):
        option = ""
        while option != "4":
            option = self.view.view_type_game_menu()
            if option == "1":
                option = "4"
                self.set_game_mode(0)
            
            elif option == "2":
                option = "4"
                self.set_game_mode(1)
                
            elif option == "3":
                option = "4"
                self.set_game_mode(2)               
                
            elif option == "4":
                self.view.clear_console()
                
            else:
                self.view.invalid_option()

    #--------------------------------------------------------------------------
    #input : none
    #function: show how to play the game
    #output:none
    def how_to_play(self):
        self.view.view_how_to_play()
        self.view.clear_console()
    
    #--------------------------------------------------------------------------
    #input : none
    #function: controll for the main menu option
    #output:none
    def main_menu(self):
        
        option = ""
        while option != "3":
            option = self.view.view_main_menu()
            if option == "1":
                self.new_game_menu()
            
            elif option == "2":
                self.how_to_play()
                
            elif option == "3":
                self.view.clear_console()
                
            else:
                self.view.invalid_option()   

    #--------------------------------------------------------------------------
    #input : player_type1 and player_type2 are string
    #function: create two humans players
    #output: a list with two human players
    def h_vs_h(self, player_type1, player_type2):
        players = list()
        P1name = self.view.input_option("Enter " +player_type1+"'s name: ")
        players.append(Player('1', P1name))
        P2name = self.view.input_option("Enter " +player_type2+"'s name: ")
        players.append(Player('2', P2name))
        return players
    
    #--------------------------------------------------------------------------
    #input : player_type1 and player_type2 are string
    #function: create two computer agents 
    #output: a list with two computer agents 
    def c_vs_c(self, player_type1, player_type2):
        players = list()
        P1name = self.view.input_option("Enter " +player_type1+"'s name: ")
        players.append(Agent('1', P1name,0,0,0,0))
        P2name = self.view.input_option("Enter " +player_type2+"'s name: ")
        players.append(Agent('2', P2name,0,0,0,0))
        return players
    
    #--------------------------------------------------------------------------
    #input : player_type1 and player_type2 are string
    #function: create a human player and a computer agent 
    #output: a list witha player and an agent 
    def h_vs_c(self, player_type1, player_type2):
        players = list()
        P1name = self.view.input_option("Enter " +player_type1+"'s name: ")
        players.append(Player('1', P1name))
        P2name = self.view.input_option("Enter " +player_type2+"'s name: ")
        players.append(Agent('2', P2name,0,0,0,0))
        return players
    
    #--------------------------------------------------------------------------
    #input : none
    #function: according to the game mode
    #output: a list with the  players  
    def create_players(self):
        self.view.view_title()
        if self.game_mode == self.game_modes[0]:
            return self.c_vs_c("Computer1","Computer2")
        elif self.game_mode == self.game_modes[1]:
            return self.h_vs_h("Human1","Human2")
        elif self.game_mode == self.game_modes[2]:
            return self.h_vs_c("Human","Computer")

    #--------------------------------------------------------------------------
    #input : a players list, an int with the actual player
    #function: show the winner player
    #output:none
    def show_winner(self, players, actual):
        if actual:
            self.view.player2_wins("bright", "", "cyan")
        else:
            self.view.player1_wins("bright", "", "cyan")
        players[actual].add_win()
        players[not actual].add_lose()
        print("{} is the winner".format(players[actual].name))
        players[actual].print_record()
        players[not actual].print_record()
     
    #--------------------------------------------------------------------------
    #input : a players list, an int with the actual player
    #function: show draw message, and add the values draw
    #output:none
    def draw(self, players, actual):
        self.view.view_draw()
        players[actual].add_draw()
        players[not actual].add_draw()
        players[actual].print_record()
        players[not actual].print_record()
        
    #--------------------------------------------------------------------------
    #input : a players list, an int with the actual player
    #function: determine if the game ended or not
    #output:boolean value
    def ended_game(self, players, actual):
        if self.checker.check_win(self.board, self.board.last_column, players[actual].character):
            self.show_winner(players, actual)
            return True
        elif not(self.board.have_legal_move()):
            self.draw(players, actual)
            return True
        return False        
    
    #--------------------------------------------------------------------------
    #input : a players list, an int with the actual player
    #function: ask for the human player's column number
    #output: 
    def human_request_column(self, players, actual):
        column = -2
        try:
            column = int(self.view.input_option(">>>> {} select a column's number: ".format(players[actual].name)))
        except ValueError:
            column = -2
            self.view.alert("invalid move ! D:")
        return column
    
    #--------------------------------------------------------------------------
    #input : a players list, an int with the actual player
    #function: ask for the player's column number
    #output: an int with column number > 0
    def request_column(self, players, actual):
        if type(players[actual]) is Agent:
            players[actual].throw_die()
            return players[actual].select_move(self.board,self.level, players[not actual].character)
        elif type(players[actual]) is Player:
            return self.human_request_column(players, actual)
        return -2
    
    #--------------------------------------------------------------------------
    #input : player's index 
    #function: change the player in turn
    #output: 1 or 0
    def change_turn(self, Actual):
        return not(Actual)
    
    #--------------------------------------------------------------------------
    #input : none
    #function: create players and start the game 
    #output: none
    def start_game(self):
        players = self.create_players()
        play_again = "y"

        while play_again != "n":
            
            self.default()
            self.play(players)
            play_again =  self.view.input_option(">>>> Do you want to play again?[y/n]: ")  
            
    #--------------------------------------------------------------------------
    #input : a list with two players
    #function: to control the normal execution of the game
    #output: a list with two players
    def play(self, players):
        actual = 0
        self.view.view_title()
        self.board_printer.print_board(self.board)
        
        column = self.request_column(players, actual)
        while( column  != -1):
            self.view.view_title()

            if self.board.insert_value(column, players[actual].character):
                self.board_printer.print_board(self.board)
                if self.ended_game(players, actual):
                    return players
                actual = self.change_turn(actual)

            else:
                self.board_printer.print_board(self.board)
                self.view.invalid_option()
            column = self.request_column(players, actual)
        
        return players
            

            