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
