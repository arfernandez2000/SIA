from turtle import end_fill
import numpy


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
        w = numpy.zeros(dim)
        error = 1
        self.errorMin = length * 2
        while error > 0 and i < cota:
            i_x = numpy.random.randint(0, length)
            excitedState = numpy.inner(self.training[i_x], w)
            activationState = self.activation(excitedState)
            deltaW = self.learnRate * (self.expOut[i_x] - activationState) * self.training[i_x]
            print("w", w)
            print("delta", deltaW)
            w += deltaW
            print("despues", w)
            error = self.error(self.training, self.expOut, w)
            if error < self.errorMin:
                self.errorMin = error
                self.wMin = w
            i += 1
        print(self.errorMin)
        print(self.wMin)