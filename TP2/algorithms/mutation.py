from TP2.backpack import Chromosome
from typing import List
from random import random

def mutation(individuals: List[Chromosome], p):
    if (p < 0 or p > 1):
        raise Exception('probability must be greater or equal than 0 and smaller or equal than 1')
    for i in range(len(individuals)):
        r = random()
        if (r < p):
            aux = individuals[i][0]
            newChrom = (not aux, individuals[i][1])
            individuals[i] = newChrom