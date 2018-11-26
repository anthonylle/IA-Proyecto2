"""
    tests GeneticTrainer Class
"""
from Agent.Agent import Agent
from GeneticTrainer.GeneticTrainer import mutate, GeneticTrainer
from NameRandomizer.NameGenerator import get_random_name
from Connect4.Connect4 import Connect4


def test_mutate():
    individual = Agent("1", get_random_name(), 15, 30, 60, 90)
    original_params = [individual.percent_first_move,
                       individual.percent_second_move,
                       individual.percent_third_move,
                       individual.percent_fourth_move]
    mutated = mutate(individual, 100)
    mutated_params = [mutated.percent_first_move,
                      mutated.percent_second_move,
                      mutated.percent_third_move,
                      mutated.percent_fourth_move]

    assert(original_params != mutated_params)


def test_reproduce():
    trainer = GeneticTrainer(10, 100)
    parent1 = Agent("1", get_random_name(), 15, 30, 60, 90)
    parent2 = Agent("2", get_random_name(), 5, 20, 50, 80)
    child1, child2 = trainer.reproduce(parent1, parent2)

    parent1_params, parent2_params = [15, 30, 60, 90], [5, 20, 50, 80]
    child1_params = [child1.percent_first_move,
                     child1.percent_second_move,
                     child1.percent_third_move,
                     child1.percent_fourth_move]
    child2_params = [child2.percent_first_move,
                     child2.percent_second_move,
                     child2.percent_third_move,
                     child2.percent_fourth_move,]

    assert(parent1_params != child1_params and parent2_params != child2_params)


def test_generate_population():
    empty_population = []
    trainer = GeneticTrainer(10, 100)
    actual_population = trainer.generate_population(100)
    assert (empty_population != actual_population and len(actual_population) == 100)


def test_agents_play_a_game():
    agent1 = Agent("1", get_random_name(), 0, 0, 0, 0)
    agent2 = Agent("2", get_random_name(), 0, 0, 0, 0)
    players = [agent1, agent2]
    game = Connect4('cls')
    game.default()
    game.game_mode = game.game_modes[0]
    [agent1, agent2] = game.logic_play(players=players)
    assert((agent1.record[agent1.WINS] == 0 or agent1.record[agent1.DRAWS] == 0) and
           (agent2.record[agent2.WINS] == 0 or agent2.record[agent2.DRAWS] == 0))
