from typing import List, Tuple
from random import random

from main import backpack
from backpack import Chromosome

def get_random_population(P, prob):
    population = set()
    capacity = backpack.getCapacity()
    for i in range(P):
        chromosome = [False] * capacity
        for i in range(capacity):
            if random() < prob:
                chromosome[i] = True
        population.add(tuple(chromosome))
    
    return population

def select_two_by_fitness(population):
    # A TERMINAR
    return population.pop(), population.pop()

def genetic_algorithm(P, prob, crossbreed, mutation, selection, stop, n=0):
    population = get_random_population(P,prob)

    while not stop(population):
        new_population = set()
        aux_population = population.copy()
        while new_population.__len__ < P:
            one, two = select_two_by_fitness(aux_population)
            child_one, child_two = crossbreed(one,two, n)
            child_one = mutation(child_one)
            child_two = mutation(child_two)
            new_population.add(child_one)
            new_population.add(child_two)
        total_population = population.union(new_population)
        population = selection(total_population)

    return population