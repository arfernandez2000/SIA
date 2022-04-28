import numpy as np
from plot_step_simple import add_w
from plot_linear_errors import add_error

class perceptrons:

    def __init__(self, training, expOut, learnRate, activation, error, isSimple = False):
        self.error = error
        self.activation = activation
        self.learnRate = learnRate
        self.expOut = expOut #ya me los pasan como arrays, hay que hacerlo en el ej1
        self.training = training
        self.errorMin = None
        self.wMin = None
        self.isSimple =isSimple
    
    def train(self, cota):
        i = 0 
        length = len(self.training)
        dim = len(self.training[0])
        w = np.append(np.zeros(dim-1),1)
        self.errorMin = length * 2
        error = 1

        while error > 0 and i < cota:
            i_x = np.random.randint(0, length)
            excitedState = np.dot(self.training[i_x], w)
            activationState = self.activation(excitedState)
            E_i = np.array(self.training[i_x])
            deltaW = self.learnRate * (self.expOut[i_x] - activationState) * E_i
            w += deltaW
            error = self.error(self.training, self.expOut, w, length)
            if error < self.errorMin:
                self.errorMin = error
                print(error)
                self.wMin = w
                if self.isSimple: 
                    add_w(w)
                else:
                    add_error(error)
            i += 1