import numpy as np
from get_data import data, raw_data
#Paso Inicial
k = 5
p = len(raw_data)
n = len(raw_data.columns)

def set_init_weights():
  w = []
  for _ in range(1,n):
    wi = np.random.rand(p)
    w.append(wi)
  return np.array(w)

def kohonen(init_radius = 1, init_learn_rate = 0.5, max_epochs = 100):
  #Paso Inicial
  weights = set_init_weights()
  radius = init_radius
  learn_rate = init_learn_rate
  t = 1
  cut = False
  #Paso t
  while t < max_epochs and not cut:
    #Selecciono un registro de entrada Xp
    print(data)
    x_index = np.random.choice(range(data.shape[0]))
    x = data[x_index]
    print('weights: ', weights, 'x: ', x)
    aux = x - weights
    w_k = np.argmin(aux)
    print(w_k)
    t += 1
kohonen()