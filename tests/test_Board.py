from Board.Board import Board
from io import StringIO
from unittest import mock

board = Board(6, 7)

m = [['1','2', ' ', ' ', ' ', '1', ' '],
    ['1', '1', '1', ' ', ' ', '2', ' '],
    ['2', '1', '2', '2', ' ', '1', ' '],
    ['2', '1', '1', '1', '2', '2', ' '],
    ['2', '2', '1', '2', '2', '1', ' '],
    ['1', '1', '1', '2', '1', '2', '1']]
board.moves_count=34

board.matrix = m


def test_copy():
    copy = board.copy()
    assert(copy.__dict__ == board.__dict__)

#------------------------------------------------------------------------------
def test_create():
    board = Board(6, 7)
    board.create()
    matrix = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    
    assert(board.matrix == matrix)

def test_create2():
    board = Board(6, 7)
    board.create()
    assert(board.matrix != [])

#-------------------------- insert value --------------------------------------   
def test_insert_value1():
    copy = board.copy()
    assert (copy.insert_value(0, "1") == False)

def test_insert_value2():
    copy = board.copy()
    assert (copy.insert_value(8, "2") == False)
    
def test_insert_value3():
    copy = board.copy()
    assert (copy.insert_value(9, "1") == False)  
    
def test_insert_value4():
    copy = board.copy()
    assert (copy.insert_value(-1, "2") == False)  
    
def test_insert_value5():
    copy = board.copy()
    assert (copy.insert_value(1, "2") == False)
    
def test_insert_value6():
    copy = board.copy()
    assert (copy.insert_value(4, "1") == True)  
    
def test_insert_value7():
    copy = board.copy()
    assert (copy.insert_value(7, "2") == True) 
    
def test_insert_value8():
    copy = board.copy()
    assert (copy.insert_value(6, "1") == False)
    
#-------------------------- insert aux ----------------------------------------   
def test_insert_aux1():
    
    assert( board.insert_aux(0, "2") == False)
    
def test_insert_aux2():    
    assert( board.insert_aux(1, "2") == False)
    
def test_insert_aux3():    
    assert( board.insert_aux(5, "2") == False)

def test_insert_aux4():    
    copy = board.copy()
    assert( copy.insert_aux(2, "2") == True)

def test_insert_aux5():    
    copy = board.copy()
    copy.insert_aux(2, "2") 
    m = [['1','2', '2', ' ', ' ', '1', ' '],
        ['1', '1', '1', ' ', ' ', '2', ' '],
        ['2', '1', '2', '2', ' ', '1', ' '],
        ['2', '1', '1', '1', '2', '2', ' '],
        ['2', '2', '1', '2', '2', '1', ' '],
        ['1', '1', '1', '2', '1', '2', '1']]

    assert( copy.matrix == m) 

def test_insert_aux6():    
    copy = board.copy()
    assert( copy.insert_aux(4, "2") == True)
    
def test_insert_aux7():    
    copy = board.copy()
    copy.insert_aux(4, "1") 
    m = [['1','2', ' ', ' ', ' ', '1', ' '],
        ['1', '1', '1', ' ', ' ', '2', ' '],
        ['2', '1', '2', '2', '1', '1', ' '],
        ['2', '1', '1', '1', '2', '2', ' '],
        ['2', '2', '1', '2', '2', '1', ' '],
        ['1', '1', '1', '2', '1', '2', '1']]
    assert( copy.matrix == m)  

#---------------------- is_column_full ----------------------------------------

def test_is_column_full1():
    assert ( board.is_column_full(0) == True)     

def test_is_column_full2():
    assert ( board.is_column_full(1) == True)  
    
def test_is_column_full3():
    assert ( board.is_column_full(5) == True) 
    
def test_is_column_full4():
    assert ( board.is_column_full(2) == False)     

def test_is_column_full5():
    assert ( board.is_column_full(3) == False)  
    
def test_is_column_full6():
    assert ( board.is_column_full(4) == False) 
    
def test_is_column_full7():
    assert ( board.is_column_full(6) == False)

#---------------------- have_legal_move ----------------------------------------

def test_have_legal_move1():
    assert( board.have_legal_move() == True)
    
