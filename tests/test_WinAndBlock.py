"""
    tests WinAndBlock class 
"""
from WinAndBlock.WinAndBlock import *
from Connect4.Connect4 import Connect4
from Board.Board import Board
from Player.Player import Player

def test_check_normal_flow_empty_matrix_no_win_posibility():
    checker = Checker()
    connect4 = Connect4('clear')
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    players = [Player('1', "Player1"), Player('2', "Player2")]
    actual = 0 #Player1

    result = checker.check(connect4, board, players,actual)
    assert(result == -1)

def test_check_win_posibility_player1_col_4():
    win_checker = Win_Checker()
    connect4 = Connect4('clear')
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['1', '1', '1', ' ', '2', '2', ' ']]
    players = [Player('1', "Player1"), Player('2', "Player2")]
    actual = 0 #Player1

    
    result = win_checker.check(connect4, board, players,actual)
    assert(result == 4)

def test_check_block_posibility_player1_col_6():
    block_checker = Block_Checker()
    connect4 = Connect4('clear')
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '1', ' ', ' ', ' ', ' ', ' '],
                    ['1', '1', '2', '2', '2', ' ', ' ']]
    players = [Player('1', "Player1"), Player('2', "Player2")]
    actual = 0 #Player1

    
    result = block_checker.check(connect4, board, players,actual)
    assert(result == 6)

def test_check_win_posibility_player2_col_3():
    win_checker = Win_Checker()
    connect4 = Connect4('clear')
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', '1', ' ', ' ', ' ', ' ', ' '],
                    ['1', '1', ' ', '2', '2', '2', ' ']]
    players = [Player('1', "Player1"), Player('2', "Player2")]
    actual = 1 #Player2

    result = win_checker.check(connect4, board, players,actual)
    assert(result == 3)

def test_check_block_posibility_player2_col_1():
    block_checker = Block_Checker()
    connect4 = Connect4('clear')
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['1', '1', '1', ' ', ' ', '2', ' '],
                    ['1', '1', '2', '2', '2', '1', ' '],
                    ['1', '1', '2', '2', '2', '1', '2']]
    players = [Player('1', "Player1"), Player('2', "Player2")]
    actual = 1 #Player2

    result = block_checker.check(connect4, board, players,actual)
    assert(result == 1)

def test_check_block_posibility_player2_col_2():
    win_checker = Win_Checker()
    connect4 = Connect4('clear')
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['1', '1', '1', ' ', ' ', '2', ' '],
                    ['1', '1', '2', '2', '2', '1', ' '],
                    ['1', '1', '2', '2', '2', '1', '2']]
    players = [Player('1', "Player1"), Player('2', "Player2")]
    actual = 0 #Player1

    result = win_checker.check(connect4, board, players,actual)
    assert(result == 2)

def test_check_win_True_vertical_Player1():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', '2', '2', '1', ' ', '2', ' ']]
    four_in_a_row = checker.check_win(board, 3, '1')
    assert(four_in_a_row == True)


def test_check_win_True_horizontal_Player2():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', '1', '1', ' ', ' ', ' '],
                    [' ', '2', '2', '2', '2', '2', '1']]
    four_in_a_row = checker.check_win(board, 5, '2')
    assert(four_in_a_row == True)

def test_check_win_True_diagonal_Player2():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', ' ', ' ', ' ', ' ', ' '],
                    [' ', '1', '2', '1', ' ', ' ', ' '],
                    [' ', '1', '1', '2', '1', ' ', ' '],
                    ['2', '2', '2', '2', '2', '2', '1']]
    four_in_a_row = checker.check_win(board, 2, '2')
    assert(four_in_a_row == True)

def test_check_win_True_diagonal_inverse_Player1():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', ' ', '2', '1', ' ', ' '],
                    [' ', '1', '2', '1', '1', ' ', ' '],
                    [' ', '2', '1', '2', '1', ' ', ' '],
                    ['2', '1', '2', '2', '2', '2', '1']]
    four_in_a_row = checker.check_win(board, 4, '1')
    assert(four_in_a_row == True)

def test_check_win_False_Player2():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', ' ', '2', ' ', ' ', ' '],
                    [' ', '1', '2', '1', ' ', ' ', ' '],
                    ['1', '1', '1', '2', '1', ' ', ' '],
                    ['2', '2', '2', '2', '1', '2', '2']]
    four_in_a_row = checker.check_win(board, 3, '2')
    assert(four_in_a_row == False)

def test_check_vericals_highest_disc_greater_than_2_col_3():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' ']]
    four_in_a_row = checker.check_verticals(board, 3, '1')
    assert(four_in_a_row == False)

