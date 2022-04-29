import numpy as np
from sklearn.linear_model import Perceptron

from plot_linear_errors import add_error

class LinearSimplePerceptron(Perceptron):

    def update(self, err, w):
        change = super().update(err,w)
        if change:
            add_error(err)
    
    def activation(self,excitedState):
        return excitedState

    def error(self,training,expOut,w,p):
        error = 0
        for i in range(p):
            excitedState = np.dot(training[i], w)
            print(excitedState)
            e = ((expOut[i] - excitedState)**2)
            error += e
        return error/2