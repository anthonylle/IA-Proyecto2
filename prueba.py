from MessagePrinter.MessagesPrinter import MessagePrinter
from Board.Board import Board
from BoardPrinter.BoardPrinter import BoardPrinter
from Player.Player import Player

def prueba_mensaje():
	# usar 'clear' en vez de 'cls 'si estan el linux o similar
    mensajes = MessagePrinter('clear')
    mensajes.welcome_message("bright", "", "green")
    mensajes.input_option(">>>> Do you want star the game?[s/n]: ")
    
    board = Board(6,7)
    board.create()
    bp = BoardPrinter('clear',"bringht", "", "blue")
    bp.load_boar(board.column_size)
    player1 = Player('2', "Jake")
    player2 = Player('1', "Teno")
    players = []
    players.append(player1)
    players.append(player2)
    Actual = 0

    """
        podria tomarse el ciclo como posible ciclo principal del juego
    """
    _input = 1
    while( _input  != -1):
        bp.clear_console()
        mensajes.title("bright","","cyan")
        
        if board.insert_value(_input, players[Actual].character): 
            bp.print_board(board)
            if Actual == 0:
                Actual = 1
            else:
                Actual = 0
        else:
            bp.print_board(board)
            mensajes.alert("invalid move ! D:")
        _input = int(mensajes.input_option(">>>> {} select a number column: ".format(players[Actual].name)))

prueba_mensaje()
