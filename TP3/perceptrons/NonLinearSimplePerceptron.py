import numpy as np
from sklearn.linear_model import Perceptron
from sympy import *

from plot_linear_errors import add_error

class NonLinearSimplePerceptron(Perceptron):
    beta = 0.4
    def g(self,x):
        return np.tanh(beta*x)

    def g_prime(self,x):
        return 1 - np.tanh(x)**2

    def activation(self,excitedState):
        return self.g(excitedState)

    def delta(self, i_x, excitedState, E_i):
        return super().delta(i_x,excitedState,E_i) * self.g_prime(excitedState)

    def update(self, err, w):
        change = super().update(err,w)
        if change:
            add_error(err)
    
    max_output = None
    min_output = None

    def error(self, training, expOut, w, p):
        if (not self.max_output):
            max_output = np.amax(expOut)
        if (not self.min_output):
            min_output = np.amax(expOut)

        error = 0
        for i in range(p):
            excitedState = np.dot(training[i], w)
            activation = self.activation(excitedState)
            print('activation: ', activation)
            output = expOut[i]
            normalized_output = ((output-min_output)/(max_output-min_output)) * 2 - 1
            print('normalized: ', normalized_output)
            e = ((normalized_output - self.activation(excitedState))**2)
            error += e
        return error/2