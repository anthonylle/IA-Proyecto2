"""
    tests GeneticTrainer Class
"""
from Agent.Agent import Agent
from GeneticTrainer.GeneticTrainer import mutate, GeneticTrainer
from NameRandomizer.NameGenerator import get_random_name


def test_mutate():
    individual = Agent("1", get_random_name(), 10, 10, 10, 10)
    original_params = [individual.percent_first_move,
                       individual.percent_second_move,
                       individual.percent_third_move,
                       individual.percent_fourth_move]
    mutated = mutate(individual)
    mutated_params = [mutated.percent_first_move,
                      mutated.percent_second_move,
                      mutated.percent_third_move,
                      mutated.percent_fourth_move]

    assert(original_params != mutated_params)


def test_crossover():
    trainer = GeneticTrainer(10, 100)
    parent1 = Agent("1", get_random_name(), 1, 2, 3, 4)
    parent2 = Agent("2", get_random_name(), 100, 99, 98, 97)
    child1, child2 = trainer.crossover(parent1, parent2)

    parent1_params, parent2_params = [1, 2, 3, 4], [100, 99, 98, 97]
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
    assert (empty_population != actual_population)


