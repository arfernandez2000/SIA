import numpy as np
from get_data import data, raw_data
#Paso Inicial: Inicializo valores
k = 5 # Revisar
p = len(raw_data)
n = data.shape[1]

def set_init_weights():
  w = []
  for _ in range(1,p):
    wi = np.random.rand(n)
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
    #Paso 1: Selecciono un registro de entrada Xp
    x_index = np.random.choice(range(data.shape[0]))
    x = data[x_index]
    #Paso 2: Encontrar la neurona ganadora
    aux = []
    for w in weights:
      aux.append(x - w)
    w_k = np.argmin(aux)
    #Paso 3: Actualizar los pesos de las neuronas vecinas
    t += 1
kohonen()