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

def q_selection(list, p_i_list, divisor, P):
    len_p_i_list = len(p_i_list)
    i = 1
    q_i = 0
    q_iplusone = p_i_list[0] / divisor
    res = set()
    while (len(res) < P):
        if (i == len_p_i_list):
            i = 1
            q_i = 0
            q_iplusone = p_i_list[0] / divisor

        q_i += p_i_list[i-1] / divisor
        q_iplusone += p_i_list[i] / divisor
        r = random.uniform(0,1)

        if (q_i < r and q_iplusone >= r):
            res.add(list[i-1])
        i += 1

    return [*res, ]

def ruleta(list, backpack):
    sums = []
    sumFit = 0
    
    for i in range (len(list)):
        sums.append(backpack.getFitness(list[i]))
        sumFit += sums[i]
    P = len(list) / 2
    res = q_selection(list, sums, sumFit, P)
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
    
    res = q_selection(l, p_rank, sumfit, P)
    return res

def tournament(list, backpack):
    u = random.uniform(0.5,1)
    competitors = random.sample(list, 4)
    pair_one = competitors[:2]
    pair_two = competitors[2:]
    r = random.uniform(0,1)
    winners = []
    pairs = [pair_one, pair_two, winners]
    for p in pairs:
        first_fit = backpack.getFitnes(p[0])
        second_fit = backpack.getFitness(p[1])
        best_fit = p[1] if second_fit > first_fit else p[0]
        worst_fit = p[1] if second_fit <= first_fit else p[0]

        if r < u:
            winners.append(best_fit)
        else:
            winners.append(worst_fit)

    return winners[-1]

def boltzman(List, backpack):
    i = 0

def truncated(list, k, backpack):
    fitness = []
    for i in range (len(list)):
        fitness.append(backpack.getFitness(list[i]), list[i])
    fitness.sort()
    list_truncated = fitness[k: len(list)]

    #TO DO: HAY QUE LLAMAR A ALGUNO DE LOS OTROS METODOS. DESPUES DEFINIMOS CUAL

