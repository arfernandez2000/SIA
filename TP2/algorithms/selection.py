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
    q_i_minus_one = 0
    q_i = p_i_list[0] / divisor
    res = set()
    while (len(res) < P):
        if (i == len_p_i_list):
            i = 1
            q_i_minus_one = 0
            q_i = p_i_list[0] / divisor

        q_i_minus_one += p_i_list[i-1] / divisor
        q_i += p_i_list[i] / divisor
        r = random.uniform(0,1)

        if (q_i_minus_one < r and r <= q_i):
            res.add(list[i])
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
    P = len(l) /2
    p_rank = []
    for i in range(len(aux)):
        fit_inv = (P - i)/P
        p_rank.append(fit_inv)
        sumfit += fit_inv
    
    res = q_selection(l, p_rank, sumfit, P)
    return res

def tournament(list, backpack):
    P = len(list)/2
    winners = []
    while len(winners) < P:
        u = random.uniform(0.5,1)
        competitors = random.sample(list, 4)
        pair_one = competitors[:2]
        pair_two = competitors[2:]
        r = random.uniform(0,1)
        final = []
        pairs = [pair_one, pair_two, final]
        for p in pairs:
            first_fit = backpack.getFitness(p[0])
            print("FIRST", first_fit)
            second_fit = backpack.getFitness(p[1])
            print("SECOND", second_fit)
            best_fit = p[1] if second_fit > first_fit else p[0]
            worst_fit = p[1] if second_fit <= first_fit else p[0]
            print("BEST",backpack.getFitness(best_fit))
            if r < u:
                final.append(best_fit)
            else:
                final.append(worst_fit)
        winners.append(final[-1])
    print("WINNERS", winners)
    print("LEN WINNERS", len(winners))
    return winners

def boltzman(l, backpack):
    pass

def truncated(list, k, backpack):
    fitness = []
    for i in range (len(list)):
        fitness.append(backpack.getFitness(list[i]), list[i])
    fitness.sort()
    list_truncated = fitness[k: len(list)]

    #TO DO: HAY QUE LLAMAR A ALGUNO DE LOS OTROS METODOS. DESPUES DEFINIMOS CUAL

