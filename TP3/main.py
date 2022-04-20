import numpy

from perceptrons.perceptrons import *
from perceptrons.stepSimplePerceptron import *
from plot import plot

trainData = numpy.array([[-1,1,1], [1,-1,1], [-1,-1,1] , [1,1,1]])
expectOut = numpy.array([-1,-1,-1,1])

perceptron = perceptrons(trainData, expectOut, 0.3, activationStepSimple, errorStepSimple)
perceptron.train(1000)
plot(perceptron.wMin,trainData,expectOut)