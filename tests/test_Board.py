from Board.Board import Board

board = Board(6, 7)
board.matrix = [['1', '2', ' ', ' ', ' ', '1', ' '],
                ['1', '1', '1', ' ', ' ', '2', ' '],
                ['2', '1', '2', '2', ' ', '1', ' '],
                ['2', '1', '1', '1', '2', '2', ' '],
                ['2', '2', '1', '2', '2', '1', ' '],
                ['1', '1', '1', '2', '1', '2', '1']]

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