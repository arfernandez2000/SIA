import pandas as pd
import numpy as np

#Paso Inicial
data = pd.read_csv('europe.csv')
k = 5
p = len(data)
n = len(data.columns)

def set_init_weights():
  w = []
  for _ in range(1,k*k):
    wi = np.random.rand(n)
    w.append(wi)
  return np.array(w)

def kohonen(init_radius = 1, init_learn_rate = 0.5, max_epochs = 1000):
  #Paso Inicial
  weights = set_init_weights()
  radius = init_radius
  learn_rate = init_learn_rate
  t = 1
  cut = False
  #Paso t
  while t < max_epochs and not cut:
    #Selecciono un registro de entrada Xp
    x_index = np.random.choice(data.index)
    x = data.values[x_index]
    #w_k = 
    t += 1
kohonen()