def test_check_vericals_win_highest_disc_row_equals_2_col_3():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    ['2', '2', ' ', '1', ' ', ' ', '2']]
    four_in_a_row = checker.check_verticals(board, 3, '1')
    assert(four_in_a_row == True)

def test_check_vericals_win_highest_disc_row_equals_1_col_3():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    ['2', '2', '1', '2', ' ', ' ', '2']]
    four_in_a_row = checker.check_verticals(board, 3, '1')
    assert(four_in_a_row == True)

def test_check_vericals_win_highest_disc_row_equals_0_col_3():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', ' ', ' ', ' '],
                    ['2', '2', '1', '2', '1', ' ', '2']]
    four_in_a_row = checker.check_verticals(board, 3, '1')
    assert(four_in_a_row == True)

def test_check_vericals_false_in_the_fourth_disc_col_3():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', ' ', ' ', ' '],
                    ['2', '2', '1', '2', '1', ' ', ' ']]
    four_in_a_row = checker.check_verticals(board, 3, '1')
    assert(four_in_a_row == False)

def test_check_vericals_win_Player2_col_6():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', '2'],
                    [' ', ' ', ' ', ' ', ' ', ' ', '2'],
                    [' ', ' ', ' ', '1', ' ', ' ', '2'],
                    [' ', ' ', ' ', '1', ' ', ' ', '2'],
                    [' ', '1', ' ', '2', ' ', ' ', '1'],
                    [' ', '1', '1', '2', '1', ' ', '2']]
    four_in_a_row = checker.check_verticals(board, 6, '2')
    assert(four_in_a_row == True)
    
def test_horizontals_win_Player1_row_0_1right_2left():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', ' ', '2', '2', ' ', ' '],
                    [' ', '1', '1', '1', '1', ' ', ' ']]
    four_in_a_row = checker.check_horizontals(board, 2, '1')
    assert(four_in_a_row == True)

def test_horizontals_win_Player1_row_0_all_3_discs_at_the_left():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', '2', '2', ' ', ' ', ' '],
                    [' ', '1', '1', '1', '1', ' ', ' ']]
    four_in_a_row = checker.check_horizontals(board, 4, '1')
    assert(four_in_a_row == True)

def test_horizontals_win_Player1_row_0_all_3_discs_at_the_right():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', '2', '2', ' ', ' ', ' '],
                    [' ', '1', '1', '1', '1', '2', ' ']]
    four_in_a_row = checker.check_horizontals(board, 1, '1')
    assert(four_in_a_row == True)

def test__check_horizontals_6_discs_but_only_1_at_the_right():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', '2', '2', '2', ' ', '2'],
                    ['2', '1', '1', '1', '1', '1', '1']]
    discs_in_a_row = checker._check_horizontals(board, 5+1, 5, '1', True)
    assert(discs_in_a_row == 1)

def test__check_horizontals_6_discs_but_only_4_at_the_left():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', '2', '2', '2', ' ', '2'],
                    ['2', '1', '1', '1', '1', '1', '1']]
    discs_in_a_row = checker._check_horizontals(board, 5-1, 5, '1', False)
    assert(discs_in_a_row == 4)

def test__check_horizontals_6_discs_but_an_oponent_disc_in_the_middle():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', '2', '2', '2', ' ', '2'],
                    ['1', '1', '1', '2', '1', '1', '1']]
    discs_in_a_row = checker._check_horizontals(board, 0+1, 5, '1', True)
    assert(discs_in_a_row == 2)

def test_check_diagonals_3_in_line_player1():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', '1', ' ', ' ', ' ', ' '],
                    [' ', '1', '2', ' ', ' ', ' ', ' '],
                    ['1', '2', '1', '2', ' ', ' ', ' ']]
    fout_in_a_row = checker.check_diagonals(board, 0, '1')
    assert(fout_in_a_row == False)

def test_check_diagonals_3_in_line_player2():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', '1', ' ', ' ', ' ', ' '],
                    [' ', '1', '2', ' ', ' ', ' ', ' '],
                    ['1', '2', '1', '2', ' ', ' ', ' ']]
    fout_in_a_row = checker.check_diagonals(board, 0, '2')
    assert(fout_in_a_row == False)

def test_check_diagonals_player1_win():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    ['2', '2', '1', '1', ' ', ' ', ' '],
                    ['2', '1', '2', '1', ' ', ' ', ' '],
                    ['1', '2', '1', '2', ' ', ' ', ' ']]
    fout_in_a_row = checker.check_diagonals(board, 3, '1')
    assert(fout_in_a_row == True)

