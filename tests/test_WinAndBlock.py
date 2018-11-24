"""
    WinAndBlock tests
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