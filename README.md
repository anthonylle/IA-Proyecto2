![Imgur](https://i.imgur.com/E8Ta3b1.png)

Instituto Tecnológico de Costa Rica 	      
Escuela de Ingeniería en Computación       
Curso: Inteligencia Artificial	      
Semestre 2 - 2018		 	      
Proyecto II 			      
Estudiantes: 			      
* Diego Tenorio Solís 	      
* Jake Herrera Hernández 		      
* Anthony Leandro Miranda

##### Repositorio se puede encontrar en el [siguiente enlace](https://github.com/anthonylle/IA-Proyecto2)
------------------------------------------------
------------------------------------------------
# Estrategia de Solución
------------------------------------------------
Para la realización de este proyecto se decidió dividirlo en distintos módulos para un mayor orden y facilidad de uso, los cuales se explicarán a continuación

```py
Main.py

def main():
"""
    Calls the game main function(Connect4)
    return: None
"""
```
```py
WinAndBlock.py

class Checker():
    def check(self, connect4, board, players, actual):
        """
            Checks if the actual player in the actual board can win
            and returns the respective column number 
        """
        
    def set_player_value(self, players, actual):
        """
            it is used in the children functions to check if it is looking
            for actual player win or actual player lose
            Returns the payer value to look up
        """
    
    def check_win(self, board, col, player_value):
        """
            Main function to check if the player given can win in the 
            actual board
            Returns True or False
        """
        
    def check_lines(self, board, player_value, next_discs):
        """
            Main check lines function which returns how many verticals, 
            horizontals and diagonals there are of the actual player 
            in the actual board, of an x number of discs limit,
            it recovers the entire board
        """
        
    def check_verticals(self, board, col, player_value):
        """
            it returns True if there are 4 vertical discs in the given column
            False if not
        """
    
    def check_verticals_count(self, board, row, col, player_value, next_discs):
        """
            returns 1 if there are x or more discs in a vertical row 
            0 if not
        """
    
    def check_horizontals(self, board, col, player_value):
        """
            it checks if there are 4 horizontals discs in a row
            returns True if so, else False
            it checks to right and left from the last disc inserted 
            in the board, variations of Breadth-first search
        """
    
    def _check_horizontals(self, board, col, row, player_value, look_right):
        """
            Auxiliar recurcive function, returns the amount of horizontal
            discs in a row to left or right from the col and row 
            possition given
        """
    
    def check_horizontals_count(self,board,row,col,player_value,next_discs):
        """
            check if there are x discs count next to the row, col given
            Returns True of False, uses Breadth-first search
        """
    
    def _check_horizontals_count(self,board,col,row,player_value,look_right,next_discs):
        """
            Auxiliar recursive function returns the amount of horizontal
            discs to left or right from the col,row  given even if there
            are empty squares in the way
        """
        
    def check_diagonals(self, board, col, player_value):
        """
            it checks if there are 4 diagonals discs in a row
            returns True if so, else False
            it checks to up and down from the last disc inserted
            in the board, variation of Breadth-first search
            uses the transposed matrix to check 2 types of diagonals
        """
    
    def _check_diagonals(self, board, col, row, player_value, look_up):
        """
            Auxiliar recurcive function, returns the amount of diagonals
            discs in a row to up or down from the col and row 
            possition given
        """
    
    def check_diagonals_count(self, board, row, col, player_value, next_discs):
        """
            check if there are x discs count in diagonal next to the row,col 
            given, returns 0,1 or 2, 2 if there are x discs in both diagonals
            uses Breadth-first search
        """
    
    def _check_diagonals_count(self,board,row,col,player_value,next_discs,identity):
        """
            returns the amount of discs next to the row,col given in diagonal
            uses Breadth-first search
        """
    
    def __check_diagonals_count(self, board, col, row, player_value, look_up):
        """
            Auxiliar recursive function returns the amount of diagonals
            discs to up or down from the col,row  given even if there
            are empty squares in the way
        """
        
#----------------------------------------------------------------
class Win_Checker(Checker):
    def set_player_value(self, players, actual):
        """
            Overwrited funtion, to check the actual players win
        """
        
#-------------------------------------------------------------
class Block_Checker(Checker):
    def set_player_value(self, players, actual):
        """
            Overwrited funtion, to check the oponents win
        """

#-------------------------------------------------------------
class Secuential_Count_Checker(Checker):
    def check_lines(self, board, player_value, next_discs):
        """
            Overwrited function, deffers from its father in calling 
            check_diagonals instead of check_diagonals_count
        """
        
    def check_horizontals_count(self,board,row,col,player_value,next_discs):
        """
            Overwrited function it differs from it father when asign discs = 1
            insted of discs = 0
        """
    
    def check_diagonals(self, board, row, col, player_value, next_discs):
        """
            Overwrited function it differs from it father when asign discs = 1
            insted of discs = 0
        """

#-------------------------------------------------------------
class Block_3_In_Line_Checker(Checker):
    def check_verticals_count(self,board,row,col,player_value,next_discs):
        """
            returns 1 if there are x or more discs in a vertical row 
            with a block at the begining
        """
    
    def check_horizontals_count(self,board,row,col,player_value,next_discs):
        """
            checks if there are x discs count next to the row, with at least
            one actual player disc in the row, to seach blocks
        """
    
    def _check_horizontals_count(self,board,col,row,player_value,look_right,next_discs,oponent):
        """
            Auxiliar recursive function returns the amount of horizontal
            discs to left or right from the col,row  given even if there
            are empty squares in the way, it have the oponent option to 
            look for oponent or actual player discs 
        """
    
    def check_diagonals_count(self, board, row, col, player_value, next_discs):
        """
            check if there are x discs count in diagonal next to the row,col 
            given, returns 0,1 or 2, 2 if there are x discs in both diagonals
            with at least one actual player discs in the middle
        """
    
    def _check_diagonals_count(self,board,row,col,player_value,next_discs,identity):
        """
            returns the amount of discs next to the row,col given in diagonal
            looks for oponent discs and players discs
        """
    
    def __check_diagonals_count(self, board, col, row, player_value, next_discs, look_up, oponent):
        """
            Auxiliar recursive function returns the amount of diagonals
            discs to up or down from the col,row  given even if there
            are empty squares in the way, also looks for oponent discs or 
            players discs
        """
```
```py
Player.py

class Player():
    def add_win(self):
    """
        input : none
        function: add one to wins
        output: none
    """

    def add_lose(self):
        """
            input : none
            function: add one to lose
            output: none    
        """
    
    def add_draw(self):
        """
            input : none
            function: add one to draw
            output: none   
        """
    
    def print_record(self):
        """
            input: none
            function: Prints the Record of a Player
                    e.g record=[2,1,0]
                    Player Record: Wins: 2 | Losses: 1 | draws: 0
            output: none
        """
```
```py
MiniMax.py

class MiniMax():
    def search_best_move(self, state_board, board_area):
        """
            function: Looks for the best move to take, it calls min_value
            with all the columns then decides the best move amongst then
            output: an int with best 
        """
    
    def check_state(self, board, depth, player):
        """
            function checks if there's a win, no more legal moves or the depth
            has come to 0
            output: boolean
        """
    
    def heuristic(self, state_board):
        """
            function: Fathers Model funtion
            output: 0
        """

    def min_value(self, depth, state_board, alfa, beta):
        """
            function: search the best value for the human(oponent) the worse 
            for the computer
            output: int value, the least between alfa and beta 
        """
    def max_value(self, depth, state_board, alfa, beta):
        """
            function: search the best value for the computer and the worse for the human (oponent)
            output: int value, the higher bwtween alpha and beta   
        """
    
    def print_state(self, depth, board):
        """
            function: Prints the actual depth and matrix
            output: None
        """

#-------------------------------------------------------------
class Secuential(MiniMax):
    def heuristic(self, state_board):
        """
        fucntion: Overwrites heuristic function, it gives a 100000 weight to 4 in line
        discs, 100 to 3 in line discs and 1 to the 2 in line discs, then
        returns the sum of them all, if the oponent haves 4 in line returns
        -100000
        output: weight calculated
        """

#-------------------------------------------------------------
class Block_3_In_Line(MiniMax):
    def heuristic(self, state_board):
        """
        function: Overwrites heuristic function, it gives a 1000 weight to 3 in line
        discs blocked, 100 to 2 in line with discs blocked and 150 to the 4 
        in line with discs blocked, then returns the sum of them all, if the 
        oponent haves 4 in line returns -100000 
        output: weight calculated
        """

#-------------------------------------------------------------
class Espaces(MiniMax):
    def heuristic(self, state_board):
        """
        function: Overwrites heuristic function, it gives a 100000 weight to 4 in line
        discs, 100 to 3 in line with spaces discs and 1 to the 2 in line with 
        spaces discs, then returns the sum of them all, if the oponent haves 
        4 in line returns -100000 
        output: weight calculated
        """

#-------------------------------------------------------------
class Play_3_In_Line(MiniMax):
    def heuristic(self, state_board):
        """
        function: Overwrites heuristic function, it gives a 1000 weight to 3 in line
        discs blocked, 100 to 2 in line with discs blocked and 150 to the 4 
        in line with discs blocked, then returns the sum of them all, if the 
        oponent haves 4 in line returns -100000 
        output: weight calculated
        """
```
```py
MessagePrinter.py

class MessagePrinter(ConsoleControl):
    def input_option(self, message):
        """
            function: get a input value from the console, prints a message 
            in yellow color
            output: a string value
        """
    def alert(self, message):
        """
            function: Prints an alert message in red
            output: none
        """
    def print_message(self, style, back, fore, message):
        """
            function: prints a message in console, with a specific style
            output: none       
        """
    
    def clear_print(self, style, back, fore, message):                  
        """
            function: Clears the console and then prints the message given with stile a specific style, 
            #output: none 
        """  
        
    def print_without_end(self, color, message):
        """
        function: prints without carriage return '\n'
        return: none
        """
    
```
```py
ConsoleControl.py

class ConsoleControl(object):
    def fore_color(self, color = "reset"):
        """
            function: choose the letter's color
            output: none    
        """
    
    def back_color(self, color = "reset"):
        """
          function: Chooses the backgrond's color in line console
          output: none 
        """
    
    def style_selector(self, style = "reset"):
        """
        #function: Chooses the letter's style
        #output: none     
        """
    def font_selector(self, style, back, fore):
        """
            function: set style for console's line
            output: none
        """
    def clear_console(self):
        """
            function: clear all the console
            output: none  
        """
    def cursor_position(self, row, column):
        """
            function: set the cursor's position in the console
            output: none
        """
        
    def cursor_position2(self, row, column):
        """
            function: set the cursor's position in the console
            output: none   
        """
        
    def reset_all(self):
        """
            input : none
            function: set the original console's style
            output: none    
        """
```
```py
Connect4VIew.py

class Connect4View(MessagePrinter):
    def view_title(self):
        """
            function: Prints the Connect4 title
            output: None
        """

    def view_winner(self):
        """
           funtion: Prints You've Von title
           output: None
        """
    
    def view_lost(self):
        """
            function: Prints You've Lost title
            output: None
        """

    def view_draw(self):
        """
            function: Prints Draw title
            output: None
        """
    
    def view_menu(self, menu, space):
        """
            function: Prints in console the menu title
            output: None
        """

    def view_main_menu(self):
        """
            function: prints the main menu
            output: None
        """

    def view_new_game_menu(self):
        """
            function: Prints the new menu title
            output: None
        """

    def view_type_game_menu(self):
        """
            function: Prints type of the game menu
            output: None
        """

    def view_how_to_play(self):
        """
            function: Prints how to play menu
            output: None
        """
        
    def column_option(self):
        """
            function: Prints select a number column input
            output: None
        """
    
    def select_level(self):
        """
            function: Prints select level input
            output: None
        """
    
    def invalid_option(self):
        """
            function: Prints in red invalid option
            outpu: None
        """

    def player1_wins(self, style, back, fore):
        """
            function: Prints Player2 Wins title
            output: None 
        """

    def player2_wins(self, style, back, fore):
        """
            function: Prints Player2 Wins title
            output: None 
        """
    
    def print_players_names(self, p1_name, p2_name):
        """
            function: print in console the players's names
            output: None        
        """
```
```py
Connect4.py
    
class Connect4():
    def default(self):
        """
            function: Create a game environment for default
            output: None
        """
        
    def new_game_menu(self):
        """
            function: Displays the Game Menu ask the user which option to choose
            output:None  
        """
    
    def select_level(self):
        """
        function: Asks the user to the level(depth) the computer will have
        output: None
        """

    def set_game_mode(self,mode):
        """
        function : Sets the game mode from the game_modes array
        output: None
        """

    def type_game_menu(self):
        """    
        function: Displays the Game Menu, asks which mode to play
                  h vs h, h vs c, c vs c
        output: None
        """ 
    
    def how_to_play(self):
        """
        function: Displays the how to play guide
        output: None
        """
        
    def main_menu(self):
        """
        function: Displays the Main Menu, ask if play new game, show how to 
        play or exit the game
        output: None
        """

    def training_computer(self):
        """
        input: none
        function: get the training
        return: None
        """

    def get_computer_parameters(self):
        """
            input: none
            functions: get values from console for computer agent
            return: None
        """
    
    def h_vs_h(self, player_type1, player_type2):
        """
            function: Sets the game to play human vs human 
            output: a list with two human players
        """
    
    def c_vs_c(self, player_type1, player_type2):
        """
        function: Sets the game to play computer vs computer 
        output: a list with two computer agents 
        """

    def h_vs_c(self, player_type1, player_type2):
        """
            function: Sets the game to play human vs computer
            output: a list witha player and an agent 
        """
    
    def create_players(self):
        """
            function: From the game mode decided by the user creates the Players
            output: a list with the  players  
        """

    def show_winner(self, players, actual):
        """
            function: Displays the winner of the game and each player record
            output:none
        """
    
    def draw(self, players, actual):
        """   
            function: Displays a draw title and update players record
            output: None
        """

    def ended_game(self, players, actual):
        """
            function: Checks if one player have won or if there are no more moves played
            output: Boolean value
        """
        
    def human_request_column(self, players, actual):
        """
            function: Request a column to a human user
            output: column selected value
        """

    def request_column(self, players, actual):
        """
            function: checks which player is to play, if it is human ask for a
            column if it is a computer calls the next_move function
            output: an int with column number > 0
        """
    
    def change_turn(self, Actual):
        """
            function: change the player in turn
            output: 1 or 0
        """
    
    def start_game(self):
        """
            function: Stars the game, it holds the game's playing cyclo until 
            the player types "n"
            output: None
        """

    def play(self, players):
        """
            function: Single game, playing cyclo, it asks for the column, 
            inserts the disc checks for, checks if win, change turn, and 
            repeat the cyclo
            output: a list with two players
        """
```
```py
BoardPrinter.py

class BoardPrinter(ConsoleControl):
    def creat_divider(self, column_size):
        """
            function: Creates the divisions (═ + ╬  + ═)*columns+ ╣ = ═╬═╬═╬═╣
            output: None
        """

    def create_footer(self, column_size):
        """
            function: Creates the footer
            ╚ + (═*3 + ╩)*columns-1 + ═*3 + ╝ = ╚═══╩═══╩═══╩═══╝ 
            output: None 
        """
    
    def create_header(self,column_size):
        """
            function: Creates the header 
            "  " ═ + (╬ + ═*3)*columns + ╗  =         1   2   3
                                                "  ═╬═══╬═══╬═══╗"
            output: None
        """

    def load_boar(self,column_size):
        """
            function: It prepares the divider, footer and headers class to 
            print the board
            output: None
        """
    
    def generate_board_string(self, board):
        """
            function: read the board and create the board view
            output: A String with the board view
        """

    def print_board(self, board):
        """
            function: Prints the board view
            output: None
        """
```
```py
Board.py

class Board():
def copy(self):
        """
            function: Creates a copy of the actual board
            output: new board object 
        """        

    def create(self):
        """
            function: create a this matrix a fill its rows
            output: none
        """
        
    def  insert_value(self, column_number, value):
        """
            function: verify if column number is into the range 
            output: a boolean value, true is insert is ok and false if no     
        """

    def insert_aux(self, column_number, value):
        """
            function: insert a new value in the board, and update 
            moves_count and last move
            output: a boolean value, true is insert is ok and false if no   
        """ 

    def is_column_full(self, column_number):
        """
            function: verify if the i column is full or not
            output: true if is full or false if it has at least a space
        """ 
    
    def have_legal_move(self):
        """
            function: Checks if moves_count have reach the maximun number allow
            output: true if it has a space or false if it has not a space 
        """

    def getAt(self, row, col):
        """
            function: Returns the value in the row,col position
            output: specifict space in the board    
        """

    def get_highest_disc(self, col, player_value):
        """
            function: returns the row value where it finds the first apereance
            of the player value
            output: int value, -1 if the column is empty or other if not
        """

    def get_lowest_disc(self, col, player_value):
        """
            function: Return the row value where it finds the first apereance
            of the player value, from button to top, mainly used by transposed board
            output: int value, -1 if the column is empty or other if not
        """

    def get_diagonal_border(self, row, col):
        """
            function: Returns the fist diagonal position
            output: two int values    
        """

    def get_transposed(self):
        """
            function: Creates a copy of the board and invertes it
            output:  a Board object 
        """

    def setAt(self, row, col, value):
        """
            function: Sets the a value of the row and col given
            output: true if all is ok or false if it isn't
        """
        
        def print_matrix(self):
        """
            function: Prints the matrix to have a perspective of it's actual state
            output: None
        """
```
```py
Agent.py

class Agent(Player):
    def throw_die(self):
        """
            function: throw_die for a new percent
            output: None
        """ 
    
    def select_move(self, board_state,depth_max, oponent):
        """
            function: Select the best move using minimax
            output: Int with column number > 0     
        """

    def next_move(self, board, players, actual):
        """
            function: Checks if it can win, block or make a move from the strategies
            output: column move chosen
        """
```
------------------------------------------------
# Sudocódigo de funciones
### Gane y Bloqueo
#### Checker
##### Funcion principal, revisa si hay un gane en las verticales, horizontales o diagonales
```
class Checker()
    function chec*(board, players, actual) returns column to win or block
        copy <- board.get_copy()
        for col in range(copy.column_size)
            player_value_to_look <- get_player_value(players, actual)
            copy.insert_disc(col, player_value_to_look)
            if check_win(copy, col, player_value_to_look)
                return col
            copy.remove_disc_at(row, col)
        return -1
        
    function get_player_value(players, actual) returns the players value to look up
        return "1"
    
    function check_win(board, col, player_value) returns true if a 4 in line is found
        return check_verticals(board, col, player_value) or 
               check_horizontals(board, col, player_value) or
               check_diagonals(board, col, player_value)
    
    function check_verticals(board, col, player_value) returns true if vertical 4 in line is found
        four_in_a_row <- False
        highest_disc <- board.get_highest_disc(col)
        if (highest_disc <= 2)
            for row in range(highest_disc, highest_disc+4)
                if board.get_value_at(row, col) != player_value
                    break
                else if row == highest_disc+3
                    four_in_a_row <- True
        return four_in_a_row
    
    function check_horizontals(board, col, player_value)returns true if 4 in horizontal row found
            discs <- 1 #my actual disc
            highest_disc_row <- board.get_highest_disc(col, player_value)
            discs += aux_check_horizontals(board, col+1, highest_disc_row, player_value, True)
            discs += aux_check_horizontals(board, col-1, highest_disc_row, player_value, False)
        return discs >= 4
    
    function aux_check_horizontals(board, col, row, player_value, look_right) returns discs in sequence found at right or left
        if col >= 0 and col < board.column_size:
            if look_right
                if board.get_value_at(row, col) == player_value
                    return 1 + aux_check_horizontals(board, col+1, row,
                                                player_value, look_right)
            else
                if board.get_value_at(row, col) == player_value
                    return 1 + aux_check_horizontals(board, col-1, row, 
                                                player_value, look_right)
        return 0
    
    function check_diagonals(board, col, player_value) returns if there are 4 in a diagonal row
        discs <- 1  #Actual disc
        discsT <- 1 #Actual disc
        inverted_matrix <- board.get_inverted_matrix() #to check the other diagonal
        highest_disc_row <- board.get_highest_disc(col, player_value)
        lowest_disc_row_t <- inverted_matrix.get_lowest_disc(col, player_value)
        discs  += aux_check_diagonals(board, col-1, highest_disc_row-1, player_value, True)
        discs  += aux_check_diagonals(board, col+1, highest_disc_row+1, player_value, False)
        discsT += aux_check_diagonals(inverted_matrix, col-1,lowest_disc_row_t-1, player_value, True)
        discsT += aux_check_diagonals(inverted_matrix, col+1,lowest_disc_row_t+1, player_value, False)
        return discs >= 4 or discsT>=4
        
    function aux_check_diagonals(board, col, row, player_value, look_up) returns amount of sequential discs found to up or down diagonal
        if col >= 0 and row >= 0 and col < board.column_size and row < board.row_size
        if look_up
            if board.get_value_at(row, col) == player_value
                return 1 + aux_check_diagonals(board, col-1, row-1, player_value, look_up)
        else
            if board.get_value_at(row, col) == player_value
                return 1 + aux_check_diagonals(board, col+1, row+1, player_value, look_up)
        return 0
```
#### Win_Checker
#### Clase de Gane, hereda de Checker y sobreescribe la funcion de set_player_value para que busque si hay un 4 en linea mío
```
class Win_Checker() inherits Checker
    function set_player_value(self, players, actual) returns actual player value
        return players[actual].value
```
#### Block_Checker
#### Clase de Bloqueo, hereda de Checker y sobreescribe la funcion de set_player_value para que busque si hay un 4 en linea de mi oponente
```
class Block_Checker(Checker):
    function set_player_value(self, players, actual) returns actual oponent value
        return players[not(actual)].value
```
### Algorítmo Genético
#### Generate Population
De acuerdo a un N para el tamaño de la población se crean N agentes totalmente aleatorios (nombre y parámetros aleatorios)

```
function generate_population(population_size)
    inputs
    	- population_size: amount of individuals to be created for the new population
    returns
		- a list with the randomly generated population in order to use it if required, if not, it's still kept in the
    local attribute population
    population = []
    for i <- 1 to population_size do
        Generate-a-random-seed
        first_percent <- random-value-in-range(0,0.25) with 2 decimal floating point numbers
        second_percent <- random-value-in-range(first_percent,0.5) with 2 decimal floating point numbers
        third_percent <- random-value-in-range(second_percent,0.75) with 2 decimal floating point numbers
        fourth_percent <- random-value-in-range(third_percent,1) with 2 decimal floating point numbers
        population.append(Agent("1", get-random-name(), first_percent, second_percent, third_percent, fourth_percent))
    return population
```
#### Reproduce
Este necesita de 2 Agentes (padres) que aleatoreamente serán cortados para formar 2 nuevos hijos con sus genes (parámetros)

```
function reproduce(parent1: Agent, parent2: Agent) -> [Agent, Agent]:
        inputs
        	- parent1: an Agent to generate a couple of children with another Agent
        	- parent2: an Agent to generate a couple of children with another Agent
        return 
        	- a listf of 2 children (new Agents) with the new combination of the parents (Agents) genes (params)
        """
        Generate-a-random-seed

        parent1_params <- parent1.percent_first_move, \
                         parent1.percent_second_move, \
                         parent1.percent_third_move, \
                         parent1.percent_fourth_move \

        parent2_params <- parent2.percent_first_move, \
                         parent2.percent_second_move, \
                         parent2.percent_third_move, \
                         parent2.percent_fourth_move

        index <- random-value-in-range(1, 3)
        child1_params <- parent1_params[:index] + parent2_params[index:]
        child2_params <- parent2_params[:index] + parent1_params[index:]
        child1 <- Agent("1", get-random-name(), 0, 0, 0, 0)
        child2 <- Agent("2", get-random-name(), 0, 0, 0, 0)
        child1.percent_first_move, \
        child1.percent_second_move, \
        child1.percent_third_move, \
        child1.percent_fourth_move <- child1_params

        child2.percent_first_move, \
        child2.percent_second_move, \
        child2.percent_third_move, \
        child2.percent_fourth_move <- child2_params
        return [child1, child2]
```
#### Mutate
Un individuo tiene un chance de probabilidad de mutar, y si al lanzar un dado se cumple esa probabilidad, entonces se selecciona aleatoriamente un parámetro y se muta de acuerdo al rango en el que se encuentra, para esto se necesita conocer los límites del rango tanto a la izquierda como a la derecha, por ejemplo: un 4to parámtro 0.94 puede encontrarse limitado por un 3er parámetro 0.78 y 1.0
La mutación tiene una baja probabilidad. Para este caso 8%.

```
function mutate(individual: Agent, probability) -> Agent:
    inputs
    	- individual: An Agent that can have a chance for mutating 1 of its params
    returns 
    	- the same Agent whether or not it mutates
    
    Generate-a-random-seed
    dies <- random-value-in-range(1, 100)
    if (dies <= probability) then
        index <- random-value-in(0, 3)

        current_first <- individual.percent_first_move
        current_second <- individual.percent_second_move
        current_third <- individual.percent_third_move
        current_fourth <- individual.percent_fourth_move

        percents <- [current_first, current_second, current_third, current_fourth]
        limits <- [0] + percents + [100]
        percents[index] <- random-value-in-range(limits[index], limits[index + 2]) with 2 decimal floating point numbers

        [individual.percent_first_move,
         individual.percent_second_move,
         individual.percent_third_move,
         individual.percent_fourth_move] <- percents

    return individual
```
#### Get Fitnes
Para obtener el fitness se toma en cuenta la cantidad de ganes que un individuo (agente) tiene

```
function get_fitness(individual: Agent)
    inputs
    	- individual: instance of Agent to be evaluated for a fitness measure
    returns
		- the amount of WINS the Agent already has set in its record as a fitness value
    return individual.record[individual.WINS]
```
#### Genetic Algorithm
Este se encarga de generar una población aleatoria, entrenar cada individuo y evaluar los N mejores para luego cruzarlos, mutarlos (si se da) y luego reevaluar a los nuevos individuos (niños) para saber su fitness. Cuando terminan de transcurrir las generaciones el mejor individuo (por su fitness) es seleccionado de la generación actual.

```
function genetic_algorithm():
    returns
		- the best individual from a population after N generations passed specified by its fitness function
    
    preserved_individuals = []

    for i <- 0 to number_of_generations do
        generation_fitness <- {}            
        population = generate_population((preserved_individuals_amount * 10) - size(preserved_individuals))
        population.append(preserved_individuals)
        preserved_individuals = []

        for each individual in population do
            opponents <- population.copy()
            opponents.remove(individual)
            individual <- train(individual, opponents)
            generation_fitness[individual] <- get_fitness(individual)

        best_fitting_individuals <- get_N_best_fitting(generation_fitness, preserved_individuals_amount)
        best_fitting_pairs <- make_pairs(best_fitting_individuals)
        children = []

        for each parent1, parent2 in best_fitting_pairs do
            parent1_copy <- copy.deepcopy(parent1)
            parent2_copy <- copy.deepcopy(parent2)

            children <- reproduce(parent1_copy, parent2_copy)
            children[0] = mutate(children[0], self.mutation_probability)
            children[1] = mutate(children[0], self.mutation_probability)
            preserved_individuals.append(children)
            children = []

            population.remove(parent1)
            population.remove(parent2)
            delete parent1 from generation_fitness
            delete parent2 from generation_fitness

        for each new_child in children:
            opponents = population.copy()
            opponents.remove(new_child)
            new_child = train(new_child, opponents)
            generation_fitness[new_child] = get_fitness(new_child)

    population.append(preserved_individuals) # for final iteration
    best_individual = get_N_best_fitting(generation_fitness, 1)
    return best_individual
```
#### Train

```
function train(self, individual: Agent, opponents: list):
    inputs
    	- individual: an Agent that will play against a list of Agents (opponents) in order to check the amount of wins it gets
    	- opponents: a list of Agents that will play 1 by 1 against the individual to be trained
    returns 
    	- the same individual (Agent) from the input, but 'trained'
    
    individual.character <- "1"
    for each opponent in opponents do
        opponent.character <- "2"
        players <- [individual, opponent]
        game <- new Game
        [individual, _] <- game.play(players)
    return individual

```
------------------------------------------------
# Análisis de resultados
Se mostrará el comportamiento de las pruebas unitarias y las pruebas de cobertura en el código.

### Pruebas de Pytest

MacBook-Pro-de-Anthony:IA-Proyecto2 aleandro$ pytest tests/
================================================================================ test session starts ================================================================================
platform darwin -- Python 3.6.6, pytest-3.8.2, py-1.7.0, pluggy-0.7.1
rootdir: /Users/aleandro/Documents/Tareas/IA/Proyectos/IA-Proyecto2, inifile:
plugins: remotedata-0.3.0, openfiles-0.3.0, doctestplus-0.1.3, arraydiff-0.2
collected 183 items                                                                                                                                                                 

tests/test_Agent.py ......................                                                                                                                                    [ 12%]
tests/test_Board.py ....................................................                                                                                                      [ 40%]
tests/test_Connect4.py ......                                                                                                                                                 [ 43%]
tests/test_ConsoleControl.py ...........................                                                                                                                      [ 58%]
tests/test_GeneticTrainer.py .....

### Pruebas de Coverage

----------- coverage: platform linux, python 3.6.7-final-0 -----------
Name                                             Stmts   Miss  Cover
--------------------------------------------------------------------
IA-Proyecto2/Agent/Agent.py                         84     44    48%
IA-Proyecto2/Agent/_init_.py                       0      0   100%
IA-Proyecto2/Board/Board.py                         97      4    96%
IA-Proyecto2/Board/_init_.py                       0      0   100%
IA-Proyecto2/BoardPrinter/BoardPrinter.py           55     45    18%
IA-Proyecto2/BoardPrinter/_init_.py                0      0   100%
IA-Proyecto2/Connect4/Connect4.py                  214    161    25%
IA-Proyecto2/Connect4/_init_.py                    0      0   100%
IA-Proyecto2/Connect4View/Connect4View.py           59     29    51%
IA-Proyecto2/Connect4View/_init_.py                0      0   100%
IA-Proyecto2/ConsoleControl/ConsoleControl.py       62      1    98%
IA-Proyecto2/ConsoleControl/_init_.py              0      0   100%
IA-Proyecto2/MessagePrinter/MessagesPrinter.py      26      9    65%
IA-Proyecto2/MessagePrinter/_init_.py              0      0   100%
IA-Proyecto2/MiniMax/MiniMax.py                     99     21    79%
IA-Proyecto2/MiniMax/_init_.py                     0      0   100%
IA-Proyecto2/Player/Player.py                       23      5    78%
IA-Proyecto2/Player/_init_.py                      0      0   100%
IA-Proyecto2/WinAndBlock/WinAndBlock.py            242      5    98%
IA-Proyecto2/apuntes de tablero.py                   0      0   100%
IA-Proyecto2/main.py                                 5      5     0%
IA-Proyecto2/test_setup.py                           2      0   100%
IA-Proyecto2/tests/test_Agent.py                    76      0   100%
IA-Proyecto2/tests/test_Board.py                   158      0   100%
IA-Proyecto2/tests/test_BoardPrinter.py              0      0   100%
IA-Proyecto2/tests/test_Connect4.py                 40      0   100%
IA-Proyecto2/tests/test_Connect4View.py              4      1    75%
IA-Proyecto2/tests/test_ConsoleControl.py           89      0   100%
IA-Proyecto2/tests/test_MessagePrinter.py            0      0   100%
IA-Proyecto2/tests/test_MiniMax.py                  66      4    94%
IA-Proyecto2/tests/test_Player.py                   50      0   100%
IA-Proyecto2/tests/test_WinAndBlock.py             364      0   100%
IA-Proyecto2/tests/test_main.py                      0      0   100%
--------------------------------------------------------------------
TOTAL                                             1815    334    82%

------------------------------------------------

------------------------------------------------
# Manual de Instalación

### Requisitos básicos:
- Python 3.6.7, se recomienda este enlace de [descarga](https://www.python.org/downloads/release/python-367/)

------------------------------------------------

------------------------------------------------
# Manual de Ejecución
### Requisitos básicos:
- Tener python 3 instalado en la PC

### Ejecución:
- Main Menu:
	* New Game:
	   *  Type of game: Select the game mode: computer vs computer human vs computer or human vs human
	   *  Level Game: Selects a level for the computer from 1 to 4
	   *  Training: Trains the Agent and returns the best Agents parameters
	   *  Start: Starts the game.
	        *  Enter de PLayers name, if its a computer you have to add its parameters with the format ***0.1, 0.3, 0.6, 1***
	        *  Then Star playing by selecting the column you want to move, from 1 to 7, also if you want to leave the game type ***-1***
	        *  When a player wins or there is a draw, a message pops up and display the payers record, if you don't want to play again type ***n*** else ***y*** 
	   *  Back: Redirects to the Main Menu
	* How to pLay: Display a menu of how to play the game
	* Exit: Exits the game
.

------------------------------------------------
# Distribución de notas y trabajo realizado
------------------------------------------------
### Distribución de trabajo
- Diego Tenorio:
	* Implementación de algoritmos de bloqueo y gane
	* Algoritmo general del juego
	* Implementación de estrategias nuevas
	* Documentación

- Jake Herrera :
	* Desarrollo de interfaz
	* Algoritmo general del juego
	* Implementación de estrategias nuevas
	* Documentación

- Anthony Leandro:
	* Desarrollo del algoritmo genético
	* Implementación de estrategias nuevas
	* Documentación

### Distribución de nota

Estudiante| Tenorio | Jake 	| Anthony |
---------	|---------|---------|---------|
Tareas| 		100	| 		100	| 		100	|
