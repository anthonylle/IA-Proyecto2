from MiniMax.MiniMax import *
from Board.Board import Board

board = Board(6, 7)
board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', '2', ' ', ' ', ' '],
                [' ', ' ', '1', '1', ' ', ' ', '1']]

def test_check_state():
    minimax = MiniMax(1, '1', '2')
    state = minimax.check_state(board, 1, '1')
    assert(state == False)

def test_check_state_win():
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', ' ', ' ', ' '],
                    [' ', '2', '1', '1', '1', '1', ' ']]
    minimax = MiniMax(1, '1', '2')
    board.insert_value(7, '1')
    state = minimax.check_state(board, 1, '1')
    assert(state == True)

def test_check_state_depth_reached():
    minimax = MiniMax(1, '1', '2')
    state = minimax.check_state(board, 2, '1')
    assert(state == True)

def test_check_state_max_legal_moves_reached():
    minimax = MiniMax(1, '1', '2')
    board.moves_count = 42
    state = minimax.check_state(board, 1, '1')
    board.moves_count = 7
    assert(state == True)

def test_minimax_search():
    minimax = MiniMax(1, '1', '2')
    best_move = minimax.search_best_move(board, [0,1,2,3,4,5,6])
    assert (best_move == 1)

def test_heuristic():
    minimax = MiniMax(1, '1', '2')
    heuristic = minimax.heuristic(board)
    assert(heuristic == 0)

def test_min_value():
    minimax = MiniMax(2, '1', '2')
    board.matrix = [['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['1', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['1', ' ', ' ', '2', ' ', ' ', ' '],
                    ['2', ' ', '1', '2', ' ', ' ', ' '],
                    ['2', '2', '1', '1', '1', ' ', ' ']]
    min_value = minimax.min_value(0, board, -99999, 99999)
    assert(min_value == 0) #heuristica

def test_min_value():
    minimax = MiniMax(2, '1', '2')
    board.matrix = [['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['1', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['1', ' ', ' ', '2', ' ', ' ', ' '],
                    ['2', ' ', '1', '2', ' ', ' ', ' '],
                    ['2', '2', '1', '1', '1', ' ', ' ']]
    min_value = minimax.max_value(0, board, -99999, 99999)
    assert(min_value == 0) #heuristica

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

def test_minimax_Block3_in_line():
    block_3 = Block_3_In_Line(1, '2', '1')
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', '2', '1', ' ']]
    best_move = block_3.heuristic(board)
    assert (best_move == 1100)


def test_minimax_Block_3():
    secuential = Block_3_In_Line(1, '1', '2')
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '1', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', ' ', '1', ' ', ' ', ' '],
                    [' ', '2', '1', '1', ' ', ' ', ' ']]
    best_move = secuential.heuristic(board)
    assert (best_move == 1300)

def test_minimax_Play_3_in_line():
    secuential = Block_3_In_Line(1, '1', '2')
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', '2', ' ', ' '],
                    [' ', '1', '1', '1', '2', ' ', ' ']]
    best_move = secuential.heuristic(board)
    assert (best_move == 1200)