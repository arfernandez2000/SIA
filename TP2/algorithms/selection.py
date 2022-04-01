import math
import random

LENGTH_FINAL = 100
def selection(List, int):
    print("hola")

def elite(l, backpack):
    aux = list(l)
    aux.sort(key = backpack.getFitness, reverse = True)
    return set(aux[0:LENGTH_FINAL])

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

    return res

def ruleta(individuals, backpack):
    f_list = []
    sumFit = 0
    length = len(individuals)
    for i in range (length):
        f_list.append(backpack.getFitness(individuals[i]))
        sumFit += f_list[i]
    res = selection_method(individuals, f_list, sumFit, length / 2, addZero=True)
    return res

def rank(individuals, backpack):
    aux = list(individuals)
    sumfit = 0
    aux.sort(key = backpack.getFitness, reverse = True)
    length = len(individuals)
    f_i_list = []
    for i in range(0,len(aux)):
        fit_inv = (length - i) / length 
        f_i_list.append(fit_inv)
        sumfit += fit_inv
    
    res = selection_method(aux, f_i_list, sumfit, length / 2)
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
            second_fit = backpack.getFitness(p[1])
            best_fit = p[1] if second_fit > first_fit else p[0]
            worst_fit = p[1] if second_fit <= first_fit else p[0]
            if r < u:
                final.append(best_fit)
            else:
                final.append(worst_fit)
        winners.append(final[-1])
    return winners

Tc = 5
T_0 = 100
generation = 0
def t_function(k,gen):
    return Tc + (T_0 - Tc) * math.pow(math.e, -k*gen)

def boltzman(individuals, backpack, gen):
    sumFit = 0
    length = len(individuals)
    ve_list = []
    fitnessList = [backpack.getFitness(x) for x in individuals]
    temp = t_function(1,gen)
    for i in range(0, length):
        print(fitnessList[i])
        ve_i = math.pow(math.e,fitnessList[i]) / temp
        ve_list.append(ve_i)
        sumFit += ve_i
    
    return selection_method(individuals, ve_list, sumFit, length / 2, addZero = True)


def truncated(list, k, backpack):
    fitness = []
    for i in range (len(list)):
        fitness.append(backpack.getFitness(list[i]), list[i])
    fitness.sort()
    list_truncated = fitness[k: len(list)]

    #TO DO: HAY QUE LLAMAR A ALGUNO DE LOS OTROS METODOS. DESPUES DEFINIMOS CUAL

