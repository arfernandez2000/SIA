from typing import List
from random import random

def mutation(individual, p):
    if (p < 0 or p > 1):
        raise Exception('probability must be greater or equal than 0 and smaller or equal than 1')
    indt = list(individual)
    for i in range(len(individual)):
        r = random()
        if (r < p):
            aux = indt[i]
            indt[i] = not aux
    return tuple(indt)