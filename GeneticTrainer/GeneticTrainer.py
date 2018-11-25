import random
from Agent.Agent import Agent


class GeneticTrainer:

    def __init__(self, preserved_individuals_amount, number_of_generations):
        self.preserved_individuals_amount = preserved_individuals_amount
        self.number_of_generations = number_of_generations

    @property
    def get_best_configuration_params(self) -> list:
        return None

    def generate_population(self):
        self.population = []
        for i in range(0, self.number_of_generations):
            random.seed()
            first_percent = random.randint(0, 100)
            second_percent = random.randint(0, 100)
            third_percent = random.randint(0, 100)
            fourth_percent = random.randint(0, 100)
            self.population.append(Agent(first_percent, second_percent, third_percent, fourth_percent))

    def mutate(self, individual):
        return None

    def get_fitness(self, individual):
        return None