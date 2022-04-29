from abc import ABC, abstractmethod
import numpy as np
from plot_step_simple import add_w
from plot_errors import add_error

class Perceptron(ABC):

    def __init__(self, training, expOut, learnRate):
        self.learnRate = learnRate
        self.expOut = expOut
        self.training = training
        self.errorMin = None
        self.wMin = None
        self.length = len(training)
    
    @abstractmethod
    def activation(self):
        pass

    @abstractmethod
    def error(self):
        pass

    def delta(self, i_x, excitedState, E_i):
        activationState = self.activation(excitedState)
        delta = self.learnRate * (self.expOut[i_x] - activationState) * E_i
        return delta
    
    def update(self, err, w):
        if err < self.errorMin:
            self.errorMin = err
            self.wMin = w
            return True
        return False

    def train(self, cota):
        i = 0 
        length = len(self.training)
        dim = len(self.training[0])
        w = np.append(np.zeros(dim-1),1)
        self.errorMin = length * 2
        error = 1

        while error > 0.001 and i < cota:
            i_x = np.random.randint(0, length)
            excitedState = np.dot(self.training[i_x], w)
            E_i = np.array(self.training[i_x])
            deltaW = self.delta(i_x,excitedState,E_i)
            w += deltaW

            error = self.error(w, self.training, self.expOut)
            self.update(error,w)
            i += 1
        print('Error minimo: ',self.errorMin)
        print('W minimo: ', self.wMin)

    def test(self, test_input, test_output):
        error = self.error(self.wMin, test_input, test_output)
        print(error)
        return error