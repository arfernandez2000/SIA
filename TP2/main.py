from backpack import Backpack, Elem
from typing import List

maxWeight: int
maxItems : int
elems: List[Elem] = []

with open("./source/Mochila100Elementos.txt", 'r') as f:
    line = f.readline()
    count: int = 0

    while line:
        aux: List[str] = line.split()

        if count ==0:
            maxItems = aux[0]
            maxWeight = aux[1]
        else:
            elem = Elem(aux[0], aux[1])
            elems.append(elem)
        count+=1
        
    f.close()
    
backpack = Backpack(maxItems, maxWeight,elems)