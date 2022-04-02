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
last_population = genetic_algorithm(backpack, P, 0.2, mutation_prob, selection)

fitness_values = []
gen = 0
gens = []

optimo = last_population.pop()
for popu in last_population:
    gens.append(gen)
    fitness_values.append(backpack.getFitness(popu))
    if backpack.getFitness(optimo) < backpack.getFitness(popu):
        optimo = popu
    gen += 1
print("Optimo: ", optimo)
print("Weight: ", backpack.getWeight(optimo))
print("Beneficio: ", backpack.getBenefit(optimo))
draw(gens, fitness_values)