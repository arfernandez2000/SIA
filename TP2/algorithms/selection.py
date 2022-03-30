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
    res = []
    sumFit = 0
    sums = []
    fitness = []
    
    for i in range(0, len(list)):
        sums[i] = Backpack.getFitness(list[i])
        sumFit += sums[i]
    P = len(list) / 2
    i = 0
    q_j = sums[0] / sumFit
    q_jplusone = q_j + sums[1] / sumFit
    while (len(res) != P):
        if (i == len(list) - 2):
            i = 0
        p_i = sums[i] / sumFit
        p_iplusone = sums[i+1]/sumFit
        r = random.uniform(0,1)
        if r > q_j and r <= q_jplusone:
            res.add(list[i])
        i += 1
        q_j = q_jplusone
        q_jplusone =  q_j + sum[i+1] / sumFit
    return res

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

