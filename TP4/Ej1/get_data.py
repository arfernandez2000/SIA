import pandas as pd
import numpy as np

#Paso Inicial
raw_data = pd.read_csv('europe.csv')
data = np.array(list(map(lambda x: x[1:], raw_data.values)))

def normalize_2d(matrix):
    norm = np.linalg.norm(matrix)
    matrix = matrix/norm  # normalized matrix
    return matrix

data = normalize_2d(data)