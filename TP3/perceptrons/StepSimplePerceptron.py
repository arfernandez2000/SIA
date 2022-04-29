import numpy as np

from perceptrons.Perceptron import Perceptron
from plot_step_simple import add_w, plot

class StepSimplePerceptron(Perceptron):

    def update(self, err, w):
        change = super().update(err,w)
        if change:
            add_w(w)

    def activation(self,excitedState):
        return 1.0 if excitedState > 0.0 else -1.0

    def error(self,w,input,output):
        error = 0
        for u in range(len(input)):
            excitedState = np.dot(input[u], w)
            e = ((output[u] - self.activation(excitedState))**2)
            error += e
        return error/2