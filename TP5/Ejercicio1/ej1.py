# Implementar un Autoencoder b´asico para 
# las im´agenes binarias de la lista de
# caracteres del archivo ”font.h”
#
# 1. Plantear una arquitectura de red para el Codificador 
# y Decodificar que permita
# representar los datos de entrada en dos dimensiones.
#
# 2. Describan y estudien las diferentes tecnicas de 
# optimizacion que fueron aplicando
# para permitir que la red aprenda todo el set de datos 
# o un subconjunto del
# mismo. En el caso de que sea un subconjunto mostrar 
# porque no fue posible
# aprender el dataset completo.
#
# 3. Realizar el grafico en dos dimensiones que muestre 
# los datos de entrada en el
# espacio latente.
#
# 4. Mostrar como la red puede generar una nueva letra que 
# no pertenece al conjunto
# de entrenamiento.

import numpy as np
from fonts import *
# from 

character_template = np.array([[0] * 5] * 7)
character = np.copy(font_1[1])
character.resize(7, 1)

bin_array = np.zeros(5, dtype=int)
for i in range(0,5):
    bin_array[4-i] = character[0] & 1
    character[0] >>= 1
bin_array.resize(1, 5)

