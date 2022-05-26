import numpy as np
from get_data import data, raw_data
from Neuron import Neuron
from utils import * 

def update_weigth(eta, s, weights, j):
    return weights + eta * s * (data[j] - s * weights)

def activation(weights, j):
    s = 0
    for i in range(len(data[j])):
        s += data[j][i] * weights[i]
    return s

def oja(epochs = 5000, eta = 0.0001):
    print("DATA", data)
    N = len(data)
    weights = np.random.uniform(-1, 1, len(data[0]))

    for i in range(0, epochs):
        for j in range(0, N):
            s = activation(weights, j)
            weights = update_weigth(eta, s, weights, j)
    print("WEIGHTS: ", weights)


oja()