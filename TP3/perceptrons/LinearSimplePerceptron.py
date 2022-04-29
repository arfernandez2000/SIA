import numpy as np

from perceptrons.Perceptron import Perceptron
from plot_linear_errors import add_error

class LinearSimplePerceptron(Perceptron):

    def update(self, err, w):
        change = super().update(err,w)
        if change:
            add_error(err)
    
    def activation(self,excitedState):
        return excitedState

    def error(self,w):
        error = 0
        for i in range(self.length):
            excitedState = np.dot(self.training[i], w)
            print(excitedState)
            e = ((self.expOut[i] - excitedState)**2)
            error += e
        return error/2