#import numpy
from perceptrons.perceptrons import *
from perceptrons.stepSimplePerceptron import *
from perceptrons.linearSimplePerceptron import *
from config_loader import *
from plot_step_simple import plot

if perceptron == "linear":
    linear_perceptron = perceptrons(test_trainDataEx2_linear, test_expectOutEx2_linear, 0.5, activatonLinearSimple, errorLinearSimple)
    linear_perceptron.train(1000)
    print(linear_perceptron.wMin, '\nError: ', linear_perceptron.errorMin)

else:
    perceptron = perceptrons(trainDataEx1, expectOutEx1, 0.01, activationStepSimple, errorStepSimple, isSimple=True)
    perceptron.train(1000)
    plot()