def test_check_diagonals_player1_win_invese_diagonal():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', '1', ' ', ' ', ' ', ' '],
                    ['2', '2', '1', '1', ' ', ' ', ' '],
                    ['2', '1', '2', '1', ' ', ' ', ' '],
                    ['1', '2', '1', '2', ' ', ' ', ' ']]
    fout_in_a_row = checker.check_diagonals(board, 0, '2')
    assert(fout_in_a_row == True)

def test__check_diagonals_player2_5_in_diagonal_but_not_next_pos_6_5():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', '2', ' ', ' ', ' ', ' ', ' '],
                    ['1', '1', '2', ' ', ' ', ' ', ' '],
                    ['1', '1', '1', '2', ' ', ' ', ' '],
                    ['2', '1', '2', '1', '2', ' ', ' '],
                    ['2', '2', '2', '1', '2', '1', ' '],
                    ['1', '2', '1', '2', '1', '1', '2']]
    diagonal_discs = checker._check_diagonals(board, 6-1, 5-1, '2', True)
    assert(diagonal_discs == 0)

def test__check_diagonals_player2_4_in_diagonal_just_1_down_pos_3_2():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', '2', ' ', ' ', ' ', ' ', ' '],
                    ['1', '1', '2', ' ', ' ', ' ', ' '],
                    ['1', '1', '1', '2', ' ', ' ', ' '],
                    ['2', '1', '2', '1', '2', ' ', ' '],
                    ['2', '2', '2', '1', '2', '1', ' '],
                    ['1', '2', '1', '2', '1', '1', '2']]
    diagonal_discs = checker._check_diagonals(board, 3+1, 2+1, '2', False)
    assert(diagonal_discs == 1)

def test__check_diagonals_player2_4_in_diagonal_just_2_up_pos_3_2():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', '2', ' ', ' ', ' ', ' ', ' '],
                    ['1', '1', '2', ' ', ' ', ' ', ' '],
                    ['1', '1', '1', '2', ' ', ' ', ' '],
                    ['2', '1', '2', '1', '2', ' ', ' '],
                    ['2', '2', '2', '1', '2', '1', ' '],
                    ['1', '2', '1', '2', '1', '1', '2']]
    diagonal_discs = checker._check_diagonals(board, 3-1, 2-1, '2', True)
    assert(diagonal_discs == 2)

def test_check_horizontals_count_1_with_0_neighbours():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' ']]
    neighbour_discs = checker.check_horizontals_count(board, 5, 3, '1', 0)
    assert(neighbour_discs == 1)

def test_check_horizontals_count_0_with_2_neighbours_but_search_limit_2():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', ' ', ' ', '2'],
                    ['1', ' ', ' ', '1', ' ', ' ', '1']]
    neighbour_discs = checker.check_horizontals_count(board, 5, 3, '1', 2)
    assert(neighbour_discs == 0)

def test_check_horizontals_count_1_with_2_neighbours_search_limit_2_but_only_one_into_limit():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', ' ', ' ', '2'],
                    [' ', '1', ' ', '1', ' ', ' ', '1']]
    neighbour_discs = checker.check_horizontals_count(board, 5, 3, '1', 2)
    assert(neighbour_discs == 1)

def test_check_diagonals_count_2_with_2_neighbours_search_limit_1_Player2():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', ' ', ' ', ' '],
                    [' ', ' ', '2', '1', ' ', ' ', ' '],
                    [' ', ' ', '1', '2', ' ', ' ', '2'],
                    ['2', '1', '1', '1', ' ', ' ', '1']]
    neighbour_discs = checker.check_diagonals_count(board, 5, 0, '2', 1)
    assert(neighbour_discs == 2)

def test_check_diagonals_count_1_search_limit_2_with_2_neighbours_but_only_1_in_limit_Player2():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', ' ', ' ', ' '],
                    [' ', ' ', '2', '1', ' ', ' ', ' '],
                    [' ', ' ', '1', '2', ' ', ' ', '2'],
                    ['2', '1', '1', '1', ' ', ' ', '1']]
    neighbour_discs = checker.check_diagonals_count(board, 5, 0, '2', 2)
    assert(neighbour_discs == 1)


def test_check_diagonals_count_1_search_limit_3_with_2_neighbours_both_in_limit_Player2():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', ' ', ' ', ' '],
                    [' ', ' ', '2', '1', ' ', ' ', ' '],
                    [' ', ' ', '1', '2', ' ', ' ', '2'],
                    ['2', '1', '1', '1', ' ', ' ', '1']]
    neighbour_discs = checker.check_diagonals_count(board, 5, 0, '2', 3)
    assert(neighbour_discs == 1)

