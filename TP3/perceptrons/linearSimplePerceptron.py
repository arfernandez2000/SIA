import numpy as np

def activatonLinearSimple(excitedState):
    return excitedState

def errorLinearSimple(training, expOut, w, p):
        error = 0
        print(p)
        for i in range(p):
            excitedState = np.dot(training[i], w)
            print(excitedState,' - ', expOut[i], ' = ', excitedState - expOut[i] )
            error += ((expOut[i] - excitedState)**2)
            #print(error)
        return error/2