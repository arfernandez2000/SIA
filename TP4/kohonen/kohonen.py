import numpy as np
from get_data import data, raw_data
from Neuron import Neuron
from plot import plot_map, plot_u_matrix
from utils import * 

def update_eta(old_eta):
  return old_eta * 0.9

def update_radius(old_radius):
  return old_radius * 0.9

def kohonen(k = 3,init_eta = 0.1,init_radius = 2):
  #Paso Inicial: Inicializo valores
  p = len(raw_data)
  labels = raw_data.columns[1:]
  countries = raw_data.values[:,0]
  n = data.shape[1]

  weights = set_init_weights(k)
  grid = np.empty((k,k), Neuron)
  index = 0
  for i in range(k):
      for j in range(k):
          grid[i][j] = Neuron(weights[index],0,(i,j))
          index += 1

  eta = init_eta
  radius = init_radius
  max_epochs = 100

  t = 1
  cut = False
  #Paso t
  while t < max_epochs and not cut:
    #Paso 1: Selecciono un registro de entrada Xp
    x_index = np.random.choice(range(data.shape[0]))
    x = data[x_index]
    #Paso 2: Encontrar la neurona ganadora
    w_k = get_winner_neuron(grid,x)
    #Paso 3: Actualizar los pesos de las neuronas vecinas
    n_k = update_neighborhood_weight(weights, radius, w_k)
    
    for i in range(k):
      for j in range(k):
          if (j in n_k):
            weights[j] = weights[j] + eta * (x-weights[j])
            grid[i][j].weights = weights[j]
    t += 1
    eta = update_eta()
    radius = update_radius()

  plot_map(k,grid,countries)
  plot_u_matrix(k,grid)
kohonen()