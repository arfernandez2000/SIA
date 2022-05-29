import numpy as np
import sys

from tomlkit import boolean
from get_data import data, raw_data
from Neuron import Neuron
from plot import plot_map, plot_u_matrix
from utils import * 

def update_eta(t):
  return 1 / t

def update_radius(old_radius, t, adaptive):
  if adaptive:  
    return np.round(1 + (old_radius / t))
  else:
    return old_radius

def create_grid(k,weights):
  grid = np.empty((k,k), Neuron)
  index = 0
  for i in range(k):
      for j in range(k):
          grid[i][j] = Neuron(weights[index],0,(i,j))
          index += 1
  return grid

def kohonen(k = 3, init_radius = 2, adaptive_radius = False):
  #Paso Inicial: Inicializo valores
  countries = raw_data.values[:,0]
  weights = set_init_weights(k)
  radius = init_radius
  max_epochs = 10000 * k * k

  t = 1
  eta = update_eta(t)
  cut = False
  #Paso t
  while t < max_epochs and not cut:
    #Paso 1: Selecciono un registro de entrada Xp
    x_index = np.random.choice(range(data.shape[0]))
    x = data[x_index]
    
    #Paso 2: Encontrar la neurona ganadora
    w_k = get_winner_neuron(weights,x)
    
    #Paso 3: Actualizar los pesos de las neuronas vecinas
    n_k = update_neighborhood_weight(weights, radius, w_k, k)
    
    for j in range(k*k):
      if (j in n_k):
        weights[j] = weights[j] + eta * (x-weights[j])
    
    t += 1
    eta = update_eta(t)
    radius = update_radius(radius, t, adaptive_radius)
    
  grid = create_grid(k,weights)
  
  plot_map(k,grid,countries)
  plot_u_matrix(k,grid)

k = int(sys.argv[1]) if len(sys.argv) >= 2 else 3
radius = float(sys.argv[2]) if len(sys.argv) >= 3 else 1
adaptive_radius = True if len(sys.argv) >= 4 else False
kohonen(k=k,init_radius=radius, adaptive_radius=adaptive_radius)