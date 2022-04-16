import numpy

from perceptrons.perceptrons import *
from perceptrons.stepSimplePerceptron import *


trainData = numpy.array([[-1,1], [1,-1], [-1,-1] , [1,1]])
expectOut = numpy.array([1,1,-1,-1])

perceptron = perceptrons(trainData, expectOut, 0.1, activationStepSimple, errorStepSimple)
perceptron.train(5)