def test_have_legal_move2():
    copy = board.copy()
    copy.moves_count = 0
    assert( copy.have_legal_move() == True)
    
def test_have_legal_move3():
    copy = board.copy()
    copy.moves_count = 41
    assert( copy.have_legal_move() == True)    
    
def test_have_legal_move4():
    copy = board.copy()
    copy.moves_count = 42
    assert( copy.have_legal_move() == False) 
    
    
#---------------------- is_legal_area -----------------------------------------   
def test_is_legal_area():        
    is_legal_area = board.is_legal_area([0,1,2])
    assert (is_legal_area == True)
    
def test_is_legal_area2():
    is_legal_area = board.is_legal_area([0,1])
    assert (is_legal_area == False)
    
def test_is_legal_area3():    
    is_legal_area = board.is_legal_area([2,3,4])
    assert (is_legal_area == True)
    
def test_is_legal_area4():    
    is_legal_area = board.is_legal_area([5])
    assert (is_legal_area == False)
    
def test_is_legal_area5():    
    is_legal_area = board.is_legal_area([0,1,2,3,4,5,6])
    assert (is_legal_area == True)    
    
def test_is_legal_area6():   
    is_legal_area = board.is_legal_area([])
    assert (is_legal_area == False)    
    
#---------------------- get_at -----------------------------------------
    
def test_setAt1():
    copy = board.copy()
    assert( copy.setAt(-1,6," ") == False)
    
def test_setAt2():
    copy = board.copy()
    assert( copy.setAt(7,6, "1") == False)
    
def test_setAt3():
    copy = board.copy()
    assert( copy.setAt(0,7, "2") == False)
    
def test_setAt4():
    copy = board.copy()
    assert( copy.setAt(0,-1, "2") == False)
    
def test_setAt5():
    copy = board.copy()
    assert( copy.setAt(0,0, "2") == True)
    
def test_setAt6():
    copy = board.copy()
    assert( copy.setAt(5,6, "2") == True)

def test_setAt7():
    copy = board.copy()
    assert( copy.setAt(2,3, "2") == True)
    
def test_setAt8():
    copy = board.copy()
    copy.setAt(5,6, "2")
    m = [['1','2', ' ', ' ', ' ', '1', ' '],
        ['1', '1', '1', ' ', ' ', '2', ' '],
        ['2', '1', '2', '2', ' ', '1', ' '],
        ['2', '1', '1', '1', '2', '2', ' '],
        ['2', '2', '1', '2', '2', '1', ' '],
        ['1', '1', '1', '2', '1', '2', '2']]
    assert( copy.matrix == m)
    
    
#---------------------- get_column_with_space ---------------------------------
def test_get_column_with_space1():
    assert (board.get_column_with_space([0,1,2,3,4,5,6]) == 2)
    
    
def test_get_column_with_space2():
    assert (board.get_column_with_space([0,1]) == -2)
    
def test_get_column_with_space3():
    assert (board.get_column_with_space([5]) == -2)
    
    
def test_get_column_with_space4():
    assert (board.get_column_with_space([4,5,6]) == 4)
    
def test_get_column_with_space5():
    assert (board.get_column_with_space([6,5,4]) == 6)
    
def test_get_column_with_space6():
    assert (board.get_column_with_space([]) == -2)
            
def test_get_column_with_space7():
    assert (board.get_column_with_space([3,4,5,6]) == 3)
    
#---------------------------  get_set_space  ----------------------------------
    
def test_get_set_space():
    assert( board.get_set_space() == {0,1,2,3,4,5,6})
    
class Test_Print():
    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_print_matrix(self, mock_stdout):

        board.print_matrix()

        console = "".join(["['1','2', ' ', ' ', ' ', '1', ' ']\n",
                            "['1','1', '1', ' ', ' ', '2', ' ']\n",
                            "['2','1', '2', '2', ' ', '1', ' ']\n",
                            "['2','1', '1', '1', '2', '2', ' ']\n",
                            "['2','2', '1', '2', '2', '1', ' ']\n",
                            "['1','1', '1', '2', '1', '2', '1']\n"])  
        assert (mock_stdout.getvalue() == console)