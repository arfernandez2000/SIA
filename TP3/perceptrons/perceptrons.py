import numpy as np
from perceptrons.nonLinearSimplePerceptron import g_prime
from plot_step_simple import add_w
from plot_linear_errors import add_error

class perceptrons:

    def __init__(self, training, expOut, learnRate, activation, error, isSimple = False, g_prime = None):
        self.error = error
        self.activation = activation
        self.learnRate = learnRate
        self.expOut = expOut #ya me los pasan como arrays, hay que hacerlo en el ej1
        self.training = training
        self.errorMin = None
        self.wMin = None
        self.isSimple = isSimple
        self.g_prime = g_prime

    def delta(self, i_x, excitedState, E_i):
        activationState = self.activation(excitedState)
        delta = self.learnRate * (self.expOut[i_x] - activationState) * E_i

        if self.g_prime:
            delta = delta * self.g_prime(excitedState)

        return delta

    def train(self, cota):
        print(self.g_prime)
        i = 0 
        length = len(self.training)
        dim = len(self.training[0])
        w = np.append(np.zeros(dim-1),1)
        self.errorMin = length * 2
        error = 1

        while error > 0 and i < cota:
            i_x = np.random.randint(0, length)
            excitedState = np.dot(self.training[i_x], w)
            E_i = np.array(self.training[i_x])

            deltaW = self.delta(i_x,excitedState,E_i)
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