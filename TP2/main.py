from backpack import Backpack, Elem
from typing import List
from algorithms.genetic_algorithm import *
from algorithms.selection import *
from config_loader import file, P, mutation_prob, selection_name
from graphic import draw

maxWeight: int
maxItems : int
elems: List[Elem] = []

with open(file, 'r') as f:
    line = f.readline()
    count: int = 0

    while line != '\n':
        aux: List[str] = line.split()

        if count ==0:
            maxItems = int(aux[0])
            maxWeight = int(aux[1])
        else:
            elem = Elem(int(aux[0]), int(aux[1]))
            elems.append(elem)
        count+=1
        line = f.readline()
        
    f.close()

selection_method_dic = {
    'ruleta': ruleta,
    'boltzman': boltzman,
    'elite': elite,
    'tournament': tournament,
    'rank': rank,
    'truncated': truncated
}

selection = selection_method_dic.get(selection_name)
backpack = Backpack(maxItems, maxWeight,elems)

def stop(lastUpdate, gen):
    return lastUpdate == unchanged_gens or gen == max_gens

last_population = genetic_algorithm(backpack, P, 0.2, mutation_prob, selection, stop)

fitness_values = []

optimo = last_population.pop()
for popu in last_population:
    fit = backpack.getFitness(popu)
    fitness_values.append(fit)
    if backpack.getFitness(optimo) < fit:
        optimo = popu

weight = backpack.getWeight(optimo)
benefit = backpack.getBenefit(optimo)

print("Optimo: ", optimo)
print("Weight: ", weight)
print("Beneficio: ", benefit)
draw(fitness_values, weight, benefit)