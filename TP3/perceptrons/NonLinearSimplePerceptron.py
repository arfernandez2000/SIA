import numpy as np

from perceptrons.Perceptron import Perceptron
from plot_linear_errors import add_error

class NonLinearSimplePerceptron(Perceptron):
    def __init__(self, training_set, expected_output,learning_rate, beta):
        max_output = np.amax(expected_output)
        min_output = np.amin(expected_output)
        output = [None] * len(expected_output)
        for i in range(len(expected_output)):
            output[i] = 2 * ((expected_output[i] - min_output) / (max_output - min_output)) - 1
            print("OUTPUT", output[i])
        super().__init__( training_set,  output,learning_rate, beta)

    def g(self,x):
        return np.tanh(self.beta*x)

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
            e = ((output - activation)**2)
            error += e
        return error/2