import numpy as np
from get_data import data

def set_init_weights(k):
    w = []
    for _ in range(0,k*k):
      i = np.random.randint(len(data))
      wi = data[i]
      w.append(wi)
    return np.array(w)
  
def update_neighborhood_weight(weights, radius, w_k):
  umbral = weights[w_k]
  res = []
  for i in range(len(weights)):
    if i != w_k and np.linalg.norm(weights[i] - umbral) < radius:
      res.append(i)
  return np.array(res)

# def get_winner_neuron(grid,x):
#   aux = []
#   for row in grid:
#     for neu in row:
#         aux.append(np.linalg.norm(x-neu.weights))
#   aux = np.array(aux)
#   w_k = np.argmin(aux)
#   return w_k

def get_winner_neuron(x,weights):
  aux = list(map(lambda wi: np.linalg.norm(x-wi), weights))
  aux = np.array(aux)
  w_k = np.argmin(aux)
  return w_k