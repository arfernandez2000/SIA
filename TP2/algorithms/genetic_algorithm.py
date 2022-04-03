from random import random
import math
from algorithms.mutation import *
from algorithms.crossbreed import *
from config_loader import unchanged_gens, max_gens

def get_random_population(P, prob, backpack):
    population = []
    capacity = backpack.getCapacity()
    while len(population) < P:
        weight = backpack.getMaxWeight()
        indexes = list(range(0, capacity))
        chromosome = [False] * capacity
        while len(indexes) > 0:
            if len(indexes) != 1: 
                index = random.randint(0, len(indexes) - 1)
            else:
                index = 0
            elemWeight = backpack.getElemWeight(indexes[index])
            if elemWeight <= weight:
                chromosome[indexes[index]] = True
                weight -= elemWeight
            indexes.pop(index)
        individual = tuple(chromosome)
        population.append(individual)
    return population

def select_two_by_fitness(population):
    # A TERMINAR
    return population.pop(), population.pop()

def update(lastFitness, lastUpdate, actualFitness):
    print(lastUpdate)
    if(math.fabs(lastFitness - actualFitness) < 0.00001):
        lastUpdate += 1
    else:
        lastUpdate = 0
    return lastUpdate

def genetic_algorithm(backpack, P, prob, pmutation, selection, stop):
    gen = 0
    population = get_random_population(P,prob, backpack)
    lastFitness = 0
    lastUpdate = 0
    actualFitness = backpack.getPopuFitness(population)
    print(population)

    while not stop(lastUpdate, gen):
        gen += 1
        print('GEN')
        new_population = []
        aux_population = list(population)
        aux_population.sort(key = backpack.getFitness)
        while len(new_population) < P:
            if(len(aux_population) < 2):
                aux_population += list(population)
            one, two = select_two_by_fitness(aux_population)
            child_one, child_two = crossbreed(one,two,backpack)
            child_one = mutation(child_one, pmutation)
            child_two = mutation(child_two, pmutation)
            new_population.append(child_one)
            new_population.append(child_two)
        population += new_population
        print('POPLATION', len(population))
        if selection.__name__ == 'boltzman':
            population = selection(population, backpack, gen, len(population))
        elif selection.__name__ == 'elite':
            population = selection(population, backpack)
        else:
            print(selection.__name__)
            population = selection(population, backpack, len(population))
            print('popu')

        print("LENGTH POP DESPUES SELECTION", len(population))
        lastFitness = actualFitness
        actualFitness = backpack.getPopuFitness(population)
        lastUpdate = update(lastFitness, lastUpdate, actualFitness)

    return population