import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from get_data import data
from utils import get_winner_neuron

def plot_map(k,grid,countries):
    values = np.zeros((k,k), int)
    
    index = 0
    for entrie in data:
        min_position = (None,None)
        min_dist = 999
        for row in grid:
            for col in row:
                w = col.weights
                dist = np.linalg.norm(entrie-w)
                if dist < min_dist:
                    min_position = col.position
                    min_dist = dist
        grid[min_position[0], min_position[1]].count += 1
        grid[min_position[0], min_position[1]].add_element(countries[index])
        values[min_position[0], min_position[1]] += 1
        index += 1
        
    i = 0
    for col in grid:
        for j in range(len(col)):
            print('Neurona (',i,',',j,') tiene a: ', grid[i][j].elements)
        i += 1

    fig, ax = plt.subplots(figsize=(20,10))

    for col in grid:
        for neuron in col:
            i, j = neuron.position[0], neuron.position[1]
            step = 1 / (len(neuron.elements) - 0.2) if len(neuron.elements) > 0 else 0
            i = 0.4 if len(neuron.elements) == 1 else i
            for e in neuron.elements:
                text = ax.text(j + 0.2,i+0.01, e,
                                ha="center", va="center", color="r")
                i += step
    sns.heatmap(values, annot=True, center=0, ax=ax, cmap='summer')
    plt.show()