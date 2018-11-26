from MiniMax.MiniMax import *
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
    best_move = minimax.search_best_move(board, [0,1,2,3,4,5,6])
    assert (best_move == 1)

def test_minimax_Secuential():
    secuential = Secuential(1, '1', '2')
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', '2'],
                    [' ', ' ', ' ', ' ', ' ', ' ', '1'],
                    [' ', ' ', '2', ' ', ' ', '1', '1'],
                    ['2', '1', '2', '2', '2', '1', '1']]
    best_move = secuential.heuristic(board)
    assert (best_move == 114)