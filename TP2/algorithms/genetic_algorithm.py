from turtle import back
from typing import List, Tuple
from random import random
from algorithms.mutation import *
from algorithms.crossbreed import *

def get_random_population(P, prob, backpack):
    population = set()
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
        print("INDI WEIGHT", backpack.getWeight(individual))
        print("INDI BENEFIT", backpack.getBenefit(individual))
        population.add(individual)
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
    print(population)

    while gen < 500:
        print("GEN: ", gen)
        print("ACTUAL FITNESS: ", actualFitness)
        gen += 1
        new_population = set()
        aux_population = list(population)
        aux_population.sort(key = backpack.getFitness)
        while len(new_population) < P:
            if(len(aux_population) < 2):
                aux_population += list(population)
            one, two = select_two_by_fitness(aux_population)
            print("BEFORE")
            print(one)
            print(two)
            child_one, child_two = crossbreed(one,two, n, backpack)
            print("AFTER")
            print(child_one)
            print(child_two)
            child_one = mutation(child_one, pmutation)
            child_two = mutation(child_two, pmutation)
            new_population.add(child_one)
            new_population.add(child_two)
        total_population = population.union(new_population)
        population = set(selection(total_population, backpack))
        lastFitness = actualFitness
        actualFitness = backpack.getPopuFitness(population)
        print(population)

    return population