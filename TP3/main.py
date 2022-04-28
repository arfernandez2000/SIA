#import numpy
from perceptrons.perceptrons import *
from perceptrons.stepSimplePerceptron import *
from perceptrons.linearSimplePerceptron import *
from config_loader import *
from plot_step_simple import plot

if perceptron == "linear":
    train = load_entries()
    goals = load_goals()
    linear_perceptron = perceptrons(trainData, expectOut, 0.01, activatonLinearSimple, errorLinearSimple)
    linear_perceptron.train(1000)
    print(linear_perceptron.wMin, '\nError: ', linear_perceptron.errorMin)

else:
    perceptron = perceptrons(trainData, expectOut, 0.01, activationStepSimple, errorStepSimple)
    perceptron.train(5000)
    plot()