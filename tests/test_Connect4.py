"""
    tests Connect4 class
"""

from Connect4.Connect4 import Connect4
from Player.Player import Player
from MessagePrinter.MessagesPrinter import MessagePrinter
from Board.Board import Board

import unittest 
from io import StringIO 
from unittest.mock import patch


def test_main_menu():
    connect4 = Connect4("clear")
    connect4.input = lambda: '3'
    #connect4.main_menu()


class Test_Inputs(unittest.TestCase):

    def request_column_assert(self, given_answer, expected_out, connect4, players, actual):
        with patch('builtins.input', return_value=given_answer):
            col = connect4.request_column(players, actual)
            assert(col == expected_out)

    def test_request_column_1(self):
        connect4 = Connect4("clear")
        players = [Player('1', "Player1"), Player('2', "Player2")]
        actual = 0 #Player1

        self.request_column_assert('1', 1, connect4, players, actual)

    def test_request_column_2(self):
        connect4 = Connect4("clear")
        players = [Player('1', "Player1"), Player('2', "Player2")]
        actual = 0 #Player1

        self.request_column_assert('7', 7, connect4, players, actual)

    def test_request_column_exception(self):
        connect4 = Connect4("clear")
        players = [Player('1', "Player1"), Player('2', "Player2")]
        actual = 0 #Player1

        self.request_column_assert('a', -2, connect4, players, actual)

def test_change_turn_player1_to_player2():
    connect4 = Connect4("clear")
    actual = 0 #player1
    jugador_actual = connect4.change_turn(actual)
    assert(jugador_actual == 1)

def test_change_turn_player2_to_player1():
    connect4 = Connect4("clear")
    actual = 1 #player2
    jugador_actual = connect4.change_turn(actual)
    assert(jugador_actual == 0)

def test_check_win_True_vertical_Player1():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', '2', '2', '1', ' ', '2', ' ']]
    four_in_a_row = connect4.check_win(board, 3, '1')
    assert(four_in_a_row == True)

def test_check_win_True_horizontal_Player2():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', '1', '1', ' ', ' ', ' '],
                    [' ', '2', '2', '2', '2', '2', '1']]
    four_in_a_row = connect4.check_win(board, 5, '2')
    assert(four_in_a_row == True)

def test_check_win_True_diagonal_Player2():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', ' ', ' ', ' ', ' ', ' '],
                    [' ', '1', '2', '1', ' ', ' ', ' '],
                    [' ', '1', '1', '2', '1', ' ', ' '],
                    ['2', '2', '2', '2', '2', '2', '1']]
    four_in_a_row = connect4.check_win(board, 2, '2')
    assert(four_in_a_row == True)

def test_check_win_True_diagonal_inverse_Player1():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', ' ', '2', '1', ' ', ' '],
                    [' ', '1', '2', '1', '1', ' ', ' '],
                    [' ', '2', '1', '2', '1', ' ', ' '],
                    ['2', '1', '2', '2', '2', '2', '1']]
    four_in_a_row = connect4.check_win(board, 4, '1')
    assert(four_in_a_row == True)

def test_check_win_False_Player2():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', ' ', '2', ' ', ' ', ' '],
                    [' ', '1', '2', '1', ' ', ' ', ' '],
                    ['1', '1', '1', '2', '1', ' ', ' '],
                    ['2', '2', '2', '2', '1', '2', '2']]
    four_in_a_row = connect4.check_win(board, 3, '2')
    assert(four_in_a_row == False)

def test_check_vericals_highest_disc_greater_than_2_col_3():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' ']]
    four_in_a_row = connect4.check_verticals(board, 3, '1')
    assert(four_in_a_row == False)

def test_check_vericals_win_highest_disc_row_equals_2_col_3():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    ['2', '2', ' ', '1', ' ', ' ', '2']]
    four_in_a_row = connect4.check_verticals(board, 3, '1')
    assert(four_in_a_row == True)

def test_check_vericals_win_highest_disc_row_equals_1_col_3():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    ['2', '2', '1', '2', ' ', ' ', '2']]
    four_in_a_row = connect4.check_verticals(board, 3, '1')
    assert(four_in_a_row == True)

def test_check_vericals_win_highest_disc_row_equals_0_col_3():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', ' ', ' ', ' '],
                    ['2', '2', '1', '2', '1', ' ', '2']]
    four_in_a_row = connect4.check_verticals(board, 3, '1')
    assert(four_in_a_row == True)

def test_check_vericals_false_in_the_fourth_disc_col_3():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '1', ' ', ' ', ' '],
                    [' ', ' ', ' ', '2', ' ', ' ', ' '],
                    ['2', '2', '1', '2', '1', ' ', ' ']]
    four_in_a_row = connect4.check_verticals(board, 3, '1')
    assert(four_in_a_row == False)

def test_check_vericals_win_Player2_col_6():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', '2'],
                    [' ', ' ', ' ', ' ', ' ', ' ', '2'],
                    [' ', ' ', ' ', '1', ' ', ' ', '2'],
                    [' ', ' ', ' ', '1', ' ', ' ', '2'],
                    [' ', '1', ' ', '2', ' ', ' ', '1'],
                    [' ', '1', '1', '2', '1', ' ', '2']]
    four_in_a_row = connect4.check_verticals(board, 6, '2')
    assert(four_in_a_row == True)
    
def test_horizontals_win_Player1_row_0_1right_2left():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', ' ', '2', '2', ' ', ' '],
                    [' ', '1', '1', '1', '1', ' ', ' ']]
    four_in_a_row = connect4.check_horizontals(board, 2, '1')
    assert(four_in_a_row == True)

