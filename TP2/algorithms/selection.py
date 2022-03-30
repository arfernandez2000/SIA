from backpack import Backpack
import random

LENGTH_FINAL = 100
def selection(List, int):
    print("hola")

def elite(list):
    fitness = []
    
    for i in range (len(list)):
        fitness.append(Backpack.getFitness(list[i]))
    fitness.sort(reverse=True)
    return sorted(list, key=fitness,reverse=True)[0:LENGTH_FINAL]

    #NO FUNCIONAAA LPM, 

def ruleta(list):
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

def rank(list):
    fitness = []
    for i in range (len(list)):
        fitness.append(Backpack.getFitness(list[i]), list[i])
    fitness.sort(reverse=True)
    P = len(list) /2
    p_rank = []
    for i in range(len(list)):
        p_rank.append((P - fitness[i]) / P)
    
    return random.choices(population = fitness, weights=p_rank, k=100)

    #TO DO : AGREGAR LO DE RANKING


def tournament(List):
    i = 0

def boltzman(List):
    i = 0

def truncated(list, k):
    fitness = []
    for i in range (len(list)):
        fitness.append(Backpack.getFitness(list[i]), list[i])
    fitness.sort()
    list_truncated = fitness[k: len(list)]

    #TO DO: HAY QUE LLAMAR A ALGUNO DE LOS OTROS METODOS. DESPUES DEFINIMOS CUAL