def test_check_diagonals_count_3_search_limit_3_transposed_diagonal_with_2_neighbours_both_in_limit_Player2():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['1', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', '2', '1', ' ', ' ', ' '],
                    ['2', '2', '1', '2', ' ', ' ', ' '],
                    ['2', '1', '1', '1', ' ', ' ', '1']]
    neighbour_discs = checker.check_diagonals_count(board, 2, 0, '1', 3)
    assert(neighbour_discs == 1)

def test_check_verticals_count_2():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', '1', ' ', ' ', ' ', ' '],
                    ['2', ' ', '2', '1', ' ', ' ', ' '],
                    ['2', '2', '1', '2', ' ', ' ', ' '],
                    ['2', '1', '1', '1', ' ', ' ', '1']]
    neighbour_discs = checker.check_verticals_count(board, 1, 0, '2', 2)
    assert(neighbour_discs == 1)

def test_check_verticals_count_5_limit_99():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', '1', ' ', ' ', ' ', ' '],
                    ['2', ' ', '2', '1', ' ', ' ', ' '],
                    ['2', '2', '1', '2', ' ', ' ', ' '],
                    ['2', '1', '1', '1', ' ', '1', '1']]
    neighbour_discs = checker.check_verticals_count(board, 1, 0, '2', 4)
    assert(neighbour_discs == 1)

def test_Secuential_Count_check_verticals():
    checker = Secuential_Count_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', '1', ' ', ' ', ' ', ' '],
                    ['2', ' ', '2', '1', ' ', ' ', ' '],
                    ['2', '2', '1', '2', ' ', ' ', ' '],
                    ['2', '1', '1', '1', ' ', '1', '1']]
    neighbour_discs = checker.check_verticals_count(board, 1, 0, '2', 4)
    assert(neighbour_discs == 1)

def test_Secuential_Count_check_horizontals():
    checker = Secuential_Count_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', '1', ' ', ' ', ' ', ' '],
                    ['2', ' ', '2', '1', ' ', ' ', ' '],
                    ['2', '2', '1', '2', ' ', ' ', ' '],
                    ['2', '1', '1', '1', ' ', '1', '1']]
    neighbour_discs = checker.check_horizontals_count(board, 5, 2, '1', 3)
    assert(neighbour_discs == 1)

def test_Secuential_Count_check_diagonals():
    checker = Secuential_Count_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', '1', ' ', ' ', ' ', ' '],
                    ['2', ' ', '2', '1', ' ', ' ', ' '],
                    ['2', '2', '1', '2', ' ', ' ', ' '],
                    ['2', '1', '1', '1', ' ', '1', '1']]
    neighbour_discs = checker.check_diagonals(board, 3, 2, '2', 3)
    assert(neighbour_discs == 1)

def test_Secuential_Count_check_lines_4_in_line_count_1():
    checker = Secuential_Count_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', '1', ' ', ' ', ' ', ' '],
                    ['2', ' ', '2', '1', ' ', ' ', ' '],
                    ['2', '2', '1', '2', ' ', ' ', ' '],
                    ['2', '1', '1', '1', ' ', '1', '1']]
    neighbour_discs = checker.check_lines(board, '2', 4)
    assert(neighbour_discs == 1)

def test_Secuential_Count_check_lines_4_in_line_count_2():
    checker = Secuential_Count_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', '1', ' ', ' ', ' ', ' '],
                    ['2', ' ', '2', '1', ' ', ' ', ' '],
                    ['2', '2', '1', '2', ' ', ' ', ' '],
                    ['2', '1', '1', '1', ' ', '1', '1']]
    neighbour_discs = checker.check_lines(board, '2', 3)
    assert(neighbour_discs == 5)

def test_Secuential_Count_check_lines_3_in_line_count_4():
    checker = Secuential_Count_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', '2'],
                    [' ', ' ', ' ', ' ', ' ', ' ', '1'],
                    [' ', ' ', '2', ' ', ' ', '1', '1'],
                    ['2', '1', '2', '2', '2', '1', '1']]
    neighbour_discs = checker.check_lines(board, '1', 2)
    assert(neighbour_discs == 14)

def test_Check_check_lines_13_in_line_count_2():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', '2'],
                    [' ', ' ', ' ', ' ', ' ', ' ', '1'],
                    [' ', ' ', '2', ' ', ' ', '1', '1'],
                    ['2', '1', '2', '2', '2', '1', '1']]
    neighbour_discs = checker.check_lines(board, '1', 2)
    assert(neighbour_discs == 13)

