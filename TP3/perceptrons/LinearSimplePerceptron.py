import numpy as np

from perceptrons.Perceptron import Perceptron
from plot_errors import add_error

class LinearSimplePerceptron(Perceptron):

    def update(self, err, w):
        super().update(err,w)
        add_error(err)

    def activation(self,excitedState):
        return excitedState

    def error(self,w,input,output):
        error = 0
        for i in range(len(input)):
            excitedState = np.dot(input[i], w)
            e = ((output[i] - excitedState)**2)
            error += e
        return error/2