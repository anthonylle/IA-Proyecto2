from MiniMax.MiniMax import MiniMax
from Board.Board import Board

def test_minimax_search():
    minimax = MiniMax(1, '1', '2')
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', ' ', ' ', ' '],
                    [' ', ' ', '1', '1', ' ', ' ', '1']]
    best_move = minimax.minimax_search(board, [0,1,2,3,4,5,6])
    assert (best_move == 0)