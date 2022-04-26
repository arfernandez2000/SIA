import numpy

def activatonLinearSimple(excitedState):
    return excitedState

def errorLinearSimple(training, expOut, w, p):
        trainLen = len(training)
        error = 0
        for i in range(trainLen):
            excitedState = numpy.inner(training[i], w)
            error += ((expOut[i] - (excitedState))**2)
            #error += abs(activationStepSimple(excitedState) - expOut[i])
            #print(error)
        #return error/2
        return error/p