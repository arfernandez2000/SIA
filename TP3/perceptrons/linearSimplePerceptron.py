import numpy as np

def activatonLinearSimple(excitedState):
    return excitedState

def errorLinearSimple(training, expOut, w, p):
        error = 0
        for i in range(p):
            excitedState = np.dot(training[i], w)
            e = ((expOut[i] - excitedState)**2)
            print(e)
            error += e
        return error/2