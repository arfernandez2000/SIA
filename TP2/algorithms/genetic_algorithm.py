from typing import List, Tuple
from random import random
from algorithms.mutation import *
from algorithms.crossbreed import *

def get_random_population(P, prob, backpack):
    population = set()
    capacity = backpack.getCapacity()
    print(capacity)
    print(type(capacity))
    while len(population) < P:
        chromosome = [False] * capacity
        for i in range(capacity):
            if random.random() < prob:
                chromosome[i] = True
        individual = tuple(chromosome)
        print(backpack.getWeight(individual))
        if(backpack.getWeight(individual) <= backpack.getMaxWeight()):
            print("ENTRE")
            population.add(individual)
    print("POPULATION", population)
    return population

def select_two_by_fitness(population):
    # A TERMINAR
    return population.pop(), population.pop()

def stop(population, generation):
    print("ENTRA")
    generation += 1
    return generation > 100

def genetic_algorithm(backpack, P, prob, pmutation, selection, n=0):
    gen =0
    population = get_random_population(P,prob, backpack)

    while gen < 100:
        print(gen)
        gen += 1
        new_population = set()
        aux_population = population.copy()
        while len(new_population) < P:
            one, two = select_two_by_fitness(aux_population)
            child_one, child_two = crossbreed(one,two, n)
            child_one = mutation(child_one, pmutation)
            child_two = mutation(child_two, pmutation)
            if(backpack.getWeight(child_one) <= backpack.getMaxWeight()):
                new_population.add(child_one)
            if(backpack.getWeight(child_two) <= backpack.getMaxWeight()):
                new_population.add(child_two)
        total_population = population.union(new_population)
        population = selection(total_population, backpack)

    return population