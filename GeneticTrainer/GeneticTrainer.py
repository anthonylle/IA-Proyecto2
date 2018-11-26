import operator
import random
from Agent.Agent import Agent
from NameRandomizer.NameGenerator import get_random_name


def mutate(individual: Agent) -> Agent:
    """
    :param individual:
    :return:
    """
    random.seed()
    index = random.randint(0, 3)
    new_values = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]

    current_first = individual.percent_first_move
    current_second = individual.percent_second_move
    current_third = individual.percent_third_move
    current_fourth = individual.percent_fourth_move

    percents = [current_first, current_second, current_third, current_fourth]
    percents[index] = new_values[index]

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

    def get_best_configuration_params(self) -> list:
        """
        \:return:
        """
        return None

    def generate_population(self, population_size) -> list:
        """
        :return:
        """
        for i in range(0, population_size):
            random.seed()
            first_percent = random.randint(0, 100)
            second_percent = random.randint(0, 100)
            third_percent = random.randint(0, 100)
            fourth_percent = random.randint(0, 100)
            self.population.append(Agent("1", get_random_name(),
                                         first_percent, second_percent, third_percent, fourth_percent))
        return self.population

    def get_fitness(self, individual: Agent) -> int:
        """
        :param individual: instance of Agent
        :return: the amount of WINS the Agent already has set in its attribute
        :rtype: int
        """
        return individual.WINS

    def crossover(self, parent1: Agent, parent2: Agent) -> (Agent, Agent):
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
        return child1, child2

    def genetic_algorithm(self):
        """"
        :return:
        """
        self.population = self.generate_population(self.preserved_individuals_amount*10)
        for i in range(0, self.number_of_generations):
            generation_fitness = {}
            for individual in self.population:
                opponents = self.population.remove(individual)
                # train indiviual 1 vs the-world-now
                generation_fitness[individual] = self.get_fitness(individual)
            best_fitting_individuals = self.get_N_best_fitting(generation_fitness, self.preserved_individuals_amount)


    def train(self, individual: Agent, opponents: list):
        for opponent in opponents:

            print(individual, opponent)


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

