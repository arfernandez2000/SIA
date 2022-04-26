import numpy as np
from plot_step_simple import add_w

class perceptrons:

    def __init__(self, training, expOut, learnRate, activation, error):
        self.error = error
        self.activation = activation
        self.learnRate = learnRate
        self.expOut = expOut #ya me los pasan como arrays, hay que hacerlo en el ej1
        self.training = training
        self.errorMin = None
        self.wMin = None
    
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
            print('DELTA: ', deltaW, 'W: ', w)
            error = self.error(self.training, self.expOut, w, length)
            #print(error)
            if error < self.errorMin:
                self.errorMin = error
                self.wMin = w
                add_w(w)
            i += 1
        
        print(self.wMin)
        print(self.errorMin)