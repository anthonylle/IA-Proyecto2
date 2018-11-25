"""
    tests Player Class
"""
from Player.Player import Player
from io import StringIO
from unittest import mock



def test_create_Player_1():
    Player('1', 'Player1')

def test_create_Player_2():
    Player('2', 'Player2')

def test_get_Player_1_name():
    player1 = Player('1', 'Player1')
    name = player1.name
    assert(name == 'Player1')

def test_get_Player_1_character():
    player1 = Player('1', 'Player1')
    character = player1.character
    assert(character == '1')

def test_get_Player_2_name():
    player2 = Player('2', 'Player2')
    name = player2.name
    assert(name == 'Player2')

def test_get_Player_2_character():
    player2 = Player('2', 'Player2')
    character = player2.character
    assert(character == '2')

def test_add_win():
    player = Player('1', 'Player')
    player.add_win()
    player.add_win()
    player.add_win()

    wins = player.record[player.WINS]
    assert(wins == 3)

def test_add_lose():
    player = Player('1', 'Player')
    player.add_lose()
    player.add_lose()

    losses = player.record[player.LOSSES]
    assert(losses == 2)

def test_add_draw():
    player = Player('1', 'Player')
    player.add_draw()

    draws = player.record[player.DRAWS]
    assert(draws == 1)



class Test_Print():
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_print_record(self, mock_stdout):
        player = Player('1', 'Player')
        player.add_win()
        player.add_win()
        player.add_lose()

        player.print_record()

        console = "Player Record: Wins: 2 | Losses: 1 | draws: 0\n"
        assert (mock_stdout.getvalue() == console)


