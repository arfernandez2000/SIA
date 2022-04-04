import math
import random
from config_loader import truncated_k, boltzman_k, T0, Tc

LENGTH_FINAL = 100

def elite(l, backpack):
    l.sort(key = backpack.getFitness, reverse = True)
    return l[0:LENGTH_FINAL]

def get_q(p_i_list, divisor):
    q = []
    aux = 0
    for i in range(0, len(p_i_list)):
        aux = aux + (p_i_list[i] / divisor)
        q.append(aux)
    return q
        
def selection_method(individuals, p_i_list, divisor, length, addZero = False):
    p_i_list = [0] + p_i_list if addZero else p_i_list
    q_list = get_q(p_i_list, divisor)
    len_p_i_list = len(p_i_list)
    i = 1
    res = set()
    while (len(res) < length):
        if (i == len_p_i_list):
            i = 1
        r = random.uniform(0,1)
        if (q_list[i-1] < r and r <= q_list[i]):
            index = i - 1 if addZero else i
            res.add(individuals[index])
        i += 1
    return list(res)

def ruleta(individuals, backpack, P):
    f_list = []
    sumFit = 0
    for i in range (P):
        f_list.append(backpack.getFitness(individuals[i]))
        sumFit += f_list[i]
    res = selection_method(individuals, f_list, sumFit, P / 2, addZero=True)
    return res

def rank(individuals, backpack, P):
    sumfit = 0
    individuals.sort(key = backpack.getFitness, reverse = True)
    length = P
    f_i_list = []
    for i in range(0, length):
        fit_inv = (length - i) / length 
        f_i_list.append(fit_inv)
        sumfit += fit_inv
    res = selection_method(individuals, f_i_list, sumfit, length / 2)
    return res

def tournament(list, backpack, P):
    stopper = P/2
    winners = []
    while len(winners) < stopper:
        u = random.uniform(0.5,1)
        competitors = random.sample(list, 4)
        pair_one = competitors[:2]
        pair_two = competitors[2:]
        r = random.uniform(0,1)
        final = []
        pairs = [pair_one, pair_two, final]
        for p in pairs:
            first_fit = backpack.getFitness(p[0])
            second_fit = backpack.getFitness(p[1])
            best_fit = p[1] if second_fit > first_fit else p[0]
            worst_fit = p[1] if second_fit <= first_fit else p[0]
            if r < u:
                final.append(best_fit)
            else:
                final.append(worst_fit)
        winners.append(final[-1])

    return winners

def truncated(list, backpack,P):
    list.sort(key = backpack.getFitness)
    list_truncated = list[truncated_k: len(list)]
    return tournament(list_truncated, backpack, P)

def t_function(k,gen): 
    return Tc+(T0-Tc)*math.exp(-k*gen)

def boltzman(individuals, backpack, gen, P):
    sumFit = 0
    ve_list = []
    temp = t_function(boltzman_k,gen)
    for i in range(0, P):
        aux_fit = backpack.getFitness(individuals[i]) / 100
        ve_i = math.exp(aux_fit/temp)
        ve_list.append(ve_i)
        sumFit += ve_i
    
    return selection_method(individuals, ve_list, sumFit, P / 2, addZero = True)

def boltzmann(individuals, backpack, gen, P):
    val = t_function(boltzman_k,gen)
    probabilities = []
    population_sum = sum(list(map(lambda individual: math.exp(backpack.getFitness(individual)/val), individuals)))/len(individuals)
    for individual in enumerate(individuals):
        relative_fitness = math.exp(individual.fitness/val)/population_sum
        probabilities.append(relative_fitness)

    return selection_method(individuals,probabilities,population_sum,P/2,addZero=True)