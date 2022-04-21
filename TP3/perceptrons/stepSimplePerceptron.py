import numpy

def activationStepSimple(excitedState):
    return 1.0 if excitedState >= 0.0 else -1.0

def errorStepSimple(training, expOut, w, p):
        trainLen = len(training)
        error = 0
        for i in range(trainLen):
            excitedState = numpy.inner(training[i], w)
            error += ((expOut[i] - activationStepSimple(excitedState))**2)
            #error += abs(activationStepSimple(excitedState) - expOut[i])
            #print(error)
        #return error/2
        return error/p