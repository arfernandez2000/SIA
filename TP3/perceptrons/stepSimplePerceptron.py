import numpy as np

def activationStepSimple(excitedState):
    return 1.0 if excitedState > 0.0 else -1.0

def errorStepSimple(training, expOut, w, p):
        error = 0
        for u in range(p):
            excitedState = np.dot(training[u], w)
            print(excitedState)
            e = ((expOut[u] - activationStepSimple(excitedState))**2)
            error += e
        return error/2