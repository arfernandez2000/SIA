#import numpy
from perceptrons.perceptrons import *
from perceptrons.stepSimplePerceptron import *
from config_loader import *
from plot import plot

#Con 0.1 se queda corto, no se porque, tendria q llegar igual pero el error da 0 antes
perceptron = perceptrons(trainData, expectOut, 0.001, activationStepSimple, errorStepSimple)
perceptron.train(1000)
plot()