#import numpy
from perceptrons.perceptrons import *
from perceptrons.stepSimplePerceptron import *
from plot import plot
from config_loader import *

#Con 0.1 se queda corto, no se porque, tendria q llegar igual pero el error da 0 antes
perceptron = perceptrons(trainData, expectOut, 0.01, activationStepSimple, errorStepSimple)
perceptron.train(1000)
plot(perceptron.wMin, wait=True)