from Agent.Agent import Agent

"""
    tests Agent Class
"""
def test_create_ranges1():
    a = Agent("1", "",0.7, 0.5, 0.9, 0.2)
    
    dic = a.create_ranges(0.7, 0.5, 0.9, 0.2)
    assert ({3: [0, 0.2], 1: [0.21000000000000002, 0.5], 0: [0.51, 0.7], 2: [0.71, 0.9]} == dic)