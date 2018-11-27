from Agent.Agent import Agent
from io import StringIO
from unittest import mock
"""
    tests Agent Class
"""

class Test_Agent():
    
    def test_create_ranges_disordered(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        dic = a.create_ranges(0.7, 0.5, 0.9, 0.2)
        assert ({3: [0, 0.2], 1: [0.21, 0.5], 0: [0.51, 0.7], 2: [0.71, 0.9]} == dic)
    
    def test_create_ranges_ascendant(self):
        a = Agent("1", "",0.1, 0.5, 0.7, 0.98)
        dic = a.create_ranges(0.1, 0.5, 0.7, 0.98)
        assert ({0: [0, 0.1], 1: [0.11, 0.5], 2: [0.51, 0.7], 3: [0.71, 0.98]} == dic)        

    def test_create_ranges_falling(self):
        a = Agent("1", "",0.98, 0.7, 0.5, 0.1)
        dic = a.create_ranges(0.98, 0.7, 0.5, 0.1)
        assert ({3: [0, 0.1], 2: [0.11, 0.5], 1: [0.51, 0.7], 0: [0.71, 0.98]} == dic)
        
    def test_create_ranges_set_biggest_percent(self):
        a = Agent("1", "",0.98, 0.7, 0.5, 0.1)
        dic = a.create_ranges(0.88, 0.7, 0.5, 0.1)
        assert (a.biggest_percent == 0.88)

    #-------------------------------------------------------------------------- 
       
    def test_throw_die_0_100(self):
         a = Agent("1", "",0.98, 0.7, 0.5, 0.1)
         die = a.throw_die(0,1)
         
         assert( 0 <= die <= 1 )

    def test_throw_die_26_57(self):
         a = Agent("1", "",0.98, 0.7, 0.5, 0.1)
         die = a.throw_die(0.26,0.57)
         assert( 0.26 <= die <= 0.57 ) 
         
    #--------------------------------------------------------------------------         
    def test_is_in_range_for_first_percent_limit1(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        
        assert( a.is_in_range(0, 0.51) == True)  
        
    def test_is_in_range_for_first_percent_limit2(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        
        assert( a.is_in_range(0, 0.70) == True) 
        
    def test_is_in_range_for_first_percent_bwtween_range(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        
        assert( a.is_in_range(0, 0.63)  == True)   
        
    def test_is_in_range_for_first_percent_out_range(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        assert( a.is_in_range(0, 0.75)  == False) 
        
    #--------------------------------------------------------------------------
    def test_is_in_range_for_second_percent_limit1(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        
        assert( a.is_in_range(1, 0.21) == True)  
        
    def test_is_in_range_for_second_percent_limit2(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        
        assert( a.is_in_range(1, 0.5) == True) 
        
    def test_is_in_range_for_second_percent_bwtween_range(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        assert( a.is_in_range(1, 0.30)  ==True ) 
         
    def test_is_in_range_for_second_percent_out_range(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        assert( a.is_in_range(1, 0.75)  == False)

    #--------------------------------------------------------------------------
    def test_is_in_range_for_third_percent_limit1(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        
        assert( a.is_in_range(2, 0.71) == True)  
        
    def test_is_in_range_for_third_percent_limit2(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        
        assert( a.is_in_range(2, 0.9) == True) 
        
    def test_is_in_range_for_third_percent_bwtween_range(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        assert( a.is_in_range(2 , 0.85)  ==True ) 
         
    def test_is_in_range_for_third_percent_out_range(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        assert( a.is_in_range(2, 0.5)  == False) 

    #--------------------------------------------------------------------------
    
    def test_is_in_range_for_fourth_percent_limit1(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        assert( a.is_in_range(3, 0) == True)  
        
    def test_is_in_range_for_fourth_percent_limit2(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        assert( a.is_in_range(3, 0.2) == True) 
        
    def test_is_in_range_for_fourth_percent_bwtween_range(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        assert( a.is_in_range(3 , 0.1)  ==True ) 
         
    def test_is_in_range_for_fourth_percent_out_range(self):
        a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
        assert( a.is_in_range(3, 0.4)  == False)

    #--------------------------------------------------------------------------
    
    
           