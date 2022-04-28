#import numpy
from perceptrons.nonLinearSimplePerceptron import activationNonLinearSimple, errorNonLinearSimple, g_prime
from perceptrons.perceptrons import *
from perceptrons.stepSimplePerceptron import *
from perceptrons.linearSimplePerceptron import *
from config_loader import *
from plot_step_simple import plot as plot_step
from plot_linear_errors import plot as plot_linear

if perceptron == "non-linear":
    non_linear_perceptron = perceptrons(trainDataEx2, expectOutEx2, 0.01, activationNonLinearSimple, errorNonLinearSimple, g_prime=g_prime)
    non_linear_perceptron.train(1000)
    print(non_linear_perceptron.wMin, '\nError: ', non_linear_perceptron.errorMin)

elif perceptron == "linear":
    linear_perceptron = perceptrons(test_trainDataEx2, test_expectOutEx2, 0.01, activatonLinearSimple, errorLinearSimple)
    linear_perceptron.train(1000)
    print(linear_perceptron.wMin, '\nError: ', linear_perceptron.errorMin)
    plot_linear()

else:
    perceptron = perceptrons(trainDataEx1, expectOutEx1, 0.01, activationStepSimple, errorStepSimple, isSimple=True)
    perceptron.train(1000)
    plot_step()