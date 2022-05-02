#import numpy
from ex3 import ex3
from ex1 import ex1
from perceptrons.NonLinearSimplePerceptron import *
from perceptrons.Perceptron import *
from perceptrons.StepSimplePerceptron import *
from perceptrons.LinearSimplePerceptron import *

from config_loader import *
from plot_step_simple import plot as plot_step
from plot_errors import plot as plot_errors

if perceptron == 'multi-layer':
    print('multi capa')
    ex3()

elif perceptron == "non-linear":
    non_linear_perceptron = NonLinearSimplePerceptron(trainDataEx2, expectOutEx2, 0.1, 0.5)
    non_linear_perceptron.train(50000)
    plot_errors()
   
elif perceptron == "linear":
    linear_perceptron = LinearSimplePerceptron(test_trainDataEx2, test_expectOutEx2, 0.01)
    linear_perceptron.train(1000)
    plot_errors()

else:
    ex1()