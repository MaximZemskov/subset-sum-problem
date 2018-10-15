import numpy
from cached_property import cached_property


class Individual:
    def __init__(self, array, desired_number, individ=None):
        self.array = array
        self.desired_number = desired_number
        if individ is None:
            self.encoded_individual = numpy.random.choice([0, 1], size=len(array), p=[.9, .1])
        else:
            self.encoded_individual = individ

    def mutation_chance(self):
        return 0.3

    @property
    def individual(self):
        return self.encoded_individual

    @property
    def decoded_individual(self):
        decoded = []
        for e_value, d_value in zip(self.individual, self.array):
            if e_value:
                decoded.append(d_value)
        return decoded

    @property
    def fitness(self):
        fitness = sum(self.decoded_individual)/self.desired_number
        return fitness if fitness <= 1 else 0

    def mutate(self):
        for idx, value in enumerate(self.individual):
            toss = numpy.random.random_sample() <= self.mutation_chance
            if toss:
                if not value:
                    self.individual[idx] = 1
                self.individual[idx] = 0



