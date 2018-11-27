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
------------------------------------------------
# Análisis de resultados
Se mostrará el comportamiento de las pruebas unitarias y las pruebas de cobertura en el código.

### Pruebas de Pytest

============================= test session starts =============================
platform win32 -- Python 3.6.4, pytest-3.8.2, py-1.7.0, pluggy-0.7.1
rootdir: E:\TEC\2018\II SEMESTRE\Inteligencia Artifical\Proyecto-IAMMM, inifile:
plugins: expect-1.1.0, cov-2.6.0
collected 36 items

test_arbol.py ............                                               [ 33%]
test_archivo.py ...                                                      [ 41%]
test_hoja.py ..                                                          [ 47%]
test_modelo.py ..                                                        [ 52%]
test_nodo.py .........                                                   [ 77%]
test_normalizador.py .....                                               [ 91%]
test_random_forest.py ...                                                [100%]

### Pruebas de Coverage

----------- coverage: platform win32, python 3.6.4-final-0 -----------
Name                    Stmts   Miss  Cover
___________________________________________
arbol.py                  131     16    88%
archivo.py                 30      3    90%
hoja.py                     8      0   100%
modelo.py                  17      2    88%
nodo.py                    51      6    88%
normalizador.py            79     13    84%
random_forest.py           86     56    35%
red_neuronal.py            66     50    24%
test_arbol.py             166      0   100%
test_archivo.py            22      0   100%
test_hoja.py               15      0   100%
test_inicializador.py       0      0   100%
test_modelo.py             22      0   100%
test_nodo.py               64      0   100%
test_normalizador.py       41      0   100%
test_random_forest.py      50      0   100%
test_red_neuronal.py        8      5    38%
___________________________________________
TOTAL                     856    151    82%

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
	* ...
	* ...

- Jake Herrera :
	* ...
	* ...

- Anthony Miranda:
	* ...
	* ...

### Distribución de nota

Estudiante| Tenorio | Jake 	| Anthony |
---------	|---------|---------|---------|
Tareas| 		100	| 		100	| 		100	|
