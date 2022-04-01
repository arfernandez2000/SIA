from backpack import Backpack, Elem
from typing import List
from algorithms.genetic_algorithm import *
from algorithms.selection import *

maxWeight: int
maxItems : int
elems: List[Elem] = []

with open("./source/Mochila100Elementos.txt", 'r') as f:
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
last_population = genetic_algorithm(backpack, 100, 0.02, 0.3, boltzman, 3)

optimo = last_population.pop()
for popu in last_population:
    if backpack.getFitness(optimo) < backpack.getFitness(popu):
        optimo = popu
print("Optimo: ", optimo)
print("Weight: ", backpack.getWeight(optimo))
print("Beneficio: ", backpack.getBenefit(optimo))
