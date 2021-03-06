from BoardPrinter.BoardPrinter import BoardPrinter
from Connect4View.Connect4View import Connect4View
from WinAndBlock.WinAndBlock import Checker
from Player.Player import Player
from Agent.Agent import Agent
from Board.Board import Board
#from GeneticTrainer.GeneticTrainer import GeneticTrainer

# class to control all game's logic
class Connect4():
    
    #--------------------------------------------------------------------------

    def __init__(self,system):
        """
        input : a string, 'cls' i for windows and 'clear' for ubunrun or other
        function: constructor
        """
        self.board =  None
        self.system = system
        self.board_printer = None
        self.view = Connect4View(system)
        self.checker = Checker()
        self.game_modes = ["c_vs_c", "h_vs_h", "h_vs_c"]
        self.game_mode = self.game_modes[1]
        self.level = 1
        
    #--------------------------------------------------------------------------
        
    def default(self):
        """
            input : None
            function: Create a game environment for default
            output: None
        """
        self.board =  Board(6,7)
        self.board.create()
        self.board_printer = BoardPrinter(self.system,"bringht", "", "white")
        self.board_printer.load_boar(self.board.column_size)        

    def new_game_menu(self):
        """
            input : None
            function: Displays the Game Menu ask the user which option to choose
            output:None  
        """
        option = ""
        while option != "5":
            option = self.view.view_new_game_menu()
            if option == "1":
                self.type_game_menu()
            
            elif option == "2":
                self.level = self.select_level()
                
            elif option == "3":
                self.training_computer()
                
            elif option == "4":
                self.start_game()
                
            elif option == "5":
                self.view.clear_console()
                
            else:
                self.view.invalid_option()
  
    def select_level(self):
        """
        input : None
        function: Asks the user to the level(depth) the computer will have
        output: None
        """
        self.view.view_title()
        level = self.view.select_level()
        if level >= 1 and level <= 4:
            return level
        else:
            self.view.invalid_option()
            return self.select_level()    
        
    #--------------------------------------------------------------------------

    def set_game_mode(self,mode):
        """
        input : Sets the game mode from the game_modes array
        output: None
        """
        self.game_mode = self.game_modes[mode]
     
    #--------------------------------------------------------------------------

    def type_game_menu(self):
        """    
        input: None
        function: Displays the Game Menu, asks which mode to play
            h vs h, h vs c, c vs c
        output: None
        """         
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

    def how_to_play(self):
        """
        input : None
        function: Displays the how to play guide
        output: None
        """
        
        self.view.view_how_to_play()
        self.view.clear_console()
    
    #--------------------------------------------------------------------------

    def main_menu(self):
        """
            input: None
            function: Displays the Main Menu, ask if play new game, show how to 
            play or exit the game
            output: None
        """
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

    def training_computer(self):
        """
            input: none
            function: get the training
            return: None
        """
        self.view.view_title()
        self.view.print_message("normal","", "white",">>> Please waiting for the training end ....")
        preserve = int(self.view.input_option(">>> How many Agents will preserve each generation while training?: "))
        generations = int(self.view.input_option(">>> How many generations will be trained?: "))
        #trainer = GeneticTrainer(preserve, generations)
        #params = trainer.get_best_configuration_params()
        #training = str(params[0]) + ", "+ str(params[1]) + ", " + str(params[2]) + ", " + str(params[3])
        training = "0.21, 0.47, 0.65, 0.94"
        self.view.print_message("normal","", "white",">>> Please copy the following text and save it: " + training)
        self.view.input_option(">>> Back [type enter]: ")

    #-------------------------------------------------------------------------

    def get_computer_parameters(self):
        """
            input: none
            functions: get values from console for computer agent
            return: None
        """
        parameters = self.view.input_option(">>>> Please enter the parameters for computer (p1, p2,p3,p4): ")
        values =[]
        for porcent in parameters.split(","):
            values.append(float(porcent))
        return values

    #--------------------------------------------------------------------------

    def h_vs_h(self, player_type1, player_type2):
        """
            input : player_type1 and player_type2 are string
            function: Sets the game to play human vs human 
            output: a list with two human players
        """
        players = list()
        P1name = self.view.input_option("Enter " +player_type1+"'s name: ")
        players.append(Player('1', P1name))
        P2name = self.view.input_option("Enter " +player_type2+"'s name: ")
        players.append(Player('2', P2name))
        return players
    
    #--------------------------------------------------------------------------

    def c_vs_c(self, player_type1, player_type2):
        """
            input : player_type1 and player_type2 are string
            function: Sets the game to play computer vs computer 
            output: a list with two computer agents 
        """
        players = list()
        P1name = self.view.input_option("Enter " +player_type1+"'s name: ")
        p = self.get_computer_parameters()
        players.append(Agent('1', P1name,p[0],p[1],p[2], p[3]))
        P2name = self.view.input_option("Enter " +player_type2+"'s name: ")
        p = self.get_computer_parameters()
        players.append(Agent('2', P2name,p[0],p[1],p[2], p[3]))
        return players
    
    #--------------------------------------------------------------------------

    def h_vs_c(self, player_type1, player_type2):
        """
            input : player_type1 and player_type2 are string
            function: Sets the game to play human vs computer
            output: a list witha player and an agent 
        """
        players = list()
        P1name = self.view.input_option("Enter " +player_type1+"'s name: ")
        players.append(Player('1', P1name))
        P2name = self.view.input_option("Enter " +player_type2+"'s name: ")
        p = self.get_computer_parameters()
        players.append(Agent('2', P2name,p[0],p[1],p[2], p[3]))
        return players

    #--------------------------------------------------------------------------

    def create_players(self):
        """
        input : none
        function: From the game mode decided by the user creates the Players
        output: a list with the  players  
        """
        self.view.view_title()
        if self.game_mode == self.game_modes[0]:
            return self.c_vs_c("Computer1","Computer2")
        elif self.game_mode == self.game_modes[1]:
            return self.h_vs_h("Human1","Human2")
        elif self.game_mode == self.game_modes[2]:
            return self.h_vs_c("Human","Computer")




    #--------------------------------------------------------------------------

    def winner(self, players, actual):
        """
        input : a players list, an int with the actual player
        function: add the values winner
        output:none
        """

        players[actual].add_win()
        players[not actual].add_lose()
        players[actual].print_record()
        players[not actual].print_record()
    #--------------------------------------------------------------------------

    def show_winner(self, players, actual):
        """
            input : a players list, an int with the actual player
            function: Displays the winner of the game and each player record
            output:none
        """
        
        if actual:
            self.view.player2_wins("bright", "", "cyan")
        else:
            self.view.player1_wins("bright", "", "cyan")
        self.view.print_players_names(players[0].name, players[1].name)     
        self.board_printer.print_board(self.board)
        self.winner(players, actual)




    #--------------------------------------------------------------------------

    def draw(self, players, actual):
        """   
        input : a players list, an int with the actual player
        function:  add the values draw
        output:none
        """
        players[actual].add_draw()
        players[not actual].add_draw()
        players[actual].print_record()
        players[not actual].print_record()
             
    #--------------------------------------------------------------------------

    def show_draw(self, players, actual):
        """   
            input: a players list, an int with the actual player
            function: Displays a draw title and update players record
            output: None
        """
        self.view.view_draw()
        self.board_printer.print_board(self.board)
        self.draw(players, actual)


    #--------------------------------------------------------------------------

    def ended_game(self, players, actual):
        """
        input : a players list, an int with the actual player
        function: Checks if one player have won or if there are no more moves played
        output: Boolean value
        """
        if self.checker.check_win(self.board, self.board.last_column, 
                                            players[actual].character):
            self.winner(players, actual)
            return True
        elif not(self.board.have_legal_move()):
            self.draw(players, actual)
            return True
        return False  
    #--------------------------------------------------------------------------

    def show_ended_game(self, players, actual):
        """
        input : a players list, an int with the actual player
        function: determine if the game ended or not
        output:boolean value
            Checks if one player have won or if there are no more moves played
        """
        if self.checker.check_win(self.board, self.board.last_column, 
                                            players[actual].character):
            self.show_winner(players, actual)
            return True
        elif not(self.board.have_legal_move()):
            self.show_draw(players, actual)
            return True
        return False        
    
    #--------------------------------------------------------------------------

    def human_request_column(self, players, actual):
        """
            function: Request a column to a human user
            output: column selected value
        """
        column = -2
        try:
            column = int(self.view.input_option
             (">>>> {} select a column's number: ".format(players[actual].name)))
        except ValueError:
            column = -2
            self.view.alert("invalid move ! D:")
        return column

    #--------------------------------------------------------------------------

    def computer_request_column(self, players, actual):
        """
        input : a players list, an int with the actual player
        function: ask for the computer player's column number
        output:
            Request a column to a human user
        """
        self.view.print_message("normal", "", "white",
          ">>> Waiting for {}'s answer... ".format(players[actual].name) )
        move = players[actual].next_move(self.board, players, actual,self.level)
        self.view.print_message("normal", "", "white",">>> Selected column: "+str(move))
        self.view.input_option(">>> Press enter to continue: ")
        return move
    
    #--------------------------------------------------------------------------

    def request_column(self, players, actual):
        """
            input : a players list, an int with the actual player
            function: checks which player is to play, if it is human ask for a
            column if it is a computer calls the next_move function
            output: an int with column number > 0
        """
        if type(players[actual]) is Agent:
            return self.computer_request_column(players, actual)

        elif type(players[actual]) is Player:
            return self.human_request_column(players, actual)
        return -2
    
    #--------------------------------------------------------------------------

    def change_turn(self, Actual):
        """
            input : player's index 
            function: change the player in turn
            output: 1 or 0
        """
        
        return not(Actual)
    
    #--------------------------------------------------------------------------

    def start_game(self):
        """
            input : None
            function: Stars the game, it holds the game's playing cyclo until 
            the player types "n"
            output: None
        """
        players = self.create_players()
        play_again = "y"

        while play_again != "n":
            
            self.default()
            self.play(players)
            play_again =  self.view.input_option(">>>> Do you want to play again?[y/n]: ")  
            
    #--------------------------------------------------------------------------

    def play(self, players):
        """
            input : a list with two players
            function: Single game, playing cyclo, it asks for the column, 
            inserts the disc checks for, checks if win, change turn, and 
            repeat the cyclo
            output: a list with two players
        """
        actual = 0
        self.view.view_title()
        self.view.print_players_names(players[0].name, players[1].name)
        self.board_printer.print_board(self.board)
        
        column = self.request_column(players, actual)
        while column  != -1:
            self.view.view_title()
            self.view.print_players_names(players[0].name, players[1].name)
            
            if self.board.insert_value(column, players[actual].character):
                self.board_printer.print_board(self.board)
                players[actual].insert_move(column)
                if self.show_ended_game(players, actual):
                    return players
                actual = self.change_turn(actual)

            else:
                self.board_printer.print_board(self.board)
                self.view.invalid_option()
            column = self.request_column(players, actual)
            
        return players
    
    
    #--------------------------------------------------------------------------

    def logic_play(self, players):
        """
        input : a list with two players
        function: to control the normal execution of the game for computers 
        output: a list with two players
            Single game, playing cyclo, it asks for the column, inserts the 
            disc checks for, checks if win, change turn, and repeat the cyclo
        """
        actual = 0
        
        column = players[actual].next_move(self.board, players, actual, depth_max=self.level)
        while column  != -1:
            
            if self.board.insert_value(column, players[actual].character):
                if self.show_ended_game(players, actual):
                    return players
                actual = self.change_turn(actual)

            column = players[actual].next_move(self.board, players, actual, depth_max=self.level)
            
        return players    