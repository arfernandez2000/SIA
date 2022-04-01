from backpack import Backpack, Elem
from typing import List
from algorithms.genetic_algorithm import *
from algorithms.selection import *
import json

maxWeight: int
maxItems : int
elems: List[Elem] = []

f = open('./config.json')
data = json.load(f)
P = data['P']
file = data['file']
mutation_prob = data['mutation_prob']
selection_name = data['selection']['method']
crossover_name = data['crossover']['method']
crossover_points = data['crossover']['points']
unchanged_gens = data['stop']['unchanged_generations']
max_gens = data['stop']['max_generations']

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


backpack = Backpack(maxItems, maxWeight,elems)
last_population = genetic_algorithm(backpack, P, 0.2, mutation_prob, elite, crossover_points)

optimo = last_population.pop()
for popu in last_population:
    if backpack.getFitness(optimo) < backpack.getFitness(popu):
        optimo = popu
print("Optimo: ", optimo)
print("Weight: ", backpack.getWeight(optimo))
print("Beneficio: ", backpack.getBenefit(optimo))
