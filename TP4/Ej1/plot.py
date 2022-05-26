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

    fig, ax = plt.subplots(figsize=(20,10))

    plt.title('AGRUPACION DE PAISES')
    i = 0
    for col in grid:
        for j in range(len(col)):
            print('Neurona (',i,',',j,') tiene a: ', grid[i][j].elements)
        i += 1
                
    sns.heatmap(values, annot=True, center=3, ax=ax, cmap='summer',linewidths=.5)
    plt.show()

def get_neighbors(i,j):
  return [(i,j+1), (i+1,j), (i+1,j+1), (i,j-1), (i-1,j), (i-1,j-1), (i-1, j+1), (i+1, j-1)]


def plot_u_matrix(k,grid):
    u_values = np.zeros((k,k),float)

    for i in range(k):
        for j in range(k):
            w = grid[i,j].weights
            neighbors = get_neighbors(i,j)
            true_neighbors = 0
            distances = []
            for n in neighbors:
                x, y = n[0], n[1]
                if x >= 0 and y >= 0 and x < k and y < k:
                    neighbor_neuron_w = grid[x,y].weights
                    dist = np.linalg.norm(w-neighbor_neuron_w)
                    distances.append(dist)
                    true_neighbors += 1
            u_values[i][j] = (sum(distances)/true_neighbors)
            
    fig, ax = plt.subplots(figsize=(20,10))
    plt.title('MATRIZ U')
    sns.heatmap(u_values,cmap='summer',linewidths=.5, ax=ax)
    plt.show()