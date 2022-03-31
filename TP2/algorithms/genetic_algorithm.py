from typing import List, Tuple
from random import random
from algorithms.mutation import *
from algorithms.crossbreed import *

def get_random_population(P, prob, backpack):
    population = set()
    capacity = backpack.getCapacity()
    while len(population) < P:
        chromosome = [False] * capacity
        for i in range(capacity):
            if random.uniform(0, 1) < prob:
                chromosome[i] = True
        individual = tuple(chromosome)
        print(backpack.getWeight(individual))
        population.add(individual)
    print("POPULATION", population)
    return population

def select_two_by_fitness(population):
    # A TERMINAR
    return population.pop(), population.pop()

def stop(lastFitness, lastUpdate, actualFitness):
    if(lastFitness - actualFitness < 0.00001):
        lastUpdate += 1
    else:
        lastUpdate =0
    return lastUpdate == 50

def genetic_algorithm(backpack, P, prob, pmutation, selection, n=0):
    gen =0
    population = get_random_population(P,prob, backpack)
    lastFitness =0
    lastUpdate =0
    actualFitness = backpack.getPopuFitness(population)

    while  not stop(lastFitness, lastUpdate, actualFitness) and gen< 20000:
        print("GEN", gen)
        gen += 1
        new_population = set()
        aux_population = list(population)
        aux_population.sort(key = backpack.getFitness)
        while len(new_population) < P:
            if(len(aux_population) < 2):
                aux_population = list(population)
            one, two = select_two_by_fitness(aux_population)
            child_one, child_two = crossbreed(one,two, n)
            child_one = mutation(child_one, pmutation)
            child_two = mutation(child_two, pmutation)
            new_population.add(child_one)
            new_population.add(child_two)
        total_population = population.union(new_population)
        population = set(selection(total_population, backpack))

    return population