def test_horizontals_win_Player1_row_0_all_3_discs_at_the_left():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', '2', '2', ' ', ' ', ' '],
                    [' ', '1', '1', '1', '1', ' ', ' ']]
    four_in_a_row = connect4.check_horizontals(board, 4, '1')
    assert(four_in_a_row == True)

def test_horizontals_win_Player1_row_0_all_3_discs_at_the_right():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', '2', '2', ' ', ' ', ' '],
                    [' ', '1', '1', '1', '1', '2', ' ']]
    four_in_a_row = connect4.check_horizontals(board, 1, '1')
    assert(four_in_a_row == True)

def test__check_horizontals_6_discs_but_only_1_at_the_right():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', '2', '2', '2', ' ', '2'],
                    ['2', '1', '1', '1', '1', '1', '1']]
    discs_in_a_row = connect4._check_horizontals(board, 5+1, 5, '1', True)
    assert(discs_in_a_row == 1)

def test__check_horizontals_6_discs_but_only_4_at_the_left():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', '2', '2', '2', ' ', '2'],
                    ['2', '1', '1', '1', '1', '1', '1']]
    discs_in_a_row = connect4._check_horizontals(board, 5-1, 5, '1', False)
    assert(discs_in_a_row == 4)

def test__check_horizontals_6_discs_but_an_oponent_disc_in_the_middle():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', '2', '2', '2', ' ', '2'],
                    ['1', '1', '1', '2', '1', '1', '1']]
    discs_in_a_row = connect4._check_horizontals(board, 0+1, 5, '1', True)
    assert(discs_in_a_row == 2)

def test_check_diagonals_3_in_line_player1():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', '1', ' ', ' ', ' ', ' '],
                    [' ', '1', '2', ' ', ' ', ' ', ' '],
                    ['1', '2', '1', '2', ' ', ' ', ' ']]
    fout_in_a_row = connect4.check_diagonals(board, 0, '1')
    assert(fout_in_a_row == False)

def test_check_diagonals_3_in_line_player2():
    connect4 = Connect4("clear")
    board = Board(6, 7)
    board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '2', '1', ' ', ' ', ' ', ' '],
                    [' ', '1', '2', ' ', ' ', ' ', ' '],
                    ['1', '2', '1', '2', ' ', ' ', ' ']]
    fout_in_a_row = connect4.check_diagonals(board, 0, '2')
    assert(fout_in_a_row == False)

def test_check_diagonals_player1_win():
        connect4 = Connect4("clear")
        board = Board(6, 7)
        board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', '1', ' ', ' ', ' '],
                        ['2', '2', '1', '1', ' ', ' ', ' '],
                        ['2', '1', '2', '1', ' ', ' ', ' '],
                        ['1', '2', '1', '2', ' ', ' ', ' ']]
        fout_in_a_row = connect4.check_diagonals(board, 3, '1')
        assert(fout_in_a_row == True)

def test_check_diagonals_player1_win_invese_diagonal():
        connect4 = Connect4("clear")
        board = Board(6, 7)
        board.matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        ['2', ' ', '1', ' ', ' ', ' ', ' '],
                        ['2', '2', '1', '1', ' ', ' ', ' '],
                        ['2', '1', '2', '1', ' ', ' ', ' '],
                        ['1', '2', '1', '2', ' ', ' ', ' ']]
        fout_in_a_row = connect4.check_diagonals(board, 0, '2')
        assert(fout_in_a_row == True)

def test__check_diagonals_player2_5_in_diagonal_but_not_next_pos_6_5():
        connect4 = Connect4("clear")
        board = Board(6, 7)
        board.matrix = [[' ', '2', ' ', ' ', ' ', ' ', ' '],
                        ['1', '1', '2', ' ', ' ', ' ', ' '],
                        ['1', '1', '1', '2', ' ', ' ', ' '],
                        ['2', '1', '2', '1', '2', ' ', ' '],
                        ['2', '2', '2', '1', '2', '1', ' '],
                        ['1', '2', '1', '2', '1', '1', '2']]
        diagonal_discs = connect4._check_diagonals(board, 6-1, 5-1, '2', True)
        assert(diagonal_discs == 0)

def test__check_diagonals_player2_4_in_diagonal_just_1_down_pos_3_2():
        connect4 = Connect4("clear")
        board = Board(6, 7)
        board.matrix = [[' ', '2', ' ', ' ', ' ', ' ', ' '],
                        ['1', '1', '2', ' ', ' ', ' ', ' '],
                        ['1', '1', '1', '2', ' ', ' ', ' '],
                        ['2', '1', '2', '1', '2', ' ', ' '],
                        ['2', '2', '2', '1', '2', '1', ' '],
                        ['1', '2', '1', '2', '1', '1', '2']]
        diagonal_discs = connect4._check_diagonals(board, 3+1, 2+1, '2', False)
        assert(diagonal_discs == 1)

def test__check_diagonals_player2_4_in_diagonal_just_2_up_pos_3_2():
        connect4 = Connect4("clear")
        board = Board(6, 7)
        board.matrix = [[' ', '2', ' ', ' ', ' ', ' ', ' '],
                        ['1', '1', '2', ' ', ' ', ' ', ' '],
                        ['1', '1', '1', '2', ' ', ' ', ' '],
                        ['2', '1', '2', '1', '2', ' ', ' '],
                        ['2', '2', '2', '1', '2', '1', ' '],
                        ['1', '2', '1', '2', '1', '1', '2']]
        diagonal_discs = connect4._check_diagonals(board, 3-1, 2-1, '2', True)
        assert(diagonal_discs == 2)