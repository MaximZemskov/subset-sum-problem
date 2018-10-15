import numpy
import logging

from individ import Individual


class Population:
    def __init__(self, array, desired_number, size=1000):
        self.array = array
        self.desired_number = desired_number
        self.size = size
        self.survivals_size = int(self.size * 0.15)
        self.mutants_size = int(self.size * 0.3)
        self.childs_size = int(self.size * 0.3)
        self._population = []

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value

    @property
    def roulette_boarders(self):
        borders = []
        denominator = sum([x.fitness for x in self.population])
        prev_arc = 0
        for individual in self.population:
            arc = individual.fitness/denominator
            borders.append((prev_arc, prev_arc + arc))
            prev_arc = prev_arc + arc
        return borders

    @property
    def alpha(self):
        return sorted(self.population, key=lambda x: x.fitness)[-1]

    def start_armageddon(self):
        print('drop meteor\nbabah!!')
        self.initialization()

    def initialization(self):
        self._population = []
        for _ in range(self.size):
            self.population.append(Individual(self.array, self.desired_number))

    def crossover(self, first_parent, second_parent):
        pivot = numpy.random.random_integers(0, len(first_parent) - 1)
        tmp = second_parent[:pivot].copy()
        second_parent[:pivot], first_parent[:pivot] = first_parent[:pivot], tmp
        toss = numpy.random.random_sample()
        if toss >= 0.5:
            return Individual(self.array, self.desired_number, second_parent)
        return Individual(self.array, self.desired_number, first_parent)

    def get_parent(self):
        toss = numpy.random.random_sample()
        for idx, (low_border, high_border) in enumerate(self.roulette_boarders):
            if high_border >= toss >= low_border:
                return self.population[idx].individual

    def breed(self):
        childs = []
        for _ in range(self.childs_size):
            first_parent = self.get_parent()
            second_parent = self.get_parent()
            childs.append(self.crossover(first_parent, second_parent))
        return childs

    def get_survivals(self):
        survivals = []
        for _ in range(self.survivals_size):
            toss = numpy.random.random_sample()
            for idx, (low_border, high_border) in enumerate(self.roulette_boarders):
                if high_border >= toss >= low_border:
                    survivals.append(self.population[idx])
        return survivals

    def mutation(self):
        for _ in range(self.mutants_size):
            idx = numpy.random.random_integers(0, self.size - 1)
            self.population[idx].mutate()

    def selection(self):
        if self.alpha.fitness == 1:
            return True
        new_population = []
        survivals = self.get_survivals()
        childs = self.breed()
        new_population.extend(survivals)
        new_population.extend(childs)
        self._population = survivals + childs
        while len(new_population) != self.size:
            #  add new individuals
            new_population.append(Individual(self.array, self.desired_number))
        self._population = new_population
        self.mutation()
        return False






