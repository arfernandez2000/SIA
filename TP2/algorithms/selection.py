from turtle import back
from backpack import Backpack
import random
from typing import Tuple

LENGTH_FINAL = 100
def selection(List, int):
    print("hola")

def elite(l, backpack):
    aux = list(l)
    aux.sort(key = backpack.getFitness, reverse = True)
    return set(aux[0:LENGTH_FINAL])
    #NO FUNCIONAAA LPM, 

def ruleta(list, backpack):
    res = set()
    sums = []
    sumFit = 0
    
    for i in range (len(list)):
        sums.append(backpack.getFitness(list[i]))
        sumFit += sums[i]
        
    len_sums = len(sums)
    P = len(list) / 2
    i = 1
    q_i = 0
    q_iplusone = sums[0] / sumFit

    while (len(res) < P):
        if (i == len_sums):
            i = 1
            q_i = 0
            q_iplusone = sums[0] / sumFit

        q_i += sums[i-1] / sumFit
        q_iplusone += sums[i] / sumFit
        r = random.uniform(0,1)

        if (q_i < r and q_iplusone >= r):
            res.add(list[i-1])
        i += 1

    return [*res, ]

def rank(l, backpack):
    aux = list(l)
    sumfit = 0
    aux.sort(key = backpack.getFitness, reverse = True)
    print(aux)
    P = len(l) /2
    p_rank = []
    for i in range(len(aux)):
        fit_inv = (P - i)/P
        p_rank.append(fit_inv)
        sumfit +=fit_inv
    
    
    return random.choices(population = aux, weights=p_rank, k=100)

    #TO DO : AGREGAR LO DE RULETA


def tournament(List, backpack):
    i = 0

def boltzman(List, backpack):
    i = 0

def truncated(list, k, backpack):
    fitness = []
    for i in range (len(list)):
        fitness.append(backpack.getFitness(list[i]), list[i])
    fitness.sort()
    list_truncated = fitness[k: len(list)]

    #TO DO: HAY QUE LLAMAR A ALGUNO DE LOS OTROS METODOS. DESPUES DEFINIMOS CUAL

