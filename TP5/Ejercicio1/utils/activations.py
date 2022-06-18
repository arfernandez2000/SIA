import numpy as np

def lineal_act(x):
    return x

def der_lineal_act(x):
    return 1

def tanh_act(x):
    return np.tanh(1 * x)

def der_tanh_act(x):
    return 1 * (1 - tanh_act(x)**2)

def logist(x):
    return 1 / (1 + np.e**(-2 * 1 * x))

def der_logist(x):
    return 2 * 1 * logist(x) * (1 - logist(x))