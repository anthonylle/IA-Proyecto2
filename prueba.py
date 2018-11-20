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

    """
        podria tomarse el ciclo como posible ciclo principal del juego
    """
    _input = 1
    while( _input  != -1):
        bp.clear_console()
        mensajes.title("bright","","cyan")
        
        if board.insert_value(_input, player1.character): 
            bp.print_board(board)
        else:
            bp.print_board(board)
            mensajes.alert("invalid move ! D:")
        _input = int(mensajes.input_option(">>>> Select a number column: "))

prueba_mensaje()