def test_Check_check_lines_3_in_line_count_3():
    checker = Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', ' ', ' ', ' '],
                    [' ', '1', ' ', '1', ' ', ' ', ' '],
                    [' ', '2', ' ', '2', ' ', ' ', ' '],
                    ['2', '1', ' ', '1', ' ', ' ', ' ']]
    neighbour_discs = checker.check_lines(board, '2', 3)
    assert(neighbour_discs == 3)


def test_Block_3_check_verticals_count():
    block = Block_3_In_Line_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', '1', ' ', ' ', ' ', ' '],
                    [' ', ' ', '2', ' ', ' ', ' ', '2'],
                    [' ', ' ', '2', ' ', ' ', '1', '1'],
                    ['2', '1', '2', '2', '2', '1', '1']]
    best_move = block.check_verticals_count(board, 3, 6, '2',3)
    assert (best_move == True)

def test_Block_3_check_verticals_count_Player1():
    block = Block_3_In_Line_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', '1', ' ', ' ', ' ', ' '],
                    [' ', ' ', '2', ' ', ' ', ' ', '2'],
                    [' ', ' ', '2', ' ', '1', '1', '1'],
                    ['2', '1', '2', '2', '2', '1', '1']]
    best_move = block.check_verticals_count(board, 2, 2, '1',4)
    assert (best_move == True)

def test_Block_3_check_verticals_count_Player1_2():
    block = Block_3_In_Line_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', '1', ' ', ' ', ' ', ' '],
                    [' ', ' ', '2', ' ', ' ', ' ', '2'],
                    [' ', ' ', '2', ' ', '1', '1', '1'],
                    ['2', '1', '2', '2', '2', '1', '1']]
    best_move = block.check_verticals_count(board, 4, 4, '1',2)
    assert (best_move == True)

def test_Block_3_check_horizontals_count_2_Player1():
    block = Block_3_In_Line_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', '2', ' ', ' ']]
    best_move = block.check_horizontals_count(board, 5, 3, '1', 2)
    assert (best_move == True)

def test_Block_3_check_horizontals_count_3_Player1():
    block = Block_3_In_Line_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', ' ', '1', '2', ' ', ' ']]
    best_move = block.check_horizontals_count(board, 5, 3, '1',3)
    assert (best_move == True)

def test_Block_3_check_diagonals_count_2_Player1():
    block = Block_3_In_Line_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', '2', ' ', ' '],
                    [' ', '2', ' ', '1', '2', ' ', ' ']]
    best_move = block._check_diagonals_count(board, 4, 3, '1',2, True)
    assert (best_move == True)

def test_Block_3_check_diagonals_count_3_Player1():
    block = Block_3_In_Line_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', ' ', ' ', ' ', ' ', ' '],
                    [' ', '1', ' ', ' ', ' ', ' ', ' '],
                    [' ', '1', ' ', '1', '2', ' ', ' '],
                    [' ', '2', ' ', '1', '2', ' ', ' ']]
    best_move = block._check_diagonals_count(board, 4, 3, '1',3, True)
    assert (best_move == True)

def test_Block_3_check_diagonals_count_3_Player1_only_2_inside_limit():
    block = Block_3_In_Line_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['1', '1', ' ', ' ', ' ', ' ', ' '],
                    ['2', '1', ' ', '1', '2', ' ', ' '],
                    ['1', '2', '1', '1', '2', ' ', ' ']]
    best_move = block._check_diagonals_count(board, 4, 3, '1',3, True)
    assert (best_move == False)

def test_Block_3_check_diagonals_count_1():
    block = Block_3_In_Line_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', '2', ' ', ' ', ' ', ' ', ' '],
                    ['1', '1', ' ', ' ', ' ', ' ', ' '],
                    ['2', '1', ' ', '1', '2', ' ', ' '],
                    ['1', '2', '1', '1', '2', ' ', ' ']]
    best_move = block.check_diagonals_count(board, 4, 3, '1',3)
    assert (best_move == 1)

def test_Block_3_check_diagonals_count_2():
    block = Block_3_In_Line_Checker()
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['2', '2', ' ', ' ', ' ', ' ', ' '],
                    ['1', '1', ' ', ' ', '2', ' ', ' '],
                    ['2', '1', ' ', '1', '2', '1', '1'],
                    ['1', '2', '2', '1', '2', '1', '1']]
    best_move = block.check_diagonals_count(board, 4, 3, '1',3)
    assert (best_move == 2)