import numpy as np
from sympy import *

beta = 0.4
def g(x):
    return np.tanh(beta*x)

def g_prime(x):
    return 1 - np.tanh(x)**2

def activationNonLinearSimple(excitedState):
    return g(excitedState)

def errorNonLinearSimple(training, expOut, w, p):
    error = 0
    for i in range(p):
        excitedState = np.dot(training[i], w)
        activation = activationNonLinearSimple(excitedState)
        print('activation: ', activation)
        e = ((expOut[i] - activationNonLinearSimple(excitedState))**2)
        #print('error: ', e)
        error += e
    return error/2