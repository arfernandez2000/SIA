import numpy
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
        w = numpy.append(numpy.zeros(dim-1),1)
        #print(w,self.training)
        self.errorMin = length * 2
        error = 1
        while error > 0 and i < cota:
            i_x = numpy.random.randint(0, length)
            excitedState = numpy.inner(self.training[i_x], w)
            #print('i_x', self.training[i_x])
            activationState = self.activation(excitedState)
            #print(activationState)
            print(self.learnRate)
            print(self.expOut[i_x])
            print(activationState)
            print(self.training[i_x])
            deltaW = self.learnRate * ((self.expOut[i_x] - activationState) * self.training[i_x]) #error aca, self.training[i_x] tiene dimension 3
            w += deltaW
            error = self.error(self.training, self.expOut, w, length)
            if error < self.errorMin:
                self.errorMin = error
                self.wMin = w
                add_w(w)
            i += 1