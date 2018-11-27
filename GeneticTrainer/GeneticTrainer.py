import operator
import random
import copy
from Agent.Agent import Agent
from Connect4.Connect4 import Connect4
from NameRandomizer.NameGenerator import get_random_name


def mutate(individual: Agent, probability) -> Agent:
    """
    :param individual:
    :return:
    """
    random.seed()
    dies = random.randint(1,100)
    if dies <= probability:
        index = random.randint(0, 3)

        current_first = individual.percent_first_move
        current_second = individual.percent_second_move
        current_third = individual.percent_third_move
        current_fourth = individual.percent_fourth_move

        percents = [current_first, current_second, current_third, current_fourth]
        limits = [0] + percents + [100]
        percents[index] = round(random.uniform(limits[index], limits[index+2]), 2)

        [individual.percent_first_move,
         individual.percent_second_move,
         individual.percent_third_move,
         individual.percent_fourth_move] = percents

    return individual


class GeneticTrainer:
    def __init__(self, preserved_individuals_amount, number_of_generations):
        self.population = []
        self.preserved_individuals_amount = preserved_individuals_amount
        self.number_of_generations = number_of_generations
        self.best_individual = None
        self.mutation_probability = 8 # 8%

    def get_best_configuration_params(self) -> list:
        """
        :return:
        """
        self.genetic_algorithm()
        first_param = self.best_individual.percent_first_move
        second_param = self.best_individual.percent_second_move
        third_param = self.best_individual.percent_third_move
        fourth_param = self.best_individual.percent_fourth_move
        return [first_param, second_param, third_param, fourth_param]

    def generate_population(self, population_size) -> list:
        """
        :return:
        """
        for i in range(0, population_size):
            random.seed()
            first_percent = round(random.uniform(0,0.25), 2)
            second_percent = round(random.uniform(first_percent,0.5), 2)
            third_percent = round(random.uniform(second_percent,0.75), 2)
            fourth_percent = round(random.uniform(third_percent,1), 2)
            self.population.append(Agent("1", get_random_name(),
                                         first_percent, second_percent, third_percent, fourth_percent))
        return self.population

    def get_fitness(self, individual: Agent) -> int:
        """
        :param individual: instance of Agent
        :return: the amount of WINS the Agent already has set in its attribute
        :rtype: int
        """
        return individual.record[individual.WINS]

    def reproduce(self, parent1: Agent, parent2: Agent) -> [Agent, Agent]:
        """
        :param parent1:
        :param parent2:
        :return:
        """
        random.seed()

        parent1_params = parent1.percent_first_move, \
                         parent1.percent_second_move, \
                         parent1.percent_third_move, \
                         parent1.percent_fourth_move \

        parent2_params = parent2.percent_first_move, \
                         parent2.percent_second_move, \
                         parent2.percent_third_move, \
                         parent2.percent_fourth_move

        index = random.randint(1, 3)
        child1_params = parent1_params[:index] + parent2_params[index:]
        child2_params = parent2_params[:index] + parent1_params[index:]
        child1 = Agent("1", get_random_name(), 0, 0, 0, 0)
        child2 = Agent("2", get_random_name(), 0, 0, 0, 0)
        child1.percent_first_move, \
        child1.percent_second_move, \
        child1.percent_third_move, \
        child1.percent_fourth_move = child1_params

        child2.percent_first_move, \
        child2.percent_second_move, \
        child2.percent_third_move, \
        child2.percent_fourth_move = child2_params
        return [child1, child2]

    def genetic_algorithm(self):
        """
        :return:
        """

        preserved_individuals = []

        for i in range(0, self.number_of_generations):
            generation_fitness = {}
            self.population = self.generate_population((self.preserved_individuals_amount * 10) - len(preserved_individuals))
            self.population.append(preserved_individuals)
            preserved_individuals = []

            for individual in self.population:
                opponents = self.population.copy()
                opponents.remove(individual)
                individual = self.train(individual, opponents)
                generation_fitness[individual] = self.get_fitness(individual)

            best_fitting_individuals = self.get_N_best_fitting(generation_fitness, self.preserved_individuals_amount)
            best_fitting_pairs = make_pairs(best_fitting_individuals)
            children = []

            for parent1, parent2 in best_fitting_pairs:
                parent1_copy = copy.deepcopy(parent1)
                parent2_copy = copy.deepcopy(parent2)

                children = self.reproduce(parent1_copy, parent2_copy)
                children[0] = mutate(children[0], self.mutation_probability)
                children[1] = mutate(children[0], self.mutation_probability)
                preserved_individuals.append(children)
                children = []

                self.population.remove(parent1)
                self.population.remove(parent2)
                del generation_fitness[parent1]
                del generation_fitness[parent2]

            for new_child in children:
                opponents = self.population.copy()
                opponents.remove(new_child)
                new_child = self.train(new_child, opponents)
                generation_fitness[new_child] = self.get_fitness(new_child)

        self.population.append(preserved_individuals) # for final iteration
        self.best_individual = self.get_N_best_fitting(generation_fitness, 1)
        return self.best_individual



    def train(self, individual: Agent, opponents: list):
        individual.character = "1"
        for opponent in opponents:
            opponent.character = "2"
            players = [individual, opponent]
            game = Connect4('cls')
            game.default()
            game.game_mode = game.game_modes[0]
            [individual, _] = game.logic_play(players=players)
        return individual

    def get_N_best_fitting(self, population: dict, n):
        """
        :param population:
        :param n:
        :return:
        """
        bests = []
        for i in range(0, n):
            best_now = max(population.items(), key=operator.itemgetter(1))[0]
            bests.append(best_now)
            del population[best_now]
        return bests


def make_pairs(elements: list, n=2):
    return zip(*[iter(elements)] * n)


agent1 = Agent("1", get_random_name(), 15,30, 60, 90)
#mutated_agent1 = mutate(agent1)
#print("Agent1 - 1st: ", agent1.percent_first_move, " 2nd: ", agent1.percent_second_move, " 3rd: ", agent1.percent_third_move, " 4th: ", agent1.percent_fourth_move)
agent2 = Agent("2", get_random_name(), 0, 0, 0, 0)

'''
players = [agent1, agent2]
game = Connect4('cls')
game.default()
game.game_mode = game.game_modes[0]
[agent1, agent2] = game.logic_play(players=players)
print("Agent1:", agent1.name, " Wins: ", agent1.record[agent1.WINS], " DRAWS: ", agent1.record[agent1.DRAWS], " Loses: ", agent1.record[agent1.LOSSES])
print("Agent2:", agent2.name, " Wins: ", agent2.record[agent2.WINS], " DRAWS: ", agent2.record[agent2.DRAWS], " Loses: ", agent2.record[agent2.LOSSES])
'''