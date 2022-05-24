import pandas as pd
import numpy as np

#Paso Inicial
raw_data = pd.read_csv('europe.csv')
data = []
for r in range(len(raw_data)):
  data.append(raw_data.values[r][1:])
data = np.array(data)
medias = []
standard_deviation = []
columns = data.shape[1]

def normalize_2d(matrix):
    norm = np.linalg.norm(matrix)
    matrix = matrix/norm  # normalized matrix
    return matrix
print('not normalized: ', data)
data = normalize_2d(data)
print('normalized: ', data)