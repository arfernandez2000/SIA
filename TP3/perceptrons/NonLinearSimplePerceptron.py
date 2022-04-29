import numpy as np

from perceptrons.Perceptron import Perceptron
from plot_errors import add_error

class NonLinearSimplePerceptron(Perceptron):
    def __init__(self, training_set, expected_output,learning_rate, beta):
        self.beta = beta
        print(self.beta)
        max_output = np.amax(expected_output)
        min_output = np.amin(expected_output)
        output = [None] * len(expected_output)
        for i in range(len(expected_output)):
            output[i] = 2 * ((expected_output[i] - min_output) / (max_output - min_output)) - 1
        super().__init__(training_set,output,learning_rate)

    def g(self,x):
        return np.tanh(self.beta*x)

    def g_prime(self,x):
        return (1 - np.tanh(x)**2)*self.beta

    def activation(self,excitedState):
        return self.g(excitedState)

    def delta(self, i_x, excitedState, E_i):
        max_output = np.amax(self.training)
        min_output = np.amin(self.training)
        E_i = 2 * ((E_i - min_output) / (max_output - min_output)) - 1
        return super().delta(i_x,excitedState,E_i) * self.g_prime(excitedState)

    def update(self, err, w):
        change = super().update(err,w)
        if change:
            add_error(err)

    def error(self, w):
        error = 0
        for i in range(self.length):
            excitedState = np.dot(self.training[i], w)
            activation = self.activation(excitedState)
            output = self.expOut[i]
            e = ((output - activation)**2)
            error += e
        return error/2