import numpy

def activatonLinearSimple(excitedState):
    return excitedState

def errorLinearSimple(training, expOut, w, p):
        trainLen = len(training)
        error = 0
        for i in range(trainLen):
            excitedState = numpy.inner(training[i], w)
            print('excited state: ', excitedState, '\n expected output: ', expOut[i])
            error += ((expOut[i] - (excitedState))**2)
        return error/2